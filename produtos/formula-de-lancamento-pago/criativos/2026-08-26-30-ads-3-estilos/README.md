# 2026-08-26 · Fórmula de Lançamento Pago · fase Captura

Conjunto reorganizado em 2026-08-26 para o padrão fixo do projeto: **conjunto, estilo, e dentro sempre `feed/` e `stories/`.**

## Onde cada coisa está

```
2026-08-26-30-ads-3-estilos/
├── copy-20-ads-eixo-novo.md        copy da entrega que está no ar (20 peças)
├── copy-30-anuncios.md             copy do plano de 30 peças em 3 estilos
├── copy-5-ads-teste-tom.md         teste de tom
├── copy-teste-estilo-popart.md     teste de estilo que originou o pop art
├── _registro-composicoes.tsv       estrutura e técnica peça a peça
├── 01-charge/{feed,stories}         preparado, ainda sem peça
├── 02-ugc-nativo/{feed,stories}     preparado, ainda sem peça
├── 03-hq-pulp/{feed,stories}        preparado, ainda sem peça
├── 04-popart/
│   ├── feed/                        as 20 peças de `copy-20-ads-eixo-novo.md`
│   └── stories/                     ainda não produzido
└── _trabalho/                       nada aqui entra na entrega
```

## O que mudou na reorganização

| Antes | Depois | Por quê |
|---|---|---|
| `entrega-feed/` | `04-popart/feed/` | a entrega é de um estilo só, e estilo precisa de nome |
| `01-popart/feed/` (2 testes) | `_trabalho/` | eram testes, não entrega, e o prefixo `01` colidia com `01-charge` |
| `_lote20`, `_popart`, `_template`, `_v3`, `_obsoleto-*` | `_trabalho/` | trabalho intermediário fora da raiz |
| `_baixar.sh`, `_processar.sh`, `_urls.tsv`, `_u20.tsv`, `_reg20.tsv`, `_registro-geracao.tsv` | `_trabalho/` | a raiz do conjunto guarda só copy e registro de composições |
| `criativos/2026-08-25-flp-ad01-hq...`, `...ad02-ugc...` | `_trabalho/_pilotos-2026-08-25/` | pilotos de estilo que estavam soltos na raiz de `criativos/` |

## Dois pontos em aberto, para o Pedro decidir

1. **O nome da pasta não bate mais com o conteúdo.** O conjunto se chama `30-ads-3-estilos`, mas o que está no ar são 20 peças de um estilo só, pop art, vindas de `copy-20-ads-eixo-novo.md`. As 30 peças em 3 estilos de `copy-30-anuncios.md` foram geradas e estão em `_trabalho/_obsoleto-copy-v2/_raw/`, marcadas como obsoletas. Se o plano de 30 morreu, o nome honesto é `2026-08-26-popart-20-ads`, e a renomeação arrasta as referências em `outputs/`.

2. **`_registro-composicoes.tsv` reprova as 20 peças de `04-popart/feed/`.** As 20 linhas dizem `REPROVADO estrutura repetida`, todas com a mesma `split-horizontal-papel-rasgado` e a mesma técnica `pop-art-halftone`. Ou as peças são refeitas, ou o registro está desatualizado. Do jeito que está, a entrega que ocupa a pasta de estilo é uma entrega reprovada.
