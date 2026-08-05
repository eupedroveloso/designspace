---
name: anuncio-spp
description: Cria anúncios FEED 1080x1080 no sistema visual "Seu Produto Pronto com IA" (Leandro Ladeira) — grid, tipografia, camadas, efeitos e relação copy↔imagem engenheirados a partir dos 16 criativos originais. Use para qualquer criativo dessa marca, ou quando o usuário pedir "um anúncio no padrão", "mais um criativo", "adapta esse ad".
---

# Anúncio SPP com IA

Sistema reconstruído por engenharia reversa de 16 anúncios FEED do arquivo `Seu Produto Pronto` (seção "Exemplos Estudo"). Cada valor aqui foi lido do Figma, não estimado.

> **Três regras acima de todas as outras:** nenhum texto abaixo de **36px** (no celular a peça renderiza a 37 % do tamanho), **densidade visual é o padrão** — clean só quando pedido explicitamente — e **a imagem decide onde o texto vai**, o que se descobre medindo, não olhando. Leia `references/legibilidade-e-densidade.md` e `references/design-editorial.md` antes de posicionar o primeiro elemento.

**Referências** — leia conforme a etapa:
- `references/design-editorial.md` — **obrigatória**: contrapeso, eixo de alinhamento, respiro, enquadramento e contraste de pior caso. É a referência que decide **onde** o texto mora
- `references/legibilidade-e-densidade.md` — **obrigatória**: piso de tamanho e como trazer densidade
- `references/vocabulario-visual.md` — **obrigatória**: os objetos do produto digital que entram na cena, escolhidos por nicho
- `references/arquetipo-retrato-com-produto.md` — arquétipo "Retrato de autoridade com o produto na tela", validado e medido. Leia o que é fixo e, principalmente, os sete eixos que **têm** que mudar a cada peça
- `references/tokens.md` — cores, fontes, escalas tipográficas
- `references/anatomia.md` — grid, coordenadas canônicas, os 5 arquétipos de layout
- `references/componentes.md` — specs exatos dos blocos reutilizáveis
- `references/efeitos.md` — o vocabulário de efeitos, que é onde o acabamento mora

---

## O princípio do sistema

**A imagem é a metáfora literal do headline.** Não é ilustração de apoio, é a piada visual que o texto explica. Essa é a regra que gera todos os criativos:

| Headline | Cena |
|---|---|
| "1º lote liberado" | homem cortando fita vermelha de inauguração |
| "Garanta sua vaga" | poltrona de cinema vazia com cordão de veludo |
| "Últimas vagas do lote 1" | despertador gigante ao lado do rosto |
| "Pare de procrastinar" | homem com placa de protesto na avenida |
| "Você vai ficar pra trás" | homem preocupado diante do monitor |
| "Faltam 5 dias" | robô com "5 DIAS" no visor |
| "Tem muito a ganhar / muito a perder" | polvo arrastando o laptop para o mar |
| "Imersão de inteligência artificial" | pescaria, e o asterisco Claude é o peixe |

Se você não consegue descrever a cena em uma frase que já contém a promessa, o criativo não está pronto. **Cena genérica de pessoa sorrindo com laptop é o erro padrão** — só aparece quando não houve ideia.

### A cena mostra a origem, os objetos mostram o destino

O produto ensina profissional a transformar conhecimento em produto digital. A foto sozinha entrega só metade disso: a pessoa no contexto dela, que é a origem. O que falta é a prova de que aquilo vira produto.

Por isso toda peça carrega **de dois a três objetos do produto digital** no plano do meio: card de venda aprovada, protocolo ou ebook impresso, card de videoaula, checkout, celular. Eles mudam por nicho, porque respondem "o que exatamente vira produto no caso desta pessoa". Catálogo, regras de medium, sombra de contato e as proibições (nunca inventar faturamento, nunca redesenhar marca de terceiro) estão em `references/vocabulario-visual.md`.

