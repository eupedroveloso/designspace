#!/usr/bin/env python3
"""
Análise de composição e contraste de um criativo.

Responde três perguntas antes de posicionar qualquer texto:
  1. Onde está a massa do assunto?          → centro de massa da energia visual
  2. Onde o texto cabe sem brigar com ela?  → ranking de zonas livres
  3. O texto que já está lá tem contraste?  → pior caso, não média

QUANDO RODAR
    Momento certo: na IMAGEM GERADA, antes de montar o texto no Figma.
    O mapa de energia não sabe distinguir assunto de tipografia — se você rodar
    numa peça já montada, o próprio texto entra na conta como se fosse assunto
    e o centro de massa mente. Para auditar peça pronta, use --recorte para
    isolar só a foto, ou use apenas a parte de contraste.

Uso:
    python analise-composicao.py imagem.png
    python analise-composicao.py peca.png --texto 76,548,520,754
    python analise-composicao.py peca.png --recorte 0,280,1080,1350

    --texto x0,y0,x1,y1     mede contraste de UMA linha de UMA cor. Repetível.
                            Caixa com duas cores de texto dentro dá número falso;
                            o script avisa quando detecta.
    --tinta RRGGBB          força a cor do texto na próxima caixa --texto, em vez
                            de deixar o script inferir. Use sempre que souber o
                            token: é o número confiável.
    --recorte x0,y0,x1,y1   restringe a análise de composição a essa região.

Ambiente: venv com Pillow.
    python3 -m venv venv && ./venv/bin/pip install Pillow

Nenhum número aqui é estimado. Se o script discorda do olho, o olho está errado.
"""

import sys
from PIL import Image


# ---------------------------------------------------------------- luminância

