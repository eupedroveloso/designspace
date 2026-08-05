# Anatomia — grid e arquétipos

---

## Grid canônico

```
┌─────────────────────────────── 1080 ───────────────────────────────┐
│                                                                    │
│   @107,92  ou  @218,36  ── lockup da marca                         │
│                                                                    │
│                                                                    │
│                        C E N A                                     │
│              (fundo + sujeito + objeto de marca)                   │
│                                                                    │
│                                                                    │
│  ┌── x=60 ─────────── 960 ───────────────────────────┐  y≈652     │
│  │  HEADLINE  (neutro + acento)                       │            │
│  │  linha de apoio                                    │            │
│  │  [elemento de urgência]                            │            │
│  └────────────────────────────────────────────────────┘            │
│                                                                    │
│  ┌── x=60 ─────────── 960 ────────── h=64 ───────────┐  y=956     │
│  │  [ícone 64]  CLIQUE EM "SAIBA MAIS" E …           │            │
│  └────────────────────────────────────────────────────┘            │
└────────────────────────────────────────────────────────────────────┘
```

**Constantes:** margem lateral `60`, largura de conteúdo `960`, CTA em `y=956` com altura `64`.

O bloco de texto é um auto-layout vertical com gap `24–40`. O frame inteiro costuma ser auto-layout vertical com gap `32–48`.

---

## Os 5 arquétipos

### 1. Texto ancorado no rodapé — *o padrão*

Cena ocupa o quadro inteiro, texto no terço inferior sobre vinheta. É o mais reutilizável e o que menos erra.

```
Frame 1080×1080  AL:V gap 32–40
  fill = #414141 + IMG/CROP + RAD[#020A0A@0.00 → #020A0A]
  Bloco de texto  960×~264 @60,652  AL:V gap 24–40
    Headline   Exo 2 Bold 56–72, lh 64–68px, CENTER, fx DSH(r24 y6 #020A0A@1.00)
    Apoio      Inter Medium 36  ou  Exo 2 Bold 40 no acento
  Linha CTA   960×64 @60,956  r4  AL:H gap 18–20
```
Usado em: *Lembrete*, *Ficar pra trás*, *Direcionamento*.
**Escolha este quando estiver em dúvida.**

### 2. Headline no topo — *contagem e anúncio*

Headline enorme no topo, sujeito ocupando a metade inferior. Serve quando a notícia é o número.

```
Headline @104,87   Exo Bold 127, UPPER, ls −3%, gradiente branco + acento
Lockup   @110,249  (versão 223×75)
Cena     imagem sangrando, cópia borrada atrás + nítida na frente
Barra    Section 1080×187 @0,893 — vidro fosco
```
Usado em: *Faltam 5 dias*.

### 3. Coluna lateral — *cena forte de um lado*

Sujeito ocupa metade do quadro, texto alinhado à esquerda na outra metade.

```
Headline  557×184 @473,219   Exo Bold 88, LEFT, lh 105%, ls −3%
Corpo     485×275 @485,403   Exo Medium 42, lh 130%
Urgência  816×164 @132,852   barra de progresso
Scrim     1080×334 @0,751    LIN[#000000 → #000000@0.00]
```
Usado em: *Últimas vagas do lote 1*.

### 4. Pilha central — *oferta completa*

Tudo centralizado numa coluna: headline, corpo, preço, data, CTA. É o mais denso; use quando a oferta tem muitos componentes.

```
Lockup     @107,92 (empilhado, 274×93)
Bloco      958×539 @61,510  AL:V gap 25
  Headline   Anton SC 136, UPPER, branco + acento
  Corpo      Manrope Medium 43, lh 53.6px, CENTER
  Preço      Anton SC 90, UPPER, branco + acento
  Painel     643×137 r15 #030407@0.40 — data e horário
  CTA        603×56 AL:H gap 21
```
Usado em: *1º lote liberado*, *Garanta sua vaga*.

### 6. Retrato de autoridade com o produto na tela — *nicho profissional, topo de funil*

Profissional do nicho olhando para a câmera, segurando um dispositivo com o produto digital na tela, num cenário reconhecível da profissão. A escuridão do rodapé vem da luz da própria foto, e o texto mora lá.

Validado e medido em 2026-08-03. Spec completo, com os parâmetros e os sete eixos de variação obrigatória, em `references/arquetipo-retrato-com-produto.md`. **Não reproduza a peça de dermatologia**: aquilo é uma execução do arquétipo, não o arquétipo.

### 5. Fundo claro — *pesquisa, presente, conteúdo leve*

Inverte tudo. Fundo com a textura clara, texto preto, halo branco em vez de sombra preta.

```
Frame  fill = #414141 + #FFFFFF + IMG:6cf4cb65/FILL   ← a textura clara da marca
Sujeito dentro de "Mask group": Ellipse #D9D9D9 blur 175 + imagem recortada
Headline  Exo 2 Bold 88, lh 88px, ls −2%, CENTER
          #020A0A + segundo trecho com LIN[#2FB4F7@0.25 → #331E79]
          fx = DSH(r77 y0 #F7F9FE@1.00)   ← halo BRANCO
CTA       Inter Medium/Extra Bold 30, #535656@0.80, UPPER
Decorativo  asteriscos Claude em azul, opacidade 0.52–0.85, LAYER_BLUR 9
```
Usado em: *Pesquisa*.
`6cf4cb65…` é o hash da textura clara — a mesma do card "Cadê você".

---

## Prompts-base de cena por arquétipo

Sempre em inglês, sempre terminando com a proibição de texto.

**Cena escura cinematográfica (arquétipos 1–4):**
```
Photorealistic cinematic photograph of a young man with curly dark brown hair and short
stubble wearing a teal petrol blue t-shirt, <AÇÃO QUE ENCENA O HEADLINE>. Dark moody
interior, warm rim lighting from the side, deep shadows, shallow depth of field, 85mm lens,
high-end commercial advertising photography.
no text, no numbers, no readable characters, no logos
```

**Cena clara (arquétipo 5):**
```
Photorealistic studio photograph of a young man with curly dark brown hair and short stubble
wearing a teal petrol blue t-shirt, <AÇÃO>. Clean seamless very light warm gray background,
soft even diffused lighting, crisp focus, editorial commercial photography.
no text, no numbers, no readable characters, no logos
```

**Objeto de marca (asterisco Claude na cena):**
```
A glossy orange <OBJETO> shaped like an eight-pointed asterisk star, 3D rendered, soft studio
reflections, warm orange gradient <#FF9500 → #CE5601>, floating, transparent background.
no text, no numbers, no readable characters, no logos
```

Gere a cena e o objeto **separados** e componha no Figma. Pedir os dois no mesmo prompt produz o asterisco deformado.
