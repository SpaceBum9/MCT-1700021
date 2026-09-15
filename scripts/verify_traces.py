#!/usr/bin/env python3
"""Verify MCT-1700021 trace ledger. HOLD is not execution.

Canonical mixer matches MCT-2600027 training/engine.py:
  json.dumps(value, sort_keys=True, separators=(\",\", \":\"), ensure_ascii=False)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOTS = frozenset({"CG-KERNEL-2026-08-19", "MCT-170021-CORE"})
HUMAN = re.compile(r"^MCT-1700021-TR-[0-9]{8}-[0-9]{4}Z$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
V1_REQUIRED = (
    "schema_version",
    "suite",
    "human_id",
    "parent_trace_id",
    "parent_human_id",
    "role",
    "action",
    "outcome",
    "timestamp",
    "consensus_score",
    "live_rail",
    "execute",
    "hold",
    "limits",
)


def repo_root() -> Path:
    here = Path(__file__).resolve()
    return here.parents[1]


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def digest_minus_tid(obj: dict[str, Any]) -> str:
    payload = {k: v for k, v in obj.items() if k not in ("trace_id", "checkpoint_sha256")}
    return sha256_text(canonical_json(payload))


def human_id_of(obj: dict[str, Any], path: Path) -> str:
    hid = obj.get("human_id")
    if isinstance(hid, str) and HUMAN.match(hid):
        return hid
    tid = obj.get("trace_id")
    if isinstance(tid, str) and HUMAN.match(tid):
        return tid
    stem = path.stem
    if HUMAN.match(stem):
        return stem
    return stem


def classify_hash(obj: dict[str, Any], raw: bytes) -> dict[str, Any]:
    tid = obj.get("trace_id")
    minus = digest_minus_tid(obj)
    full = sha256_text(canonical_json(obj))
    raw_hex = hashlib.sha256(raw).hexdigest()
    orig = dict(obj)
    orig.pop("trace_id", None)
    orig.pop("checkpoint_sha256", None)
    orig_order = sha256_text(json.dumps(orig, separators=(",", ":"), ensure_ascii=False))
    status = "legacy_human"
    if isinstance(tid, str) and SHA256.match(tid):
        if tid == minus:
            status = "verified_canon"
        elif tid == orig_order:
            status = "verified_origorder"
        elif tid == full:
            status = "verified_full"
        else:
            status = "unverified"
    elif isinstance(tid, str) and HUMAN.match(tid):
        status = "legacy_human"
    else:
        status = "missing_or_other"
    return {
        "claimed_trace_id": tid,
        "hash_status": status,
        "canon_minus_tid": minus,
        "canon_full": full,
        "raw_sha256": raw_hex,
        "origorder_minus_tid": orig_order,
    }


def load_traces(trace_dir: Path) -> list[dict[str, Any]]:
    nodes: list[dict[str, Any]] = []
    for path in sorted(trace_dir.glob("MCT-1700021-TR-*.json")):
        raw = path.read_bytes()
        obj = json.loads(raw.decode("utf-8"))
        if not isinstance(obj, dict):
            raise SystemExit(f"{path.name}: root is not an object")
        hid = human_id_of(obj, path)
        digest = classify_hash(obj, raw)
        v1 = obj.get("schema_version") == 1
        nodes.append(
            {
                "file": path.name,
                "human_id": hid,
                "schema_version": obj.get("schema_version"),
                "role": obj.get("role"),
                "action": obj.get("action"),
                "outcome": obj.get("outcome"),
                "timestamp": obj.get("timestamp"),
                "consensus_score": obj.get("consensus_score"),
                "parent_trace_id": obj.get("parent_trace_id"),
                "parent_human_id": obj.get("parent_human_id"),
                "live_rail": obj.get("live_rail"),
                "execute": obj.get("execute"),
                "hold": obj.get("hold"),
                "v1": v1,
                **digest,
            }
        )
    return nodes


def parent_ok(node: dict[str, Any], by_human: dict[str, Any], by_hash: dict[str, Any]) -> bool:
    parent = node.get("parent_trace_id")
    parent_h = node.get("parent_human_id")
    if parent in ROOTS:
        return True
    if isinstance(parent, str) and (parent in by_human or parent in by_hash):
        return True
    if isinstance(parent_h, str) and (parent_h in by_human or parent_h in ROOTS):
        return True
    return False


def check_v1(obj: dict[str, Any], node: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in V1_REQUIRED:
        if field not in obj:
            errors.append(f"missing {field}")
    if obj.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if obj.get("suite") != "MCT-1700021":
        errors.append("suite must be MCT-1700021")
    if obj.get("live_rail") is not False:
        errors.append("live_rail must be false")
    if obj.get("execute") is not False:
        errors.append("execute must be false")
    if node["hash_status"] != "verified_canon":
        errors.append("trace_id must equal canon SHA-256 minus trace_id")
    return errors


def build_chain(nodes: list[dict[str, Any]]) -> dict[str, Any]:
    head = nodes[-1] if nodes else None
    return {
        "schema_version": 1,
        "suite": "MCT-1700021",
        "lineage_trace_id": "MCT-170021-CORE",
        "updated": "2026-09-15T21:14:00.000Z",
        "mixer": "MCT-2600027/training/engine.py canonical JSON SHA-256",
        "live_rail": False,
        "execute": False,
        "count": len(nodes),
        "head": None
        if head is None
        else {
            "human_id": head["human_id"],
            "claimed_trace_id": head["claimed_trace_id"],
            "canon_minus_tid": head["canon_minus_tid"],
            "hash_status": head["hash_status"],
            "parent_trace_id": head["parent_trace_id"],
            "parent_human_id": head["parent_human_id"],
            "role": head["role"],
            "action": head["action"],
            "outcome": head["outcome"],
            "consensus_score": head["consensus_score"],
            "timestamp": head["timestamp"],
        },
        "nodes": [
            {
                "human_id": n["human_id"],
                "file": n["file"],
                "claimed_trace_id": n["claimed_trace_id"],
                "canon_minus_tid": n["canon_minus_tid"],
                "hash_status": n["hash_status"],
                "parent_trace_id": n["parent_trace_id"],
                "parent_human_id": n["parent_human_id"],
                "role": n["role"],
                "action": n["action"],
                "outcome": n["outcome"],
                "timestamp": n["timestamp"],
            }
            for n in nodes
        ],
    }


def load_known_gaps(root: Path) -> set[tuple[str, str]]:
    path = root / "schema" / "known-gaps.json"
    if not path.exists():
        return set()
    raw = json.loads(path.read_text(encoding="utf-8"))
    out: set[tuple[str, str]] = set()
    for item in raw.get("missing_parents", []):
        out.add((item["child"], item["parent_trace_id"]))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify MCT-1700021 traces")
    parser.add_argument("--write-chain", action="store_true")
    parser.add_argument("--strict", action="store_true", help="fail on recorded known gaps")
    parser.add_argument("--root", type=Path, default=None)
    args = parser.parse_args()
    root = args.root or repo_root()
    trace_dir = root / "traces"
    if not trace_dir.is_dir():
        print(f"missing {trace_dir}", file=sys.stderr)
        return 2

    known_gaps = load_known_gaps(root)
    findings: list[str] = []
    recorded: list[str] = []
    nodes = load_traces(trace_dir)
    if not nodes:
        findings.append("no trace files")

    by_human = {n["human_id"]: n for n in nodes}
    by_hash: dict[str, dict[str, Any]] = {}
    for n in nodes:
        for key in ("claimed_trace_id", "canon_minus_tid", "canon_full", "raw_sha256"):
            val = n.get(key)
            if isinstance(val, str) and SHA256.match(val):
                by_hash[val] = n

    for n in nodes:
        if n["file"] != f"{n['human_id']}.json":
            findings.append(f"{n['file']}: filename != human_id")
        if n.get("parent_trace_id") is None:
            findings.append(f"{n['human_id']}: missing parent_trace_id")
        elif not parent_ok(n, by_human, by_hash):
            gap = (n["human_id"], str(n.get("parent_trace_id")))
            msg = (
                f"{n['human_id']}: unresolved parent {n.get('parent_trace_id')} / {n.get('parent_human_id')}"
            )
            if gap in known_gaps and not args.strict:
                recorded.append(msg)
            else:
                findings.append(msg)
        if n["v1"]:
            obj = json.loads((trace_dir / n["file"]).read_text(encoding="utf-8"))
            for err in check_v1(obj, n):
                findings.append(f"{n['human_id']}: v1 {err}")

    status_counts: dict[str, int] = {}
    for n in nodes:
        status_counts[n["hash_status"]] = status_counts.get(n["hash_status"], 0) + 1

    chain = build_chain(nodes)
    chain["hash_status_counts"] = status_counts
    chain["findings"] = findings
    chain["recorded_gaps"] = recorded
    chain["runtime_contract"] = {
        "repo": "SpaceBum9/MCT-2600027",
        "path": "training/engine.py",
        "note": "related-lineage runtime; not parent of this chain",
    }

    if args.write_chain:
        dest = trace_dir / "chain.json"
        dest.write_text(canonical_json(chain) + "\n", encoding="utf-8")
        print(f"wrote {dest} ({chain['count']} nodes)")

    print(f"traces={len(nodes)}")
    print("hash_status", status_counts)
    if findings:
        print("findings:")
        for item in findings:
            print(f"  - {item}")
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
