# Paleta — Fórmula de Lançamento Pago

Medida no DOM renderizado da LP (`getComputedStyle`), não inferida de screenshot.

## Núcleo

| Papel | Hex | Onde aparece |
|---|---|---|
| Texto / preto da marca | `#14100E` | corpo e títulos sobre claro |
| Escuro de seção | `#221B17` | blocos escuros ("Você não vai receber apenas teoria") |
| Branco | `#FFFFFF` | fundo base |
| Creme | `#FAF7F3` | fundo alternado de seção |
| Creme quente | `#FDEDE7` | cards e destaques de texto |
| Areia | `#F4EEE6` · `#E8E1D9` | bordas e divisores |

## Coral — cor de marca

Gradiente da headline e dos blocos de destaque:

```
linear-gradient(to right bottom, #FF754F 0%, #C82B00 100%)
```

| Hex | Papel |
|---|---|
| `#FF754F` | coral claro — início do gradiente |
| `#F2803C` | coral médio |
| `#E0341F` | vermelho-coral |
| `#C82B00` | tijolo — fim do gradiente |

## Verde — cor do CTA

Todo botão de conversão da página:

```
linear-gradient(128.9deg, #1CE565 4.26%, #1FAE2B 95.74%)
```

| Hex | Papel |
|---|---|
| `#1CE565` | verde claro — início |
| `#1FAE2B` | verde escuro — fim |

Texto do botão: `#FFFFFF`, caixa alta.

## Acentos

| Hex | Papel |
|---|---|
| `#F2C744` | amarelo de destaque |
| `#A8D63F` | verde-limão secundário |

## Regra de uso nos criativos

- **Coral = promessa.** Headline, palavra de virada, faixa de destaque.
- **Verde = ação.** Exclusivo do CTA. Nunca use verde em texto informativo.
- **Preto `#14100E` = leitura.** Nunca preto puro `#000000`.
- Fundo claro é creme, não branco estourado.
