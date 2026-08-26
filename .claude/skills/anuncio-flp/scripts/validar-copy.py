#!/usr/bin/env python3
"""
Valida um arquivo de copy de anuncio ANTES de gastar credito gerando imagem.

Uso:  python3 validar-copy.py <arquivo.md> [--max-head 45] [--max-sub 140]

Checa, por AD:
  1. Volume de texto medido, com piso e teto por campo
  2. Repeticao entre ADs (HEAD e SUBHEAD similares, frases reaproveitadas)
  3. Entrega da mensagem (HEAD + SUBHEAD dizem o que e, para quem e o que fazer)
  4. Vicios de Light Copy (travessao, exclamacao, pergunta no HEAD, emoji)
  5. CTA na forma exata

Sai com codigo 1 se houver qualquer REPROVA. Nao gere imagem com codigo 1.
"""
import re, sys, unicodedata
from difflib import SequenceMatcher
from collections import Counter

# ---- limites, medidos sobre peca de 1080 de largura -------------------------
# HEAD roda em display condensado 88-120px: ~22 chars/linha, 3 linhas de teto.
# SUBHEAD roda em 46-56px: ~50 chars/linha, 3 linhas de teto.
LIM = {
    "head":   {"min": 18, "alvo": 45, "max": 58},
    "sub":    {"min": 45, "alvo": 140, "max": 165},
    "total":  {"max": 210},          # HEAD + SUBHEAD somados na peca
}
CTA_OK = {
    'Clique em "Saiba mais" e garanta seu ingresso',
    'Clique em "Saiba mais" e veja como participar',
}
SIMILARIDADE_REPROVA = 0.62   # razao de SequenceMatcher entre dois HEADs
NGRAM = 4                     # sequencia de N palavras repetida entre ADs

def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9 ]", " ", s).split()

def parse(path):
    txt = open(path, encoding="utf-8").read()
    ads, cur = [], None
    for line in txt.splitlines():
        m = re.match(r"^##\s+AD\s+(\d+)\s*(?:·\s*(.*))?$", line.strip())
        if m:
            cur = {"n": m.group(1), "tipo": (m.group(2) or "").strip(),
                   "head": "", "sub": "", "cta": ""}
            ads.append(cur); continue
        if cur is None: continue
        for campo, rot in (("head", "HEAD"), ("sub", "SUBHEAD"), ("cta", "CTA")):
            mm = re.match(r"^\*\*%s:\*\*\s*`(.*)`\s*$" % rot, line.strip())
            if mm and not cur[campo]:
                cur[campo] = mm.group(1)
    return ads

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    path = sys.argv[1]
    for i, a in enumerate(sys.argv):
        if a == "--max-head": LIM["head"]["max"] = int(sys.argv[i+1])
        if a == "--max-sub":  LIM["sub"]["max"]  = int(sys.argv[i+1])

    ads = parse(path)
    if not ads:
        print("Nenhum AD encontrado. O arquivo usa '## AD NN' e '**HEAD:** `...`'?"); sys.exit(2)

    reprovas, alertas = [], []
    print(f"\n{'AD':<4}{'HEAD':>6}{'SUB':>6}{'TOTAL':>7}   situacao")
    print("-" * 58)
    for a in ads:
        h, s = len(a["head"]), len(a["sub"])
        t = h + s
        flags = []
        if not a["head"]: flags.append("SEM HEAD")
        if not a["sub"]:  flags.append("SEM SUBHEAD")
        if h > LIM["head"]["max"]: flags.append(f"HEAD +{h-LIM['head']['max']}")
        if s > LIM["sub"]["max"]:  flags.append(f"SUB +{s-LIM['sub']['max']}")
        if t > LIM["total"]["max"]: flags.append(f"TOTAL +{t-LIM['total']['max']}")
        if a["head"] and h < LIM["head"]["min"]: flags.append("HEAD curto")
        if a["cta"] and a["cta"] not in CTA_OK: flags.append("CTA fora da forma")
        # vicios de light copy
        campo = f"{a['head']} {a['sub']}"
        if "—" in campo or "–" in campo: flags.append("travessao")
        if "!" in campo: flags.append("exclamacao")
        if a["head"].endswith("?"): flags.append("HEAD e pergunta")
        if re.search(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", campo): flags.append("emoji")
        # entrega da mensagem: precisa dizer o que a pessoa ganha ou o que acontece
        if a["sub"] and len(norm(a["sub"])) < 12: flags.append("SUBHEAD nao entrega a mensagem")
        estado = "ok" if not flags else "; ".join(flags)
        if flags: reprovas.append((a["n"], estado))
        print(f"{a['n']:<4}{h:>6}{s:>6}{t:>7}   {estado}")

    # ---- repeticao entre ADs -------------------------------------------------
    print("\nRepeticao entre ADs")
    print("-" * 58)
    achou = False
    for i in range(len(ads)):
        for j in range(i+1, len(ads)):
            r = SequenceMatcher(None, " ".join(norm(ads[i]["head"])),
                                      " ".join(norm(ads[j]["head"]))).ratio()
            if r >= SIMILARIDADE_REPROVA:
                achou = True
                print(f"  AD {ads[i]['n']} x AD {ads[j]['n']}: HEADs {r:.0%} parecidas")
                reprovas.append((f"{ads[i]['n']}/{ads[j]['n']}", "HEADs repetidas"))
    # ngramas repetidos
    grams = Counter()
    onde = {}
    for a in ads:
        ws = norm(a["head"] + " " + a["sub"])
        vistos = set()
        for k in range(len(ws)-NGRAM+1):
            g = " ".join(ws[k:k+NGRAM])
            if g in vistos: continue
            vistos.add(g); grams[g] += 1
            onde.setdefault(g, []).append(a["n"])
    for g, c in grams.most_common():
        if c >= 3:
            achou = True
            print(f"  \"{g}\" aparece em {c} ADs: {', '.join(onde[g])}")
            alertas.append(g)
    if not achou:
        print("  nenhuma repeticao acima do limiar")

    print("\n" + "=" * 58)
    print(f"ADs analisados: {len(ads)}   reprovas: {len(reprovas)}   alertas: {len(alertas)}")
    print(f"limites: HEAD ate {LIM['head']['max']} · SUBHEAD ate {LIM['sub']['max']} · total ate {LIM['total']['max']}")
    if reprovas:
        print("\nNAO GERE IMAGEM. Corrija a copy e rode de novo.")
        sys.exit(1)
    print("\nCopy liberada para producao de imagem.")
    sys.exit(0)

if __name__ == "__main__":
    main()