def _srgb(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lum(rgb):
    """Luminância relativa WCAG."""
    return 0.2126 * _srgb(rgb[0]) + 0.7152 * _srgb(rgb[1]) + 0.0722 * _srgb(rgb[2])


def contraste(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def hexs(rgb):
    return "#%02X%02X%02X" % tuple(rgb[:3])


# ---------------------------------------------------------------- energia

def mapa_energia(img, cols=6, rows=8, passo=16):
    """
    Energia visual por célula = desvio da luminância + gradiente médio.

    Energia alta  = detalhe, textura, borda → é ali que mora o assunto.
    Energia baixa = massa chapada           → é ali que o texto cabe.
    """
    w, h = cols * passo, rows * passo
    px = img.convert("RGB").resize((w, h), Image.LANCZOS)
    d = px.load()
    L = [[lum(d[x, y]) for x in range(w)] for y in range(h)]

    cel = []
    for r in range(rows):
        linha = []
        for c in range(cols):
            y0, y1 = r * passo, (r + 1) * passo
            x0, x1 = c * passo, (c + 1) * passo
            vals, grad = [], []
            for y in range(y0, y1):
                fila = L[y]
                for x in range(x0, x1):
                    vals.append(fila[x])
                    if x + 1 < w:
                        grad.append(abs(fila[x + 1] - fila[x]))
                    if y + 1 < h:
                        grad.append(abs(L[y + 1][x] - fila[x]))
            m = sum(vals) / len(vals)
            dev = (sum((v - m) ** 2 for v in vals) / len(vals)) ** 0.5
            g = sum(grad) / len(grad) if grad else 0.0
            linha.append({"lum": m, "dev": dev, "grad": g, "energia": dev + g * 4})
        cel.append(linha)
    return cel


def centro_de_massa(cel):
    """Centro de massa da energia, em fração 0–1 do quadro."""
    rows, cols = len(cel), len(cel[0])
    tot = sx = sy = 0.0
    for r in range(rows):
        for c in range(cols):
            e = cel[r][c]["energia"]
            tot += e
            sx += e * (c + 0.5) / cols
            sy += e * (r + 0.5) / rows
    return (sx / tot, sy / tot) if tot else (0.5, 0.5)


def _acumulado(cel, campo):
    """Soma acumulada 2D — deixa a soma de qualquer retângulo em O(1)."""
    rows, cols = len(cel), len(cel[0])
    S = [[0.0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        linha = 0.0
        for c in range(cols):
            linha += cel[r][c][campo]
            S[r + 1][c + 1] = S[r][c + 1] + linha
    return S


def _soma(S, r0, r1, c0, c1):
    return S[r1][c1] - S[r0][c1] - S[r1][c0] + S[r0][c0]


def zonas_livres(cel, min_cols=2, min_rows=2):
    """Todos os retângulos de células, ordenados por energia média crescente."""
    rows, cols = len(cel), len(cel[0])
    SE, SL = _acumulado(cel, "energia"), _acumulado(cel, "lum")
    out = []
    for r0 in range(rows):
        for r1 in range(r0 + min_rows, rows + 1):
            for c0 in range(cols):
                for c1 in range(c0 + min_cols, cols + 1):
                    area = (r1 - r0) * (c1 - c0)
                    e = _soma(SE, r0, r1, c0, c1) / area
                    l = _soma(SL, r0, r1, c0, c1) / area
                    out.append({
                        "r0": r0, "r1": r1, "c0": c0, "c1": c1,
                        "energia": e, "lum": l, "area": area,
                        # prêmio por área: zona grande e calma vale mais que pequena e calma
                        "score": e / (area ** 0.5),
                    })
    out.sort(key=lambda z: z["score"])
    return out


# ---------------------------------------------------------------- contraste

def contraste_faixa(img, box, nome="", tinta=None):
    """
    Contraste PIOR CASO de uma faixa de texto.

    A média mente: sobre bokeh, a média passa e o ponto pior reprova.
    A tinta é o percentil extremo de luminância e o fundo é medido em três
    níveis — escuro, médio e claro. Vale o menor dos três.

    A tinta é detectada como a população MINORITÁRIA entre os dois extremos:
    numa caixa justa o texto ocupa menos área que o fundo. Critério por
    distância da média falha em cena clara, onde o estouro do bokeh se afasta
    mais da média do que a própria tinta escura. Passe `tinta` para forçar.
    """
    x0, y0, x1, y1 = box
    px = img.crop((x0, y0, x1, y1)).convert("RGB")
    data = list(px.getdata())
    pares = sorted(((lum(p), p) for p in data), key=lambda t: t[0])
    n = len(pares)

    if tinta is None:
        escuro, claro = pares[int(n * 0.02)][1], pares[int(n * 0.98)][1]
        f_esc = sum(1 for _, p in pares if dist_cor(p, escuro) < 60) / n
        f_cla = sum(1 for _, p in pares if dist_cor(p, claro) < 60) / n
        tinta = escuro if f_esc <= f_cla else claro

    def dist(p):
        return sum((p[i] - tinta[i]) ** 2 for i in range(3)) ** 0.5

    fundo = [(l, p) for l, p in pares if dist(p) > 90] or pares
    m = len(fundo)
    p10, p50, p90 = fundo[int(m * .10)][1], fundo[int(m * .50)][1], fundo[int(m * .90)][1]
    cs = [contraste(tinta, p) for p in (p10, p50, p90)]
    pior = min(cs)

    mf = sum(l for l, _ in fundo) / m
    dev = (sum((l - mf) ** 2 for l, _ in fundo) / m) ** 0.5

    # Guarda contra falso positivo: se a amostra extrema for uma cor saturada
    # ocupando pouca área, quase certamente é OUTRA COR DE TEXTO na mesma caixa
    # (acento do headline), não fundo. Aí a caixa está errada, não a peça.
    def satura(p):
        return (max(p) - min(p)) / max(p) if max(p) else 0.0

    suspeita = None
    for rotulo, amostra in (("clara", p90), ("escura", p10)):
        if satura(amostra) > 0.45:
            perto = sum(1 for _, p in fundo if dist_cor(p, amostra) < 60) / m
            if perto < 0.25:
                suspeita = (rotulo, amostra, perto)

    return {
        "nome": nome, "tinta": tinta, "fundo": (p10, p50, p90),
        "contrastes": cs, "pior": pior, "desvio_fundo": dev, "suspeita": suspeita,
    }


def dist_cor(a, b):
    return sum((a[i] - b[i]) ** 2 for i in range(3)) ** 0.5


# ---------------------------------------------------------------- relatório

def relatorio(caminho, caixas, recorte=None):
    img = Image.open(caminho)
    W, H = img.size
    print(f"\n{'=' * 78}\n{caminho}   {W}×{H}\n{'=' * 78}")

    base = img
    ox = oy = 0
    if recorte:
        ox, oy = recorte[0], recorte[1]
        base = img.crop(recorte)
        W, H = base.size
        print(f"análise de composição restrita a x {recorte[0]}–{recorte[2]}  y {recorte[1]}–{recorte[3]}")

    cel = mapa_energia(base)
    rows, cols = len(cel), len(cel[0])

    print("\nMAPA DE ENERGIA VISUAL  (0 = chapado/livre   9 = detalhe/assunto)")
    emax = max(c["energia"] for l in cel for c in l) or 1
    for r in range(rows):
        faixa = "   "
        for c in range(cols):
            faixa += f"{min(9, int(cel[r][c]['energia'] / emax * 10)):>2}"
        y0 = oy + r * H // rows
        print(f"{faixa}      y {y0:>4}–{oy + (r + 1) * H // rows:<4}")

    cx, cy = centro_de_massa(cel)
    lado = "ESQUERDA" if cx < 0.45 else ("DIREITA" if cx > 0.55 else "CENTRO")
    alt = "TOPO" if cy < 0.45 else ("BASE" if cy > 0.55 else "MEIO")
    print(f"\nCENTRO DE MASSA DO ASSUNTO   x {cx * 100:.0f} %  y {cy * 100:.0f} %   →  {lado} / {alt}")
    print(f"                             em pixels: x≈{ox + int(cx * W)}  y≈{oy + int(cy * H)}")

    if lado == "DIREITA":
        oposto = "ESQUERDA — o bloco de texto vai para x baixo"
    elif lado == "ESQUERDA":
        oposto = "DIREITA — o bloco de texto vai para x alto"
    else:
        oposto = "TOPO ou BASE — assunto centralizado pede texto acima ou abaixo, não ao lado"
    print(f"CONTRAPESO                   texto no lado {oposto}")

    print("\nZONAS LIVRES  (as 6 melhores — grandes e calmas primeiro)")
    print(f"   {'região em px':<34}{'células':<12}{'energia':<10}{'lum':<8}")
    def sobrepoe(a, b):
        """Fração da zona menor coberta pela maior."""
        dc = min(a["c1"], b["c1"]) - max(a["c0"], b["c0"])
        dr = min(a["r1"], b["r1"]) - max(a["r0"], b["r0"])
        if dc <= 0 or dr <= 0:
            return 0.0
        return dc * dr / min(a["area"], b["area"])

    vistas = []
    for z in zonas_livres(cel):
        if any(sobrepoe(z, v) > 0.6 for v in vistas):
            continue
        px0, px1 = ox + z["c0"] * W // cols, ox + z["c1"] * W // cols
        py0, py1 = oy + z["r0"] * H // rows, oy + z["r1"] * H // rows
        reg = f"x {px0}–{px1}  y {py0}–{py1}"
        print(f"   {reg:<34}{z['area']:<12}{z['energia']:<10.3f}{z['lum']:<8.3f}")
        vistas.append(z)
        if len(vistas) >= 6:
            break

    if caixas:
        print("\nCONTRASTE DO TEXTO — pior caso, não média")
        print("   mínimo 4,5:1 para corpo · 3:1 para texto grande (≥30 px normal, ≥24 px bold)")
        for i, (box, tinta) in enumerate(caixas, 1):
            r = contraste_faixa(img, box, f"faixa {i}", tinta)
            p10, p50, p90 = r["fundo"]
            pior = r["pior"]
            marca = "REPROVA" if pior < 4.5 else ("limite" if pior < 7 else "ok")
            print(f"\n   faixa {i}  x {box[0]}–{box[2]}  y {box[1]}–{box[3]}")
            print(f"      tinta {hexs(r['tinta'])}   fundo {hexs(p10)} → {hexs(p90)}  (mediana {hexs(p50)})")
            print(f"      escuro {r['contrastes'][0]:5.2f}:1   médio {r['contrastes'][1]:5.2f}:1   "
                  f"claro {r['contrastes'][2]:5.2f}:1")
            print(f"      PIOR CASO {pior:5.2f}:1   [{marca}]   desvio do fundo {r['desvio_fundo']:.3f}"
                  f"{'  ← fundo movimentado, scrim local obrigatório' if r['desvio_fundo'] > 0.08 else ''}")
            if r["suspeita"]:
                rot, cor, frac = r["suspeita"]
                print(f"      ⚠ a amostra {rot} {hexs(cor)} é saturada e ocupa só {frac * 100:.0f} % da caixa —")
                print(f"        provavelmente é OUTRA COR DE TEXTO, não fundo. Refaça a caixa isolando")
                print(f"        uma linha e uma cor por vez, senão este número é falso.")
    print()


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    arquivo, caixas, recorte, i, tinta = args[0], [], None, 1, None
    while i < len(args):
        if args[i] == "--tinta":
            h = args[i + 1].lstrip("#")
            tinta = tuple(int(h[j:j + 2], 16) for j in (0, 2, 4))
            i += 2
        elif args[i] == "--texto":
            caixas.append((tuple(int(v) for v in args[i + 1].split(",")), tinta))
            tinta = None
            i += 2
        elif args[i] == "--recorte":
            recorte = tuple(int(v) for v in args[i + 1].split(","))
            i += 2
        else:
            i += 1
    relatorio(arquivo, caixas, recorte)
