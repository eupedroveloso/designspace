# Legibilidade e densidade

Duas regras que valem para **todo** criativo de feed, em qualquer nicho. Não são preferência estética — são as duas causas mais comuns de peça reprovada.

---

## 1. Piso de tamanho de texto

Um post 1080×1080 renderiza no celular a ~400px de largura. Isso é **37% do tamanho desenhado**. Texto de 19px vira 7px na tela.

| Elemento | Mínimo | Confortável |
|---|---|---|
| Headline | 56 | 90 – 180 |
| Apoio / corpo / Decorado | **36** | 38 – 46 |
| Itens de lista | **36** | 38 – 42 |
| CTA | **38** | 38 – 44 |
| Chapéu / pill / data | **36** | 38 – 42 |

**Nada abaixo de 36px, em nenhuma hipótese.** Corrigido em 2026-08-03: os pisos antigos (26 para chapéu, 30 para lista, 32 para corpo) foram reprovados na prática. A 26px o chapéu vira **9,6px** no celular e a data fica ilegível; a 32px o apoio vira 11,8px e ainda cansa. Caixa alta e tracking aberto **não** compram exceção.

**Teste antes de fechar:** multiplique cada corpo de texto por 0,37. Abaixo de **13px** no celular, aumente.

**Corolário duro:** se o texto não cabe, o problema é o espaço, não o texto. Corte palavras, corte uma linha inteira, ou **refaça a foto reservando mais área livre**. Nunca resolva diminuindo a fonte — foi assim que a peça de dermatologia foi reprovada duas vezes.

Corolário: se o texto não cabe no espaço, **o problema é o espaço, não o texto**. Reduza a quantidade de palavras ou redesenhe o bloco. Nunca resolva diminuindo a fonte.

---

## 2. Densidade é o padrão

Peça de tráfego compete no feed. Espaço vazio não lê como sofisticação, lê como peça inacabada.

**Só faça clean ou minimalista quando o usuário pedir explicitamente.** No resto, a peça deve ter camadas, textura, elementos complementares e blocos de apoio.

### Recursos para densidade sem sujeira

| Recurso | Como |
|---|---|
| **Textura de grão/papel** | imagem de textura por cima de tudo, `OVERLAY` ou `MULTIPLY` a 6–14 % |
| **Campo de cor radial** | elipse com gradiente radial na cor de apoio, atrás do sujeito |
| **Anéis concêntricos** | elipses com stroke fino, sem fill, opacidade 8–18 % |
| **Grade pontilhada** | matriz de círculos 6px, opacidade 10–20 % |
| **Card de vidro** | fill da cor base a 30–50 % + `BACKGROUND_BLUR 20–48` + borda clara a 20 % |
| **Elementos do nicho flutuando** | 3–5 objetos recortados, com sombra de contato e escalas diferentes |
| **Selo adesivo** | círculo girado 8–14° com texto em caixa alta |
| **Faixa de reforço** | barra em cor de acento com uma frase curta |
| **Sombra colorida** | `DROP_SHADOW` na cor do acento em vez de preto |

### Como distribuir

Trabalhe em **três planos**:

- **Fundo** — base, campo de cor, anéis/grade, textura. Nunca fica vazio.
- **Meio** — sujeito, elementos flutuantes, cards de vidro.
- **Frente** — texto, selos, CTA.

Se um dos três planos está vazio, a peça vai parecer simples. O erro clássico é ter só fundo chapado + texto: dois planos, nenhum meio.

### Sinais de que faltou densidade

- Mais de 25 % da área é fundo chapado sem nada acontecendo
- O olho percorre a peça inteira em menos de um segundo
- Só existe um bloco de texto além do headline
- Nenhum elemento tem transparência
- Nenhuma sombra ou brilho colorido
