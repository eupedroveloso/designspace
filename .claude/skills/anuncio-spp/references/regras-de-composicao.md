# Regras de composição — acordo firmado

Não são preferências. São condições de aceite. Peça que quebra qualquer uma delas volta.

> **Boas práticas de design editorial — contrapeso, eixo de alinhamento, escada de respiro, enquadramento e contraste de pior caso — estão em `design-editorial.md`.** Leia junto com este arquivo. Este aqui diz o que a peça não pode ter; aquele diz **onde o texto mora** e como se chega nesse lugar medindo.

---

## 0. A imagem decide onde o texto vai

Acrescentado em 2026-08-05, depois de três peças reprovadas de uma vez.

O texto **não tem posição padrão**. Nem topo, nem base, nem centralizado. A posição sai da imagem, e se descobre com `scripts/analise-composicao.py` rodado na foto **antes** de montar no Figma.

| Assunto está | Texto vai |
|---|---|
| Terço direito | esquerda |
| Terço esquerdo | direita |
| Centralizado | acima ou abaixo — nunca ao lado |
| Base | topo |

**Reprova automática:** bloco de texto fora do lado do contrapeso; ou zona livre de ≥ 6 células com energia < 0,05 sobrando sem uso enquanto o texto se espreme em outro lugar. Foi o que reprovou a `2662-1059` — 360 × 708 px de preto absoluto vazios à esquerda, com todo o texto empilhado no topo.

**E a foto se ajusta ao texto, não o contrário.** Se o assunto invade a zona escolhida, mova a foto por `imageTransform` em CROP, escale até 1,25×, ou expanda no Magnific. Empurrar o texto para a sobra é o erro que reprovou a `2662-1093`, onde a headline foi parar na faixa de maior desvio da peça (0,20) enquanto os 270 px mais calmos do topo ficaram sem função.

---

## 1. Fundo nunca é construído no Figma

**Proibido** montar fundo com formas geométricas no Figma — elipses de gradiente, anéis, arcos, grades de pontos, campos radiais. O resultado sempre fica pobre e denuncia peça montada.

O fundo vem de **imagem gerada no Magnific** ou de textura real. Se a peça precisa de atmosfera, cor ou profundidade, isso é **prompt**, não retângulo.

Vetor no Figma serve para: tipografia, ícone, CTA, régua fina. Não para cenário.

---

## 2. Proporção 40 / 40 / 20

Vale para feed e para stories, sem exceção.

| Zona | Ocupação |
|---|---|
| **Imagem** | 40 % do card |
| **Texto** | 40 % do card |
| **Respiro e margem** | 20 % do card |

Em 1080×1080 isso é ~466.000 px² para a imagem e ~466.000 px² para o bloco de texto. Em 1080×1920, ~829.000 px² para cada.

Consequência prática: **a imagem tem que ser grande.** Sujeito pequeno perdido no quadro reprova. E o texto tem que ter presença real — tipografia grande, não legenda.

---

## 3. Nada invade a área de texto

Nenhum elemento pode cruzar, encostar ou passar por trás de um bloco de texto de forma que dispute leitura — linhas, setas, cotas, formas, bordas de imagem, outro texto.

Antes de fechar: verificar o retângulo de cada texto e garantir que nada além do fundo ocupa aquele espaço.

---

## 4. Legibilidade sem concessão

Texto sobre área de transição, sobre corpo do sujeito ou sobre esvanecimento **não é aceitável**, mesmo que a razão de contraste passe no cálculo. Se o olho hesita, reprova.

Texto vai sobre região de tom homogêneo. Mas **homogêneo não quer dizer superfície lisa fabricada para receber texto**.

> **Corrigido em 2026-08-04.** A redação anterior mandava "criar a região no prompt da imagem", e o resultado foi vício: mesa, bancada e tampo em primeiro plano em quase toda peça, só para ter onde pousar a tipografia. Isso produz composição repetida e cena montada para o texto, que é o contrário do que a peça precisa.
>
> **A composição é definida pela copy.** A ideia manda na cena: enquadramento, ponto de vista, escala e o que aparece no quadro saem do que a headline diz, não da necessidade de uma faixa lisa embaixo. Uma copy de comparação pede duas coisas no quadro; uma copy de escala pede vazio; uma copy de rotina pede desordem real.
>
> **O texto encontra lugar na cena que a ideia produziu**, e não o contrário. Zonas homogêneas existem naturalmente em quase toda fotografia: sombra profunda, céu, parede fora de foco, área desfocada pela profundidade de campo, massa escura de um objeto grande. Procure onde já existe antes de inventar.
>
> Quando mesmo assim faltar contraste, o único auxílio permitido é o **degradê de duas paradas na matiz da cena**. Nunca uma superfície plana pedida no prompt só para segurar tipografia.

---

## 5. Margem é parte do desenho

