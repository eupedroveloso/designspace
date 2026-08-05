# Arquétipo — Retrato de autoridade com o produto na tela

Validado em 2026-08-03 na peça de dermatologia, depois de doze rodadas de reprovação e correção. **É um tipo de anúncio entre outros, não o formato da marca.**

## Quando usar

Topo de funil, nicho profissional definido (dermatologia, advocacia, nutrição, estética, educação), divulgando evento ou produto que ensina a pessoa a transformar conhecimento em produto digital.

Funciona porque resolve a cegueira de banner pelo reconhecimento: o profissional se vê antes de ler qualquer palavra. Não use quando o público é amplo e indefinido, nem quando a ideia da campanha pede humor, comparação ou tipografia como protagonista.

---

## O que é fixo — o sistema, não o desenho

Isto vale para **qualquer** peça, não só para este arquétipo. Não é aqui que se inventa.

**Canvas e margens.** 1080×1350. Nenhum elemento encosta na borda. Bloco de texto com 120 de margem lateral. CTA com 60 de margem inferior.

**Imagem.** Sangra o frame inteiro, sempre. Enquadramento se ajusta por `imageTransform` em modo CROP, nunca recortando a foto num retângulo menor com campo chapado embaixo. A escuridão do rodapé é fotográfica e vem da **queda de luz**, pedida no prompt. A cena precisa continuar visível no rodapé.

**Nunca peça uma superfície na cena só para segurar texto.** Mesa, bancada e tampo em primeiro plano viraram vício e produziram peças com a mesma composição. A cena responde à copy; o texto encontra lugar nela depois. Ver a regra 4 de `regras-de-composicao.md`.

**Escurecimento.** Um único degradê, **duas paradas**, mesma cor, alpha 0 → 1, na matiz dominante da cena (diferença máxima de 15° de matiz). Nunca preto neutro ou azulado, nunca vinheta radial, nunca escurecimento global.

**Sombra de texto.** Não existe por padrão. Só entra se o fundo exigir, e aí na cor da cena.

**Pisos de tamanho.** Nada abaixo de 36 px, que é 13,3 px no celular. Exceção única: objeto de contexto na cena, cujo texto é textura e não mensagem.

**Contraste.** 4,5:1 para corpo, 3:1 para texto grande. Medido, com o cuidado de separar trechos de cores diferentes na mesma linha.

**Respiro.** 22 px entre grupos de texto, o mesmo valor repetido. 25 px entre a base do sujeito e o topo do texto. 20 px entre o fim do texto e o CTA. Padding interno de container ≥ 28 px.

**Camadas isoladas.** Um papel por camada: `HEAD`, `SUBHEAD-QUADRO`, `SUBHEAD-DECORADO`, `DATA`, `CTA-TEXTO`. Nunca dois papéis no mesmo nó.

**Texto.** Só Head, SubHead, Data e CTA são vetor editável. Texto que pertence a um objeto da cena vem renderizado na imagem, em PT-BR, ou não existe.

**Copy.** Quadro **e** Decorado, os dois. Vícios do Light Copy conferidos. CTA com verbo casando com o destino.

**Auditoria.** `revisor-final` antes de entregar. Sem exceção.

---

## Parâmetros de referência — ponto de partida, não gabarito

Medidos na peça aprovada. Servem para calibrar a próxima, não para copiar coordenada.

```
Tipografia   Albert Sans

Headline     100 px ExtraBold, duas linhas, entrelinha 0,89 do corpo
             palavra-chave na cor de acento, mesmo corpo e mesmo peso
SubHead      38 px SemiBold, medida estreita (≈600 de mancha), até 2 linhas
Decorado     38 px Bold, palavra-chave no acento
Data         33–38 px Bold, caixa alta, tracking aberto, na área livre da imagem
CTA          38 px caixa baixa, alinhado à esquerda ao lado do chip,
             só "Saiba Mais" em peso alto, aspas literais
             faixa 788×136, centralizada, padding 20/24, cantos 20

Objetos      dispositivo digital na mão, com a tela renderizada na imagem
             cascata de 3 notificações de venda, 257×44, gap 51,
             opacidade decrescente, na área livre ao lado do corpo
```

