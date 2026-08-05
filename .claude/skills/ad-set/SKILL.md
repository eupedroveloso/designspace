---
name: ad-set
description: Expande um criativo aprovado em um conjunto de variações por formato e canal (feed, stories, display, capa, banner). Use quando o usuário pede "adaptar para todos os formatos", "versões para Meta/Google", "kit de anúncios", ou já aprovou uma arte e precisa dela em N tamanhos.
---

# Ad-set

Objetivo: um criativo aprovado vira o conjunto completo, sem que a composição quebre em nenhum formato.

## Passos

### 0. Pergunte onde o conjunto nasce
Link do arquivo Figma, página e seção — pelo usuário, nesta sessão. Rode `/figma-destino` e registre. O arquivo do criativo aprovado **não** é resposta: o conjunto pode ir para outro lugar, e quem decide é ele.

### 1. Confirme a base
Você precisa de um criativo aprovado — creation do Magnific ou frame do Figma. Se ainda não existe, isso é trabalho de `/brief` + `visual-generator`, não de ad-set.

Liste os formatos alvo. Padrões comuns:

| Canal | Formato | Ratio |
|---|---|---|
| Feed Meta/Instagram | 1080×1080 | 1:1 |
| Stories / Reels | 1080×1920 | 9:16 |
| Feed vertical | 1080×1350 | 4:5 |
| Display / YouTube | 1920×1080 | 16:9 |
| Banner leaderboard | 728×90 | — |
| Banner retângulo | 300×250 | — |

Confirme a lista com o usuário se ele não a deu — adaptar formato errado é retrabalho puro.

### 2. Adapte a imagem, não estique
Recorte nunca é a primeira opção. Ordem de preferência:

1. **`images_expand`** — estende a cena para o novo ratio (outpainting). Preserva o sujeito e ganha respiro. É o caminho padrão para 1:1 → 9:16.
2. **`design_auto_resize`** — quando a peça tem camadas e o layout precisa se recompor por formato. Cheque com `design_auto_resize_show`.
3. **`images_crop`** — só quando há margem sobrando de verdade e o sujeito não sofre.
4. **Regerar** no novo ratio — quando a composição pede enquadramento genuinamente diferente. Passe o original como referência para manter consistência.

Banners pequenos (728×90, 300×250) quase sempre exigem recomposição, não resize. Texto que funciona em 1:1 vira ilegível ali.

### 3. Monte no Figma
Delegue ao `figma-builder` (carregue `/figma-use` antes). Um frame por formato, nomeado `<canal>-<dimensão>`, todos numa página, em auto-layout, com o texto como camada editável — não queimado no pixel.

Se houver variação de copy, monte como componente com property de texto.

### 4. Audite
Rode `brand-guardian` no conjunto. Contraste de texto sobre imagem muda de formato para formato — o que passa em 16:9 costuma falhar em 9:16.

## Saída

Link da página Figma + lista dos formatos entregues + qualquer formato que exigiu decisão de composição diferente da base. Registre em `outputs/`.
