import type { Lang } from "./lang";

export const LANG_NUM: Record<Lang, number> = {
  en: 1,
  de: 2,
  fr: 3,
  pl: 4,
  ko: 5,
};

const SINO = ["\uc601", "\uc77c", "\uc774", "\uc0bc", "\uc0ac", "\uc624", "\uc721", "\uce60", "\ud314", "\uad6c"];
const NATIVE = ["\uc601", "\ud558\ub098", "\ub458", "\uc14b", "\ub137", "\ub2e4\uc12f", "\uc5ec\uc12f", "\uc77c\uacf1", "\uc5ec\ub35f", "\uc544\ud649"];

export type NikitaGloss = {
  line: string;
  morph: number;
  word: number;
  n: number;
  hybris: number;
};

export function morphCount(text: string): number {
  const hangul = text.match(/[\uAC00-\uD7A3]/g)?.length ?? 0;
  const words = text.trim().split(/\s+/).filter(Boolean).length;
  return hangul > 0 ? hangul : words;
}

export function wordNum(text: string): number {
  let s = 0;
  for (let i = 0; i < text.length; i += 1) s += text.charCodeAt(i);
  return s % 9;
}

export function hybrisOf(langs: Record<Lang, number>): number {
  const vals = Object.values(langs);
  const total = vals.reduce((a, b) => a + b, 0);
  if (total <= 0) return 0;
  const max = Math.max(...vals);
  const ko = (langs.ko ?? 0) / total;
  return Math.max(0, max / total - 1 / 5 - ko * 0.12);
}

export function gloss(
  text: string,
  lang: Lang,
  empire: string,
  wave: number,
  step: number,
  langs: Record<Lang, number>,
): NikitaGloss {
  const morph = morphCount(text);
  const word = wordNum(text);
  const n = LANG_NUM[lang];
  const hybris = hybrisOf(langs);
  const native = NATIVE[n] ?? "\uc601";
  const sino = SINO[morph % 10];
  const line = `NKITA ${native}/${sino} ${n}\u00b7${empire} m${morph} w${word} e${step} v${wave}`;
  return { line, morph, word, n, hybris };
}
