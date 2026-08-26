# Tipografia — Fórmula de Lançamento Pago

Lida do DOM renderizado da LP.

| Papel | Família | Peso | Observação |
|---|---|---|---|
| **Títulos / Head** | **Archivo** | 800 (ExtraBold) | todos os `h1`, `h2`, `h3` da página |
| **Corpo / Subhead** | **Albert Sans** | 400–700 | `body` inteiro |
| Mono (raro) | Geist Mono | — | números e tags |

## Comportamento

- **Archivo ExtraBold** é a assinatura da marca: grotesca larga, muito peso, tracking apertado (`-0.02em`), caixa mista — não caixa alta.
- A headline recebe o gradiente coral `#FF754F → #C82B00` aplicado no texto.
- **Albert Sans** carrega todo o corpo, com destaques em `600/700` e fundo `#FDEDE7` atrás da palavra grifada.
- CTA em **caixa alta**, Archivo/Albert Sans bold, tracking levemente aberto.

## Substitutos aceitáveis em geração por IA

Quando o modelo de imagem não acerta a fonte exata, a ordem de preferência é:

1. Archivo Black / Archivo ExtraBold
2. Anton (só para Head muito curta)
3. Inter Black / Manrope ExtraBold

Nunca serifada, nunca script, nunca condensada estreita.

## Pisos de tamanho para anúncio (mobile)

Medidos sobre a peça final de **1080×1350**:

| Elemento | Piso | Alvo |
|---|---|---|
| Head | 76 px | 88–120 px |
| Subhead | 40 px | 46–56 px |
| CTA | 38 px | 44–52 px |
| Selo de data/preço | 32 px | 36–44 px |

Abaixo do piso o lead não lê no feed a 37 % de escala.