Tipografia grande precisa de margem proporcional. Letra encostando na borda do bloco, no limite do frame ou em outro elemento é erro — não é "ousadia tipográfica".

Rótulo rotacionado, cota e elemento de apoio nunca ficam espremidos contra a tipografia principal.

---

## 6. Nada de blocos chapados

**Proibido** caixa com fundo ou borda para segurar informação — card de dado, box de estatística, moldura de texto, painel de destaque.

**Única exceção:** o CTA, e apenas nos três formatos abaixo. Também quando o usuário pedir explicitamente.

Destaque se resolve com **tipografia**: escala, peso, cor, caixa, posição. Não com retângulo em volta.

### 6.1 CTA — os três desenhos permitidos

**Nunca botão arredondado.** O CTA é uma **faixa horizontal ancorada na base**, com ícone à esquerda e texto à direita. A copy muda por nicho, produto e fase; o desenho é sempre um destes.

> **Margem no CTA é obrigatória.** Corrigido em 2026-08-03: a regra antiga mandava faixa de largura total sangrando até a borda, e faixa colada na borda parece corte, não desenho. A faixa é **inset**: 60 px de margem lateral, 44 a 60 px de margem inferior, cantos arredondados em 20. Nenhum elemento da peça encosta na borda do frame.
>
> **Caixa baixa, não caixa alta.** Segunda correção, da versão do usuário: `Clique em "Saiba Mais" e crie o seu produto digital com IA` em caixa baixa, com **só o "Saiba Mais" em peso alto**. Caixa alta em duas linhas longas cansa e some no feed. As aspas continuam literais, porque citam o botão real do Meta.
>
> **A faixa não precisa ser quase full-width.** Medida da versão aprovada: **788 px de largura em canvas de 1080**, centralizada (146 de margem de cada lado), altura 136, padding 20 vertical e 24 horizontal, texto alinhado à esquerda ao lado do chip. Faixa mais estreita que o bloco de texto dá hierarquia ao CTA sem ele virar tapete.

**A · Vidro fosco** — o mais refinado, funciona sobre foto
```
Faixa 1080×140 na base
  fills  = #FFFFFF@0.08 + #000000@0.20
  stroke = #FFFFFF@0.20
  fx     = BACKGROUND_BLUR 48
  AL:V pad 25/0/16/0
  └ Conteúdo 571×84  AL:H gap 48
      ├ Chip do ícone 119×84 r16, gradiente do canal
      │   Zoom LIN[#24A1DD→#1390CA] · WhatsApp LIN[#06C05D→#089F4E]
      │   stroke LIN[#FFFFFF→#000000@0.16] peso 2
      └ Texto 2 linhas, 32px, branco
```

**B · Faixa sólida escura** — quando o fundo é claro ou movimentado
```
Faixa de largura total na base, fill sólido escuro
  ├ ícone mão-clique 64×64, traço #FFFFFF@0.12 e @0.56, peso 4
  └ Texto 30–34px UPPER
      "Clique em "  Inter Regular/Medium  #FFFFFF@0.80
      "“Saiba Mais”" Inter Extra Bold      #FFFFFF
      resto          Inter Regular/Medium  #FFFFFF@0.80
```

**C · Faixa clara/discreta** — para peça de fundo claro
```
Mesma estrutura de B, sobre fundo claro
  ícone com traço #535656@0.12 e @0.56
  texto #535656, UPPER, "Saiba Mais" em Extra Bold
```

Em todos: **aspas literais** em "Saiba mais" — citam o botão real do Meta. O verbo final muda com o destino (inscrever, comprar, garantir ingresso, entrar no grupo, responder).

---

## 7. Texto é composição, não empilhamento

Bloco de texto atrás de bloco de texto é diagramação de relatório, não de anúncio.

A composição tipográfica trabalha: contraste de escala forte entre os níveis, palavras em pesos e caixas diferentes, alinhamentos que conversam entre si, texto que se integra à imagem em vez de sentar ao lado dela.

Referência de padrão: flyer publicitário. Se a peça parece um post de template, está errada.

### Sintoma de empilhamento

Headline, apoio e data com a **mesma largura, o mesmo alinhamento e tamanhos parecidos**, um debaixo do outro. Lê como relatório. Foi reprovado na peça de dermatologia em 2026-08-03.

### Duas headlines possíveis, e a escolha é pelo tamanho da palavra

Corrigido em 2026-08-03 a partir de uma versão do usuário. Existem dois desenhos de headline, e escolher errado é o que gera a briga de equilíbrio.

**A. Salto de escala** — linha fina em cima, palavra-herói enorme embaixo. Só funciona quando a palavra que carrega a ideia é **longa o suficiente para encher a linha**. Com palavra curta ela nunca alcança a mancha da linha de cima, e você acaba inflando o corpo até a composição desequilibrar.

**B. Headline homogênea com destaque por cor** — as duas linhas no **mesmo corpo**, peso alto, e a palavra-chave em cor de acento. A hierarquia vem da **cor**, não da escala.

