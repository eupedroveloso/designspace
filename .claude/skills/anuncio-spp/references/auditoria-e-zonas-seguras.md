# Auditoria — zonas seguras, limites e receitas de medição

Referência do agente `analisador-criativo`. Todos os números são limites, não sugestões.

---

## Zonas seguras por formato

### Feed 1080×1080 e 1080×1350

| Limite | Valor |
|---|---|
| Margem mínima de qualquer texto | **60 px** |
| Margem confortável | 72 – 88 px |
| Elemento crítico (CTA, preço, data) | nunca a menos de **72 px** da borda |

Elemento decorativo pode sangrar. Texto e logo, nunca.

### Stories 1080×1920 — **não negociável**

A interface do app cobre o topo e a base. Tudo que for texto, logo, CTA ou dado da oferta precisa caber na zona central.

| Zona | Reserva | Motivo |
|---|---|---|
| **Topo** | **250 px** | avatar, nome do perfil, barra de progresso |
| **Base** | **250 px** | caixa de resposta, "deslize para cima" |
| **Laterais** | **64 px** | recorte em telas estreitas |

**Zona segura Stories: `x 64 → 1016`, `y 250 → 1670`.**
Área útil real: 952 × 1420.

### Reels e TikTok 1080×1920

Mais restritivo que Stories — a legenda e os botões de ação comem mais espaço.

| Zona | Reserva |
|---|---|
| **Topo** | 150 px |
| **Base** | **500 px** (legenda + CTA do app) |
| **Direita** | **200 px** (curtir, comentar, compartilhar, áudio) |
| **Esquerda** | 60 px |

**Zona segura Reels: `x 60 → 880`, `y 150 → 1420`.**

Ao adaptar um feed para Reels, o headline quase sempre precisa subir e encolher. Não empurre o conteúdo para baixo.

---

## Piso de legibilidade

A peça renderiza no celular a ~**37 %** do tamanho desenhado (1080 px → ~400 px).

| Elemento | Mínimo em 1080 | Resultado no celular |
|---|---|---|
| Headline | 56 | 21 px |
| Apoio / corpo / Decorado | **36** | 13 px |
| Itens de lista | **36** | 13 px |
| CTA | **38** | 14 px |
| Chapéu / pill / data | **36** | 13 px |
| Letra miúda legal | 28 | 10 px |

**Regra de corte: `fontSize × 0,37 < 13` reprova.**

> Corrigido em 2026-08-05 para bater com `legibilidade-e-densidade.md`. Os pisos antigos (32 para corpo, 30 para lista, 26 para chapéu) tinham sido reprovados na prática em 2026-08-03, mas continuaram valendo aqui — o auditor aprovava exatamente o que a skill proibia. Caixa alta e tracking aberto **não** compram exceção.

Contraste mínimo do texto contra o que está atrás, medido no **pior caso** (ver Receitas abaixo): **4,5:1** para corpo, **3:1** para texto grande, **7:1** sobre fundo com desvio > 0,08.

"Texto grande" segue a WCAG: **≥ 30 px em peso normal** ou **≥ 24 px em negrito/ExtraBold**. Pill de 28 px em ExtraBold conta como texto grande e responde ao limite de 3:1, não ao de 4,5:1.

---

## Volume de texto

Texto demais no celular vira mancha cinza. Texto de menos não vende.

| Formato | Total de caracteres | Blocos de texto |
|---|---|---|
| Feed 1080×1080 | **180 – 420** | 4 – 7 |
| Feed 1080×1350 | 220 – 500 | 5 – 8 |
| Stories | **120 – 300** | 3 – 5 |
| Reels (capa) | 60 – 180 | 2 – 4 |

"Bloco de texto" = nó de texto com função própria (chapéu, headline, apoio, item, CTA, data, escassez).

Abaixo do piso a peça parece vazia; acima do teto, ninguém lê. Fora da faixa é **ajuste**, não bloqueio — salvo se acompanhado de fonte abaixo do mínimo.

---

## Densidade

Peça de tráfego precisa de três planos ocupados: **fundo**, **meio**, **frente**.

Sinais de que faltou densidade — dois ou mais reprovam:
- Mais de 25 % da área é fundo chapado sem nada acontecendo
- Menos de 4 blocos de texto
- Nenhum elemento com transparência
- Nenhuma sombra, brilho ou textura
- Plano do meio vazio (só fundo + texto)

Clean/minimalista **só** quando o usuário pediu explicitamente. Se pediu, essa seção inteira não se aplica.

---

## Receitas de medição

Ambiente: venv com Pillow no scratchpad (`python3 -m venv venv && ./venv/bin/pip install Pillow`).

**Inventário tipográfico** — via `use_figma`, colher de cada TEXT: `characters`, `fontSize` (e por segmento), `x/y`, `absoluteRenderBounds`. Reprovar tudo abaixo do piso.

**Margens** — para cada nó de texto, distância do `absoluteRenderBounds` às quatro bordas do frame. Menor valor é a margem efetiva.

**Zona segura de Stories** — testar `rb.x ≥ 64`, `rb.x + rb.width ≤ 1016`, `rb.y ≥ 250`, `rb.y + rb.height ≤ 1670`. Qualquer violação **bloqueia**.

**Contraste** — use `scripts/analise-composicao.py`, uma caixa por linha e por cor:

```bash
./venv/bin/python .claude/skills/anuncio-spp/scripts/analise-composicao.py peca.png \
  --tinta B23A0F --texto 128,102,596,126
```

> **Método corrigido em 2026-08-05.** A receita anterior mandava comparar com a **luminância média** da região atrás do texto. Sobre fundo homogêneo funciona; sobre bokeh, mente — a média passa e o ponto pior reprova, e é o ponto pior que decide se a palavra some. A peça `2662-1058` passou por esse buraco: chapéu laranja `#B23A0F` sobre bokeh âmbar, média 2,63:1 e **pior caso 1,43:1**, ilegível no feed.
>
> **Amostre o fundo em três níveis e valha o menor:**
>
> ```python
> fundo = [p for p in pixels_da_caixa if dist_cor(p, tinta) > 90]
> fundo.sort(key=lum)
> p10, p50, p90 = [fundo[int(len(fundo) * q)] for q in (.10, .50, .90)]
> contraste = min(ratio(tinta, p) for p in (p10, p50, p90))
> ```
>
> Meça também o **desvio da luminância do fundo**. Acima de 0,08 o fundo é movimentado e o piso sobe para **7:1** — margem para o ponto que a amostragem não pegou.

```python
def lum(p):
    def f(c):
        c = c / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(p[0]) + 0.7152 * f(p[1]) + 0.0722 * f(p[2])

def ratio(a, b):
    l1, l2 = sorted([lum(a), lum(b)], reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)
```

**Composição** — o mesmo script, sem `--texto`, rodado na **imagem antes do texto**. Reprova quando o bloco de texto não está no lado do contrapeso, ou quando sobra zona livre de ≥ 6 células fora de uso. Detalhe em `design-editorial.md`.

**Vazio** — dividir a peça em grade 12×12, marcar célula como vazia quando o desvio-padrão dos pixels for < 6. Percentual de células vazias contíguas é o indicador.

**Simulação de celular** — reduzir para 400 px e ampliar de volta com `NEAREST`. O que não se lê nessa imagem não se lê no feed.
