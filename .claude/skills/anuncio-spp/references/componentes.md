# Componentes reutilizáveis

Specs lidos dos originais. Reproduza os valores, não aproxime.

---

## Lockup da marca "SEU PRODUTO / PRONTO / COM IA"

No arquivo original vem **vetorizado** (glifos convertidos em curvas), por isso não há fonte para ler. Em peças novas reconstrua como texto vivo em `Exo Bold Italic`, calibrado por bounding box para casar largura e altura de caixa.

### Variante A — empilhada (padrão em fundo escuro)

```
Frame  274×93  @107,92   AL:V gap 10
  fx = DROP_SHADOW(r10.04  y2.79  #000000@0.30)
  ├ "seu produto"  272×32   glifos brancos #FFFFFF
  └ Frame 274×51  AL:H gap 0
      ├ Pill PRONTO  156×51  r4  fill = #FFFFFF + LIN[#2FB4F7 → #331E79]   pad 12
      └ Pill COM IA  109×51  r4  fill = #FFFFFF + LIN[#2FF7CF → #1E5B79]
                                        + LIN[#FF9500 → #CE5601]           pad 12
```

Escalas alternativas encontradas: `223×75` (pills 127×41 e 89×41, r3, pad 10, gap 8) e `356×120` (pills 203×66 e 142×66, r5, pad 16, gap 13). **Escale o conjunto inteiro proporcionalmente**, incluindo o raio.

### Variante B — em linha (topo centralizado)

```
Frame  643×62  @218,36   AL:H gap 10
  fx = DROP_SHADOW(r14  y4  #000000@0.30)
  ├ "seu produto"  284×34
  ├ Pill PRONTO  192×62  r5  pad 15  gap 15
  └ Pill COM IA  135×62  r5  pad 15  gap 15
```

---

## Linha de CTA

### Versão moderna (Inter, fundo escuro) — **use esta**

```
Frame  960×64  @60,956   r4   AL:H gap 18–20
  ├ icone  64×64  ── mão-clique
  │    Vector 38×37 @2,2   stroke #FFFFFF@0.12  peso 4
  │    Group  38×45 @16,17
  │    Vector 23×23 @9,9   stroke #FFFFFF@0.56  peso 4
  └ Texto  Inter 30, textCase UPPER, alinhado à esquerda
       "Clique em "        Inter Medium/Regular  #FFFFFF@0.80
       ""Saiba Mais""      Inter Extra Bold      #FFFFFF
       " e finalize sua compra."  Inter Medium/Regular  #FFFFFF@0.80
```

### Versão Manrope (geração Anton)

```
Frame 113  603×56   AL:H gap 21
  ├ icone 56×56
  └ Texto  Manrope SemiBold 30  #00EEFF  lh 50px  CENTER
```

### Versão barra de vidro (quando o rodapé precisa de bloco sólido)

```
Section  1080×140–187  @0,893–940
  fill   = #FFFFFF@0.08 + #000000@0.20
  stroke = #FFFFFF@0.20
  fx     = BACKGROUND_BLUR 48
  AL:V  pad 25/0/16/0  gap 32
  └ Frame 45  571×84  AL:H gap 48   fx = DSH(r36 y4 #000000@0.25)
      ├ Chip do ícone  119×84  r16
      │    fill   = LIN[#24A1DD → #1390CA]        (Zoom)
      │             LIN[#06C05D → #089F4E]        (WhatsApp)
      │             LIN[#331E79 → #49C2FF]        (genérico)
      │    stroke = LIN[#FFFFFF → #000000@0.16] peso 2
      │    pad 8/30/8/35
      └ Texto  404×84  Exo SemiBold 32  lh 130 %  ls −3 %  #FFFFFF
```

O chip empilha 3 gradientes; **o último visível é o que aparece**. Troque só o de cima para mudar de canal.

### Barra sólida de escassez

```
Frame 113  1079×100  @1,980   fill = #2F0000   AL:H gap 21
  ícone 56×56  +  Manrope SemiBold 30 #FFFFFF
```
Vermelho-sangue no rodapé, só em peça de "últimos ingressos".

---

## Chips de data e hora

```
Frame  667×66  r8  fill #232727   fx = DSH(r12 y20 #000000@0.48)
  AL:H gap 24  pad 10/24/10/24
  ├ Chip  ├ icon "calendar"  Font Awesome 6 Pro Solid 32  #FF7F56
  │       └ "21 e 22 de Agosto"  Manrope SemiBold 34  #CCCECE
  ├ Line  divisor vertical, stroke #100A0D@0.16 peso 2.75
  └ Chip  ├ icon "Clock"  Font Awesome 6 Pro Solid 32  #FF7F56
          └ "10h no ZOOM"  Manrope SemiBold 34  #CCCECE
```

**Variante em texto corrido** (sem chip), quando o layout já está cheio:
```
"Dias "              Manrope Regular  35–45  #FFFFFF
"21 e 22 de agosto"  Manrope Bold     35–45  #FFFFFF ou #00EEFF
" - "                Manrope Regular
"10h"                Manrope Bold
```
A data em Bold e o resto em Regular — nunca a linha inteira num peso só.

**Painel de data em vidro:**
```
Frame 643×137  r15  fill #030407@0.40  AL:V gap 10  pad 20/30/5/30
```

---

## Pill de escassez

```
Frame  529×78  r8  fill = LIN[#FF0F0F → #990909]   AL:H  pad 19/25/19/25
  Texto  "Últimos ingressos"  Manrope Bold 55  #FFFFFF  lh 80px  CENTER
```
Só com escassez verdadeira. É o único uso legítimo de vermelho no sistema.

---

## Barra de progresso do lote

```
Moldura  816×68  r16  fill #141514
  stroke = LIN[#FFFFFF → #000000@0.16] peso 2
  fx     = DSH(r32 y12 #000000@0.80) + DSH(r6 y4 #000000@0.56)
  pad 0/48/0/0
  └ Preenchimento  768×68  r16  AL:H gap 24  pad 2/24/2/24
        fill = LIN[#331E79 → #49C2FF]
             + LIN[#09944A → #06C05D@0.35 → #EDD62A@0.65 → #ED2A2A]
        stroke = LIN[#FFFFFF → #000000@0.16] peso 2
        ├ rótulo do lote  +  ícone
        └ "96%"  Exo Bold 40  #FFFFFF  lh 160 %  ls −2 %  UPPER
```

**Brilho:** duplique a barra inteira, aplique `LAYER_BLUR 106.7`, blend `LIGHTEN`, e coloque **atrás**. É o que faz a barra parecer acesa.

---

## Cards de dia (cronograma)

```
Frame  312×223  r20  fill #152B4A@0.20   fx = GLASS(8)   AL:V gap 31
  Título  "Dia 1:"  destaque
  Corpo   lista do conteúdo
```
Dois lado a lado com gap 25, dentro de um container de 731 de largura.
