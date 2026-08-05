---
name: ad-set
description: Expande um criativo aprovado em um conjunto de variações por formato e canal (feed, stories, display, capa, banner). Use quando o usuário pede "adaptar para todos os formatos", "versões para Meta/Google", "kit de anúncios", ou já aprovou uma arte e precisa dela em N tamanhos. Use TAMBÉM sem o usuário pedir, logo depois de todo criativo de feed aprovado, para derivar o Story 9:16 — essa derivação é obrigatória.
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
| **Feed (base do projeto)** | **1080×1350** | **4:5** |
| Stories / Reels | 1080×1920 | 9:16 |
| Feed quadrado | 1080×1080 | 1:1 |
| Display / YouTube | 1920×1080 | 16:9 |
| Banner leaderboard | 728×90 | — |
| Banner retângulo | 300×250 | — |

Confirme a lista com o usuário se ele não a deu — adaptar formato errado é retrabalho puro. **O Story 9:16 é a exceção: sai sempre, sem perguntar.** Ver a seção dedicada abaixo.

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

---

## Story 9:16 — derivação obrigatória

**Todo criativo de feed aprovado ganha automaticamente a versão Story**, sem o usuário pedir. Nomeie `<nome da peça> ST` e monte na mesma página do Figma.

Isto **não** conflita com a regra de originalidade do `CLAUDE.md`. Aquela regra proíbe repetir layout entre **peças diferentes** da campanha. Aqui é a mesma peça em outro formato: copy, foto, paleta, tipografia e chave de luz são idênticas de propósito. O que muda é só o arranjo, porque o canvas mudou.

### Zonas seguras, medidas em 1080×1920

A UI do Instagram come as pontas. **Texto vive exclusivamente entre y=269 e y=1536.** A imagem pode ocupar o frame inteiro, inclusive as faixas proibidas.

```
0    ──────────────  topo: avatar, nome, close        ZONA PROIBIDA
269  ──────────────
                     faixa útil: todo o texto da peça
1536 ──────────────
                     base: campo de resposta, ações   ZONA PROIBIDA
1920 ──────────────
```

Violação de margem não tem entrega. Antes de fechar, varra por script **todos** os nós TEXT visíveis e confira a coordenada absoluta:

```js
frame.findAll(n => n.type === "TEXT" && n.visible)
     .map(n => ({ nome: n.name, y: n.absoluteBoundingBox.y,
                  base: n.absoluteBoundingBox.y + n.absoluteBoundingBox.height }))
```

Qualquer `y < 269` ou `base > 1536` volta para conserto e revalidação.

### A imagem se estende, nunca estica

De 1080×1350 para 1080×1920 faltam 570 px de altura. A ordem é a mesma da seção 2, e `images_expand` é o caminho padrão: o Magnific continua a cena para cima ou para baixo, preservando o sujeito. Esticar a foto, deixar barra preta ou repetir o mesmo enquadramento com zoom são as três saídas erradas.

Se a expansão deformar o sujeito, regere no Magnific em `aspectRatio: "9:16"` passando a peça de feed como referência de imagem.

### Tipografia: o Story ganha altura, não largura

Os dois formatos têm **1080 px de largura** e renderizam a mesma ~400 px no celular. O fator de 37 % é idêntico, então **os pisos do `revisor-final` valem sem alteração**: nada abaixo de 36 px, headline nunca abaixo de 56.

Consequência prática: não existe "reduzir a fonte para caber no Story". O que existe é usar os 570 px extras para respiro e, se a medição permitir, crescer a headline em até 1,15× do corpo do feed. Corpo menor que o do feed é achado.

O portão de contraste de pior caso (p10/p50/p90) roda igual, e roda de novo depois da expansão: a área nova da imagem não tem o mesmo comportamento de luz da original, e é exatamente ali que o texto costuma cair.

### Fecho

Audite o Story com `revisor-final` como peça independente. Ele não herda a aprovação do feed.

---

## Saída

Link da página Figma + lista dos formatos entregues + qualquer formato que exigiu decisão de composição diferente da base. Registre em `outputs/`.
