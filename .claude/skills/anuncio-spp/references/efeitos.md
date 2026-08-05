# Efeitos — onde mora o acabamento

Dez técnicas. É a diferença entre "texto colado numa foto" e o padrão da marca.

---

## 1. Vinheta no fill do frame — **descontinuada**

> **Não use.** Decisão do usuário em 2026-08-03: a vinheta radial escurece a cena inteira e a imagem precisa continuar legível. Ela some com o cenário que faz a peça ser reconhecida pelo nicho, que é justamente o que atravessa a cegueira de banner.
>
> **No lugar dela:** resolva o contraste do texto só na faixa onde o texto está, com o scrim do item 9, e deixe o resto da imagem intacto. Se o topo também precisar de contraste para o lockup, inverta o lockup para tinta escura com halo branco (item 3) em vez de escurecer a imagem.
>
> A documentação abaixo fica como registro do que existe nos 16 originais, não como receita para peça nova.

A técnica mais usada nos originais. O escurecimento não é uma camada — está **dentro do fill do frame**:

```
fills = [
  SOLID   #414141                              ← base
  IMAGE   scaleMode CROP                       ← a cena
  GRADIENT_RADIAL [#020A0A@0.00 → #020A0A]     ← vinheta
]
```

Variantes encontradas: paradas em `0.40 → 0.80` (vinheta apertada) e `0.00 → 0.04 → 1.00` (mais suave no centro).

Faça isso **antes** de considerar qualquer scrim. Resolve contraste sem gastar camada e sem achatar a cena.

---

## 2. Brilho de acento

O efeito que dá luz ao texto colorido. Uma elipse na cor do acento, muito borrada, em blend aditivo, **atrás** do trecho de texto que leva aquela cor.

```
Ellipse  540×151
  fill  = #46FF5B@0.25          ← a cor do acento
  fx    = LAYER_BLUR 148.8
  blend = LIGHTEN               (ou SCREEN)
```

Faixas observadas: opacidade `0.25 – 0.60`, blur `86 – 150`. Elipse achatada (largura ≈ 3× a altura) acompanhando a linha de texto.

Sem isso o acento parece pintado. Com isso, parece emitir luz.

---

## 3. Sombra de legibilidade — **só quando o fundo exige**

> Corrigido em 2026-08-03. A regra antiga dizia que toda linha de texto sobre foto recebe sombra. **Está errada.** Sombra empilhada sobre fundo que já está escuro é remendo de júnior: engorda a letra, suja a contraforma e não acrescenta contraste nenhum.
>
> **Meça antes de aplicar.** Se o scrim já entrega o contraste na faixa do texto, não existe sombra. Na peça de dermatologia, o texto sem sombra alguma mediu 9,6:1 no headline, 13,6:1 no apoio e 11,0:1 no CTA. As sombras que estavam lá não faziam nada além de engrossar a tipografia.
>
> Sombra entra quando o texto **precisa** cair sobre região clara ou movimentada e não há como criar contraste de outro jeito. Aí ela usa a cor da cena, conforme o item 4.

Quando for necessária, a sombra impede o texto de "boiar".

| Contexto | Efeito |
|---|---|
| Fundo escuro, padrão | `DSH(r24 y6)` + `DSH(r12 y0)` empilhadas, ambas na **cor da cena** (item 4) |
| **Fundo claro** | **Não use halo claro.** Proibido em 2026-08-04: a auréola não existe em fotografia e deixa a peça falsa. Resolva por posição do texto ou por enquadramento |
| CTA sobre foto | `DSH(r36 y4 @0.25)` no container, na cor da cena |

Os hex fixos que estavam nesta tabela (`#020A0A`, `#F7F9FE`, `#2F2B42`) saíram: eram tons frios que só serviam às cenas frias dos originais. A cor sai da amostragem do item 4.

O halo branco em fundo claro é contraintuitivo e essencial: a sombra escura sujaria a peça.

---

## 4. Cor da cena em toda sombra e todo scrim — **padrão obrigatório**

> Deixou de ser refinamento opcional em 2026-08-03. **Nenhum escurecimento da peça usa preto neutro nem preto frio.** Sombra de texto, scrim inferior, fill escuro da barra de vidro e halo de fundo claro: todos usam a matiz dominante da cena. Preto azulado sobre cena âmbar denuncia texto colado por cima, que é exatamente o que o item 3 tenta evitar.
>
> **Receita de amostragem**, feita por medição e não a olho:
> 1. Média de RGB da região que vai receber o escurecimento (para o scrim, a faixa que ele cobre; para o halo, a região atrás do lockup).
> 2. Converta para HSV e **guarde a matiz**.
> 3. Preto quente da cena: mesma matiz, saturação × 1,35 (teto em 0,55), valor ≈ 0,055.
> 4. Halo de fundo claro: mesma matiz, saturação × 0,45 (teto em 0,10), valor ≈ 0,99.
>
> Exemplo medido na peça de dermatologia: cena em matiz 27–32°, saturação 0,22. Derivou `#0E0C0A` para sombra e scrim, e `#FCF1E3` para o halo, no lugar do antigo `#020A0A` (ciano) e `#F7F9FE` (azulado). O contraste praticamente não muda (headline 8,4:1 → 8,2:1), o que muda é o texto passar a pertencer ao ambiente.