**Para achar e tratar essa cena, carregue `/ref-ads-dna`.** Aquela skill cataloga 12 categorias de metáfora visual e o DNA fotográfico do board de referências (luz, paleta, textura, formato) — é de lá que sai a ideia da cena e a direção da imagem. Grid, tokens, tipografia e efeitos continuam sendo deste documento: o DNA manda no pixel da cena, este sistema manda no layout.

### Os três invariantes

1. **O mesmo protagonista.** Sempre o mesmo homem, camiseta petróleo/teal. É o rosto da marca.
2. **O asterisco Claude entra na cena como objeto físico.** Peixe, mascote 3D, bloco pixelado, logo em relevo. Nunca como marca d'água aplicada por cima.
3. **O headline se parte em dois.** Uma parte neutra (branco) e uma parte na cor de acento. A parte colorida carrega a informação que precisa ser lembrada — o número, o prazo, o benefício.

---

## O texto não tem lugar fixo

O grid abaixo é o **ponto de partida**, não o destino. Antes de aceitar qualquer coordenada dele, meça a imagem e deixe ela decidir:

```bash
./venv/bin/python .claude/skills/anuncio-spp/scripts/analise-composicao.py imagem.png
```

O script devolve o centro de massa do assunto, o **lado do contrapeso** e o ranking de zonas livres. Assunto à direita → texto à esquerda. Assunto na base → texto no topo. Assunto centralizado → texto acima ou abaixo, nunca ao lado.

Três peças voltaram em 2026-08-05 por ignorar isso: texto empilhado no topo com um terço da peça morto ao lado, texto sobre bokeh a 1,43:1 de contraste, e headline disputando espaço com o sujeito enquanto a região mais calma da foto ficava vazia. O método completo está em `references/design-editorial.md`.

---

## Grid canônico

Coordenadas que se repetem em quase todos os anúncios. Ponto de partida — o contrapeso pode mover o bloco de texto para uma coluna lateral:

```
Canvas ............ 1080 × 1080
Margem lateral .... 60  →  conteúdo com 960 de largura
Bloco de texto .... x=60, y≈652   (varia 467–700 conforme o peso da cena)
Linha de CTA ...... x=60, y=956, altura 64
Lockup da marca ... @107,92 (empilhado)  ou  @218,36 (em linha, centralizado)
```

O anúncio se lê de baixo para cima: **CTA fixo no rodapé → texto ancorado acima dele → cena ocupando o resto.**

Detalhe completo e os 5 arquétipos em `references/anatomia.md`.

---

## Ordem de construção

Sempre de trás para frente. Cada camada existe por um motivo funcional.

**1. Fundo com escurecimento embutido.** O fill do frame já carrega a pilha:
```
SOLID base escuro (#414141 | #010202 | #000000)
  + IMAGE (CROP ou FILL)
  + GRADIENT_RADIAL [#020A0A@0.00 → #020A0A]   ← vinheta
```
A vinheta no próprio fill do frame é o que garante contraste sem camada extra. Use-a antes de pensar em scrim.

**2. Correção de cor da cena, se precisar.** Retângulo `MULTIPLY` com `LIN[#152B4A@0.00 → #152B4A]` unifica fotos de origens diferentes num azul-noite comum.

**3. Profundidade, se a cena pedir.** Duas cópias da mesma imagem: a de baixo com `LAYER_BLUR 5` e escurecimento, a de cima nítida recortada no sujeito. É assim que se cria foco sem lente.

**4. Brilhos de acento.** Elipse na cor de acento, `LAYER_BLUR 86–150`, blend `SCREEN` ou `LIGHTEN`, posicionada **atrás do texto que vai receber aquela cor**. É o que faz o acento parecer emitir luz em vez de estar pintado.

**5. Scrim inferior, se o texto ainda não tiver contraste.** Retângulo `LIN[#000000 → #000000@0.00]` de baixo para cima.

**6. Texto.** Headline, apoio, elementos de urgência. Sempre com sombra de legibilidade — ver `references/efeitos.md`.

**7. CTA.** Último, sempre no mesmo lugar.

**8. Lockup da marca**, quando o arquétipo pedir.

---

## A copy

