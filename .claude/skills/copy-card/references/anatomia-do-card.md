# Anatomia do card — o que vai dentro do design

Este arquivo define o entregável. Copy de card é **texto que vai ser desenhado**, não legenda. Tudo que não cabe no layout está fora do escopo.

---

## Os três blocos obrigatórios

Todo card tem exatamente estes três, sempre, em qualquer fase do funil:

### HEAD
A premissa que para o scroll. É o maior elemento tipográfico do card.

- **4 a 9 palavras.** Acima disso vira parágrafo e o design perde a hierarquia.
- Legível a 1 metro de distância, na miniatura do feed.
- **Nunca pergunta. Nunca óbvia.** Ver a regra da Head em `mandala-18-tipos.md`.
- O produto não aparece aqui. Nem o nome, nem "curso", nem "método", nem sigla.
- Sem ponto final quando tem uma frase só. Com ponto quando tem duas.

### SUBHEAD
Entrega o contexto que a Head abriu. É o bloco que faz a pessoa entender do que se trata sem precisar clicar.

- **1 a 2 linhas, 12 a 25 palavras.**
- Precisa carregar o **argumento ou o dado concreto**. Subhead vaga anula a Head boa.
- É onde entra o número, o prazo, o mecanismo ou o inimigo concreto.
- Se a Head foi Clickbait ou Reflexão, é aqui que a inversão se resolve.

**A regra que não se quebra:** Head e Subhead juntas precisam entregar o contexto completo. Alguém que só olha o card, sem ler mais nada e sem clicar, precisa entender qual é o assunto e por que aquilo importa. Card que só faz sentido depois do clique falhou.

### CTA
Chama para a ação daquele projeto.

- Formato padrão: `Clique em "Saiba mais" e [complemento]`
- O complemento diz **o que a pessoa ganha ao clicar**, calibrado pela fase do funil.
- Se o botão do projeto tem outro rótulo (`Cadastre-se`, `Fale conosco`, `Comprar`), use o rótulo real e mantenha a estrutura.
- **3 a 10 palavras** no complemento. Sem exclamação, sem emoji.

Tabela de complementos por fase em `mandala-18-tipos.md`.

---

## Blocos opcionais

Use só quando o layout pede e o conteúdo justifica. Cada bloco extra rouba peso da Head.

| Bloco | Quando usa | Limite |
|---|---|---|
| **Selo / tarja** | Dado que precisa de destaque isolado: "3 dias", "R$ 0", "40 vagas" | 1 a 4 palavras |
| **Bullets** | Meio de funil, quando o argumento é uma lista de critérios | 3 itens, até 6 palavras cada |
| **Assinatura** | Nome do especialista ou marca, quando a autoridade é o argumento | 1 linha |
| **Legal** | Obrigação legal, disclaimer, validade | letra miúda, fora da hierarquia |

Nunca mais de dois blocos opcionais no mesmo card.

---

## Formato de entrega

Sempre este, uma vez por variação:

```
VARIAÇÃO 1 — [Tipo da Mandala] — [Topo | Meio | Fundo]

HEAD:     [4 a 9 palavras]
SUBHEAD:  [1 a 2 linhas com o dado concreto]
CTA:      Clique em "Saiba mais" e [complemento]

[opcional] SELO: [1 a 4 palavras]
```

Nunca entregue texto corrido. Nunca entregue legenda de rede social. Nunca entregue headline de Meta Ads separada da Head — no DesignSpace são a mesma coisa.

---

## Estruturas de card que funcionam

Referência de layout para quem vai montar no Figma. A copy se adapta à estrutura escolhida.

**Afirmação isolada.** Só Head grande sobre fundo/imagem, Subhead pequena embaixo, CTA no rodapé. Serve Topo com premissa forte. É a estrutura mais difícil de errar e a que mais depende da qualidade da Head.

**Antes / depois.** Duas colunas ou duas metades. Head no topo conectando os dois lados. Serve Meio, com tipo Comparação ou Contraste.

**Certo / errado.** Coluna com o jeito comum e coluna com o critério certo. Head afirma a premissa, nunca pergunta. Serve Meio.

**Prova em destaque.** Número grande como elemento visual dominante, Head contextualizando, Subhead com a fonte do dado. Serve Fundo, com tipo Prova Social. Exige dado real — sem número verificável, não use esta estrutura.

**Lista de critérios.** Head no topo, 3 bullets, CTA no rodapé. Serve Meio quando o argumento é comparativo.

**Cena dominante.** A imagem ocupa tudo, texto mínimo em faixa de contraste. Serve Topo com tipo Impacto Visual ou Sensação. A Head aqui precisa ser ainda mais curta, 4 a 6 palavras.

---

## Passagem para o design

A copy é a **entrada** do trabalho visual, não o fim.

**Para o `visual-generator` (Magnific):** o background é cena, textura ou atmosfera. **Nunca peça texto ao modelo de imagem.** Todo prompt de fundo termina com `no text, no numbers, no readable characters, no logos`. Nada de calendários, relógios com números ou telas com texto visível — o modelo erra e a peça vira retrabalho.

**Para o `figma-builder`:** cada bloco vira camada de texto editável com nome real (`Head`, `Subhead`, `CTA`), amarrada aos tokens tipográficos do brand kit. Texto queimado no pixel não serve — o card vai ter variação de copy e de formato.

**Contraste.** A Head cai sobre imagem em quase todo card. Garanta AA (4.5:1 corpo, 3:1 texto grande) na região exata onde o texto assenta, não na média da imagem. Se não fecha, peça faixa, gradiente ou escurecimento no fundo — nunca reduza a Head para caber em área clara.

**Hierarquia tipográfica.** Head > Subhead > CTA, sempre nessa ordem de peso visual. Se o CTA está competindo com a Head, o card perde as duas funções.

---

## Diretrizes visuais herdadas

**Cor por intenção:** vermelho/laranja para urgência e CTA. Azul para confiança e autoridade. Verde para saúde, dinheiro e resultado. Amarelo para atenção e novidade. Preto/dourado para premium.

Isso é ponto de partida, não regra. **O brand kit em `brand/` sempre prevalece** sobre esta tabela.

**Tipografia:** Head em bold, sem serifa, grande. Corpo legível, mínimo 16pt no mobile. Máximo 2 famílias por card.

**Regra dos 3 segundos:** em 3 segundos a pessoa precisa entender para quem é o card, sentir que é relevante para ela e ficar curiosa. Se a Head e a Subhead não resolvem isso sozinhas, a copy não está pronta.