**Regra de escolha: palavra-chave com menos de 6 caracteres → desenho B.** "teto" tem 4 letras. Tentei o desenho A com ela e passei três rodadas empurrando o corpo de 92 para 168 px sem nunca equilibrar. No desenho B a mesma palavra resolve: duas linhas de 100 px ExtraBold, mancha de 669 e 390 px, "teto" em laranja.

Parâmetros do desenho B, medidos:

```
Headline  100 px  Albert Sans ExtraBold
          entrelinha 89 px  →  0,89 do corpo, sempre menor que 1
          duas linhas, centralizado
          palavra-chave na cor de acento, mesmo corpo e mesmo peso
```

Entrelinha maior que o corpo em headline grande abre buraco entre as linhas e desmancha o bloco.

### Ritmo de respiro: 22 px entre grupos

Head → SubHead e Quadro → Decorado, os dois com **22 px**. Ritmo único e reconhecível, em vez de gaps improvisados de 4, 8 ou 12 px que fazem os blocos colarem.

### Aproveite a área livre da imagem antes de empilhar

Informação de serviço, como data e formato, **não precisa entrar na pilha de texto**. Se a foto tem uma faixa morta, ela vai para lá. Na peça de dermatologia a data subiu para o topo do frame (y=16, 33 px Bold, contraste 4,94:1) e devolveu ~60 px de altura para a copy respirar.

Antes de espremer entrelinha ou corpo, procure onde a imagem está vazia.

### Equilíbrio: meça a mancha, não confie no olho

A palavra-herói do headline precisa **dominar visualmente**, e dominar é largura, não tamanho de fonte no papel. Peça reprovada em 2026-08-03 tinha a linha fina com 511 px de mancha e o "TETO." com 367 px: a palavra que deveria mandar era a mais estreita das duas, e a composição ficou frouxa.

**Regra:** a mancha da palavra-herói é **igual ou maior** que a mancha da linha que vem acima dela. Confira medindo no export, não olhando:

```python
band = L[y0:y1]; cols = (band > 0.30).sum(axis=0)
xs = np.where(cols > 0)[0]; largura = xs.max() - xs.min()
```

Se não couber, o caminho é **diminuir a linha de cima**, não a palavra-herói. Na peça de dermatologia a linha fina caiu de 44 para 34 px e o "TETO." subiu de 92 para 168, fechando em 433 contra 467 px.

Isso costuma exigir altura que a cena não tem. Aí se sobe o enquadramento da foto pelo `imageTransform` em modo CROP, até o limite do cabelo do sujeito, em vez de espremer a tipografia.

### Leveza: margem, respiro e alinhamento

Reprovado em 2026-08-03: bloco colado na margem de 60, tudo alinhado à esquerda, linhas espremidas. Lê como caixa de texto, não como peça de designer.

- **Margem lateral de 120 no bloco de texto**, não 60. Os 60 do grid são o limite absoluto do frame; o texto respira mais para dentro.
- **Não se apegue ao alinhamento à esquerda.** Quando o sujeito está centralizado na foto, o texto centralizado equilibra e fica mais leve. Escolha o alinhamento pela composição da imagem, não por hábito.
- **Ar entre grupos**: 18 a 24 px entre blocos, e um vão de 20 px ou mais entre o fim do texto e a barra de CTA. Bloco que encosta em tudo parece apertado mesmo com o contraste correto.
- **Pesos mais leves onde der**: o Quadro em Regular, o Decorado em Medium. Bold em tudo endurece a peça.
- **Distância do sujeito**: pelo menos 25 px entre a base do objeto na cena e o topo do texto.

### Receita que resolve

1. **Quebre a headline em dois pesos de escala.** Uma linha fina e longa por cima, a palavra que carrega a ideia embaixo em corpo 2 a 3 vezes maior, na cor de acento. Salto entre o maior e o menor texto da peça de pelo menos 3×.
2. **Marque a entrada com uma régua**, não com pill nem caixa: retângulo de 60 a 70 px por 4 na cor de acento, acima da headline.
3. **Dê voz diferente ao Quadro e ao Decorado.** O Quadro em Medium a 82 % de opacidade; o Decorado logo abaixo em Bold, branco cheio, com a palavra-chave na cor de acento. São duas frases, não um parágrafo.
4. **Desloque a data.** Tique vertical de 3 px na margem e o texto recuado, para o olho ler que aquilo é outro nível de informação.
5. **Meça o resultado**, não confie no olho: contraste por bloco e simulação de celular a 400 px.

### O Decorado é obrigatório na peça

O Manual manda vender Quadro **e** Decorado, e a peça esquece o Decorado com frequência. O Quadro é a transformação técnica ("o que você repete já é um produto"); o Decorado é a consequência na vida da pessoa ("e ele vende nos dias em que você não atende"). Peça sem Decorado vende procedimento e não vende motivo.