Em vez de preto, a sombra usa uma cor **amostrada da cena**:

```
Cena submarina →  DSH(r62 y6 #003F64@1.00) + DSH(r21 y0 #003F64@1.00)
```

Duas sombras da mesma cor, uma larga e uma fechada. O texto passa a pertencer ao ambiente em vez de flutuar sobre ele. Amostre a cor dominante da região atrás do texto e use-a.

---

## 5. Brilho por camada duplicada

Para dar luz a um elemento gráfico (barra, chip, card):

1. Duplique o elemento inteiro
2. `LAYER_BLUR 106.7`
3. blend `LIGHTEN`
4. Coloque **atrás** do original, levemente maior

Funciona com barra de progresso, chips e pills. É a assinatura de "elemento aceso" do sistema.

---

## 6. Barra de vidro fosco

```
fill   = #FFFFFF@0.08 + #000000@0.20
stroke = #FFFFFF@0.20
fx     = BACKGROUND_BLUR 48
```

Branco baixíssimo por cima de preto médio, com borda branca sutil. **Não** é um cinza chapado — o cinza mata a foto atrás e denuncia amadorismo.

Card de vidro menor: `#152B4A@0.20`, `r20`, efeito `GLASS(8)`.

---

## 7. Profundidade de campo por duplicação

Foco sem lente. Duas cópias da mesma imagem:

```
Cópia 1 (atrás)  fill = IMG/CROP + #000000@0.20 + LIN[#000000 → #000000@0.00]
                 fx   = LAYER_BLUR 5
Cópia 2 (frente) fill = IMG/CROP recortada no sujeito
```

A de baixo borrada e escurecida, a de cima nítida. Separa o sujeito do cenário mantendo a mesma foto.

---

## 8. Correção de cor da cena

Quando fotos de origens diferentes precisam conviver:

```
Rectangle cobrindo o quadro
  blend = MULTIPLY
  fill  = LIN[#152B4A@0.00 → #152B4A]
```

O multiply em azul-noite unifica tudo numa temperatura só. Aplique sobre a cena, abaixo do texto.

---

## 9. Scrim inferior

Quando a vinheta do frame não basta:

**Duas paradas. Só isso.** Corrigido em 2026-08-03: a receita de quatro paradas que estava aqui produzia sombra dura, com transição percebida. O degradê tem exatamente dois pontos, a mesma cor nas duas pontas.

```
Rectangle largura total, ancorado na base
  fill = LIN vertical na COR DA CENA (item 4):
         posição 0 → alpha 0.00
         posição 1 → alpha 1.00
```

Comece o retângulo **abaixo do queixo do sujeito**, para que a transição não caia no rosto.

### O trabalho pesado é da imagem, não do Figma

Se você precisa de rampa complicada para o texto ler, o problema está na foto. **Peça a queda de luz no prompt**: uma chave que ilumina o assunto e cai para a sombra em direção à base, produzindo o terço inferior já quase preto, por gradiente contínuo de luz e não por corte.

Formulação que funcionou: *"a single warm key light from the upper left falls on her face and hands and then falls away very steeply downward, so that the entire lower third sinks into deep soft near black shadow with no detail; this darkness is created purely by light falloff, a smooth continuous gradient, with absolutely no hard edge, no band and no seam"*.

Medido na peça de dermatologia: com essa luz, a foto sozinha entrega **9,5:1** para texto branco em y900 e **19,7:1** no rodapé. O scrim de duas paradas só termina o serviço.

Isso substitui a gambiarra anterior de pedir "upper 55% / lower 45%", que fazia o modelo criar uma emenda horizontal para ser escondida depois.

Meça depois de aplicar: esconda o texto, exporte o fundo e confira a razão de contraste e o desvio padrão em cada faixa de texto.

---

## 10. Objeto de marca em blend aditivo

Os asteriscos e blocos 3D do Claude não entram em `NORMAL`:

```
blend = LINEAR_DODGE   (asterisco brilhando na cena escura)
blend = SCREEN         (glow de apoio ao redor)
opacidade 0.52 – 0.85, com LAYER_BLUR 9 quando estiver em segundo plano
```

O `LINEAR_DODGE` faz o objeto parecer emitir luz própria em vez de estar colado por cima. É o que integra o objeto de marca à cena.

---

## Ordem de aplicação

```
1. fill do frame (base + imagem + vinheta)
2. multiply de correção de cor
3. cópia borrada da cena  →  cópia nítida do sujeito
4. brilhos de acento (elipses aditivas)
5. objetos de marca em LINEAR_DODGE
6. scrim inferior, se ainda faltar contraste
7. texto com sombra de legibilidade
8. elementos de urgência (+ brilho por duplicação)
9. CTA
10. lockup da marca
```

Inverter essa ordem é o que produz peça "lavada": brilho aplicado depois do texto apaga o texto; scrim aplicado depois do sujeito apaga o sujeito.
