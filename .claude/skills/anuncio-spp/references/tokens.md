# Tokens — SPP com IA

Valores lidos diretamente dos 16 anúncios originais. Não estime, use estes.

---

## Cores de marca (fixas, nunca mudam)

| Token | Valor | Onde |
|---|---|---|
| Pill PRONTO | `LIN[#2FB4F7 → #331E79]` | gradiente do badge azul |
| Pill COM IA | `LIN[#FF9500 → #CE5601]` | gradiente do badge laranja |
| Pill base oculta | `LIN[#2FF7CF → #1E5B79]` | camada teal sob o laranja, sempre presente e coberta |
| Fundo branco do pill | `#FFFFFF` | fill base sob os gradientes |

Os dois pills sempre carregam `#FFFFFF` como fill base. O laranja tem **três** fills empilhados (branco, teal, laranja) — o teal é resíduo do arquivo original e fica coberto. Reproduza os três para fidelidade estrutural.

---

## Cores de acento (uma por peça)

| Família | Valores | Quando |
|---|---|---|
| Laranja | `#FF9500` `#FFA34C` `#FC8D3E` `#F67803` | padrão da marca; cena quente |
| Ciano | `#00EEFF` `#46D7FF` `#49C2FF` `#2FB4F7` | CTA em fundo escuro; cena fria; tema técnico |
| Verde | `#46FF75` `#46FF5B` `#06C05D` | liberação, dinheiro, "lote liberado" |
| Amarelo | `#FFDB0F` `#EDD62A` | urgência média, destaque de CTA |
| Vermelho | `LIN[#FF0F0F → #990909]` | **só** escassez real (pill "Últimos ingressos") |

`#00EEFF` é o ciano específico do texto de CTA na geração Manrope.

---

## Tintas e neutros

| Token | Valor | Uso |
|---|---|---|
| Ink | `#020A0A` | vinheta, sombra de texto, preto da marca |
| Ink alt | `#010202` `#09141A` `#000000` | fill base de frame |
| Base cinza | `#414141` | fill base sob imagem (geração Exo 2) |
| Grade navy | `#152B4A` | multiply de correção de cor; vidro dos cards |
| Vidro escuro | `#030407@0.40` | painel de data |
| Chip | `#232727` | chip de data com ícone |
| Texto suave | `#CCCECE` | texto dentro de chip |
| Texto claro | `#535656` | CTA em fundo claro |
| Texto 80% | `#FFFFFF@0.80` | corpo do CTA e texto secundário |
| Barra vidro | `#FFFFFF@0.08` + `#000000@0.20` | fill da barra inferior |
| Borda vidro | `#FFFFFF@0.20` | stroke da barra inferior |
| Borda de chip | `LIN[#FFFFFF → #000000@0.16]` peso 2 | stroke de ícone e barra de progresso |

---

## Tipografia — três gerações

O arquivo tem três safras. **Para peças novas use a geração Exo 2 + Inter**, que é a mais recente e a mais consistente.

### Geração A — Anton (headlines de máximo impacto)

| Papel | Fonte | Tamanho | Entrelinha | Caixa |
|---|---|---|---|---|
| Headline | `Anton SC Regular` / `Anton Regular` | 88 – 140 | 104 – 148 px | UPPER |
| Corpo | `Manrope Regular` / `Medium` | 40 – 45 | 53.6 – 60 px | original |
| Ênfase | `Manrope Bold` | 45 – 55 | — | original |
| CTA | `Manrope SemiBold` | 30 | 50 px | original |
| Data | `Manrope SemiBold` | 31 – 35 | — | original |

Anton é extremamente condensada. Serve quando o headline tem 2–4 palavras e precisa ocupar a largura toda.

### Geração B — Exo / Exo 2 (padrão atual)

| Papel | Fonte | Tamanho | Entrelinha | Tracking |
|---|---|---|---|---|
| Headline | `Exo 2 Bold` / `Exo Bold` | 56 – 127 | 64 – 68 px, ou 105 – 125 % | −2 % a −3 % |
| Corpo | `Exo Medium` | 42 | 130 % | −3 % |
| Ênfase no corpo | `Exo Bold` | 42 | — | −3 % |
| Apoio | `Inter Medium` / `Semi Bold` | 36 – 40 | 48 – 56 px | 0 |
| CTA | `Inter Medium/Regular` + `Inter Extra Bold` | 30 – 34 | auto | 0, **UPPER** |

O tracking negativo de −3 % é assinatura da marca no Exo. Sem ele a headline parece solta.

No CTA, só `"Saiba Mais"` recebe `Extra Bold`; o resto é `Medium`/`Regular` a 80 % de opacidade.

### Geração C — Albert Sans (peças de campanha isoladas)

| Papel | Fonte | Tamanho | Entrelinha |
|---|---|---|---|
| Headline | `Albert Sans Bold` | 72 | 83 px |
| Corpo | `Albert Sans Bold` | 41 | 52 px |
| Ênfase | `Albert Sans Black` | 49 | 52 px |
| CTA | `Albert Sans Bold` | 31 | 41 px |

### Ícones

`Font Awesome 6 Pro Solid` a 32 px, cor `#FF7F56`, para `calendar` e `Clock` nos chips de data.

---

## Escala de tamanhos de headline

Escolha pelo número de palavras, não pelo gosto:

| Palavras | Tamanho | Fonte |
|---|---|---|
| 2 – 3 | 127 – 140 | Anton ou Exo Bold |
| 4 – 6 | 88 – 90 | Anton / Exo 2 Bold |
| 7 – 10 | 64 – 72 | Exo 2 Bold |
| 11+ | 56 | Exo 2 Bold |

Headline nunca passa de 3 linhas.