**Headline** — uma ideia só, partida em neutro + acento. Segue as regras de gancho do `/copy-card`: premissa não óbvia, nunca pergunta, produto fora da primeira linha. A diferença aqui é que o headline precisa **caber na cena**: se a metáfora visual não sustenta a frase, troque a frase ou troque a cena.

**Linha de apoio** — o detalhe da oferta. Datas, preço, o que a pessoa recebe. Números sempre em peso Bold dentro de um parágrafo Regular. Nunca deixe um número em peso normal; ele é o que a pessoa escaneia.

**Elemento de urgência** — opcional, e só quando for real: pill de escassez, barra de progresso do lote, contagem regressiva. Specs em `references/componentes.md`.

**CTA** — sempre a mesma estrutura: `Clique em "Saiba mais" e <verbo do próximo passo>.` As aspas são literais porque citam o botão real do Meta. O verbo muda com o destino:

| Destino | Verbo |
|---|---|
| Página de captura | `e se inscreva.` |
| Checkout | `e finalize sua compra.` |
| Venda de ingresso | `e garanta seu ingresso.` |
| Grupo Telegram | `e entre no grupo.` / `para entrar.` |
| Conteúdo | `e veja como participar.` |
| Carrossel | `Arrasta` |

O ícone do CTA muda junto: mão-clique para link, Telegram para grupo.

---

## Regras de acabamento que separam o bom do amador

- **Contraste se mede no pior caso, nunca na média.** Sobre bokeh a média passa e o ponto pior reprova — foi assim que um chapéu laranja saiu a **1,43:1** na peça `2662-1058`. Amostre o fundo em três níveis (p10, p50, p90) e valha o menor. Piso: 4,5:1 para corpo, 3:1 para texto grande, **7:1 quando o desvio do fundo passa de 0,08**. Saturação não é contraste: acento quente sobre cena quente é o caso mais perigoso.
- **Sombra de texto não é automática.** Meça primeiro: se o fundo já entrega contraste, não existe sombra. E **halo claro atrás de texto escuro está proibido** desde 2026-08-04 — deixa a peça com cara falsa. Em cena clara, procure a região naturalmente mais quieta, ou mude o enquadramento.
- **A cor do brilho vem da cena.** No criativo submarino a sombra do texto é `#003F64`, não preto. Amostre a cena e use aquela cor no glow.
- **A cor de acento do headline é a cor dominante da cena.** Laranja em cena quente, ciano em cena fria, verde quando o assunto é dinheiro liberado, vermelho só para escassez.
- **Nunca mais de um acento por peça.** Duas cores de destaque anulam as duas.
- **A barra inferior é vidro, não cinza.** `#FFFFFF@0.08 + #000000@0.20`, borda `#FFFFFF@0.20`, `BACKGROUND_BLUR 48`.
- **Todo texto é camada de texto editável.** O lockup da marca é a única exceção legítima (vem vetorizado no original).

---

## Fluxo

1. Rode `/figma-status`. Bridge quebrada é a causa nº 1 de trabalho perdido.
2. Leia o brief em `briefs/` e o brand kit. Defina fase do funil — ela escolhe o arquétipo.
3. Escreva a copy com `/copy-card`, mas no formato deste sistema (headline partido + apoio + CTA).
4. Descreva a cena como metáfora literal do headline. Gere no Magnific — `references/anatomia.md` traz os prompts-base por arquétipo.
5. **Meça a imagem gerada** com `scripts/analise-composicao.py`. Anote o contrapeso e a zona livre escolhida. Se o assunto invade a zona, reenquadre por `imageTransform` antes de montar — não empurre o texto para o que sobrou.
6. Monte no Figma com o `figma-master`, na ordem de construção acima, com o bloco de texto na zona que você escolheu no passo 5.
7. **Meça o contraste do pior caso** em cada linha, uma caixa por cor. Reprovou, volte ao passo 5 — não escureça a foto inteira.
8. Confira por screenshot contra um anúncio original da mesma família.
9. Audite com `revisor-final` e `brand-guardian`.

Ao entregar, diga qual arquétipo usou e por quê aquela cena sustenta aquele headline.
