export function euclid(hits: number, steps: number): boolean[] {
  const n = Math.max(1, Math.floor(steps));
  const k = Math.max(0, Math.min(n, Math.floor(hits)));
  const pattern = Array.from({ length: n }, (_, i) =>
    Math.floor(((i + 1) * k) / n) !== Math.floor((i * k) / n),
  );
  const firstHit = pattern.indexOf(true);
  if (firstHit > 0) {
    return pattern.slice(firstHit).concat(pattern.slice(0, firstHit));
  }
  return pattern;
}

export function nextHit(pattern: boolean[], from: number): number {
  const n = pattern.length;
  for (let i = 1; i <= n; i += 1) {
    const j = (from + i) % n;
    if (pattern[j]) return j;
  }
  return from;
}