---

## Os dois desenhos de headline

Escolha pelo **tamanho da palavra-chave**, não pelo gosto.

- **Palavra-chave com menos de 6 caracteres → headline homogênea.** Duas linhas no mesmo corpo, hierarquia por cor. Palavra curta nunca alcança a mancha da linha de cima, e insistir em salto de escala desequilibra a peça. Foi o que aconteceu com "teto" por três rodadas.
- **Palavra-chave longa → salto de escala.** Linha fina em cima, palavra-herói grande embaixo, com mancha igual ou maior que a linha acima.

---

## O que TEM que mudar a cada peça

O `CLAUDE.md` proíbe reaproveitar layout, estrutura ou sequência de blocos. **Este arquivo não é exceção.** Repetir a peça de dermatologia trocando a foto e a copy é exatamente o defeito que a regra de originalidade descreve.

**Antes dos sete eixos, as seis alavancas visuais.** O `CLAUDE.md` tem a regra dura de distinção entre anúncios, exigida pelo Meta Ads Andromeda: paleta e temperatura, chave de luz, ângulo de câmera, família tipográfica, tratamento do texto e direção de arte. **Pelo menos quatro mudam de uma peça para a outra.** Mudar só nicho, copy e objeto produz peças irmãs, e foi o erro cometido entre a peça de dermatologia e a primeira versão da de professores.

O sistema aqui descrito é o **tratamento escuro**: scrim, texto branco, Albert Sans, retrato em altura dos olhos. Ele é uma das opções, não a única. O `anatomia.md` documenta o arquétipo 5, de fundo claro, com tinta escura e halo branco, e o `tokens.md` documenta três gerações tipográficas. Use isso para alternar.

Sete eixos que precisam ser reabertos toda vez:

1. **Nicho.** Pesquise antes. A paleta praticada muda tudo: dermatologia é clara e clínica, e foi isso que tirou a peça do escuro genérico. Advocacia, nutrição e educação têm outra estética.
2. **Categoria do DNA.** Esta peça usou reconhecimento direto (pessoa e cenário do nicho). O board tem doze abordagens. Humor por personificação, comparação em duas metades, tipografia como protagonista e UGC amador servem à mesma marca e produzem peças que não se parecem.
3. **Objeto do produto digital.** Tablet aqui. Podia ser celular com o checkout, notebook com a página de vendas, tela de aula. O objeto responde "o que exatamente vira produto no caso desta pessoa", e isso muda por profissão.
4. **Composição.** Sujeito centralizado e texto embaixo aqui. Sujeito lateral com coluna de texto ao lado, texto invadindo a imagem, enquadramento fechado no rosto: tudo cabe no mesmo sistema.
5. **Onde mora a informação de serviço.** Data no topo aqui, porque a foto tinha faixa morta lá. Na próxima a faixa morta pode ser outra, ou não existir, e a data vai para um selo ou para o CTA.
6. **Desenho da headline.** Depende do tamanho da palavra-chave da copy, e a copy muda a cada campanha.
7. **A copy inteira.** Sai de `/copy-anuncio`, com o tipo da Mandala escolhido pelo objetivo. Ângulo repetido é copy preguiçosa.

**Teste antes de fechar:** coloque a peça nova ao lado desta. Se a sequência vertical de blocos for a mesma, você fez template, não anúncio. Volte para o eixo 2 e escolha outra abordagem.

---

## Ordem de execução

1. `/briefing-produto` → produto e identidade
2. Pesquisa de nicho → paleta, estética, dor real
3. `/copy-anuncio` → copy, com Quadro e Decorado
4. `/ref-ads-dna` → categoria e DNA fotográfico, **escolhendo uma abordagem diferente da última**
5. `vocabulario-visual.md` → qual objeto digital entra na cena
6. Prompt da cena, com queda de luz e espaço reservado para o texto **antes** de gerar
7. Montagem no Figma, camadas isoladas
8. `revisor-final` → medir, corrigir, medir de novo
