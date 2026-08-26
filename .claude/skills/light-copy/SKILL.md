---
name: light-copy
description: Escreve e revisa copy no padrão Light Copy (metodologia VTSD de Leandro Ladeira). Argumentativa, lógica, conversacional e não óbvia. Carrega o Manual da Copy (15 princípios e 20 vícios proibidos), o checklist das 12 proibições absolutas, os 26 Elementos Literários (Ladeirísticos), a Mandala de Anúncios e a revisora final anti AI slop. Use SEMPRE que o pedido envolver escrever, reescrever, revisar ou avaliar qualquer texto de venda: página de vendas, anúncio para Meta Ads ou Google Ads, headline, lead, bullet, CTA, legenda, carrossel, roteiro de Reels, roteiro de VSL, e-mail, post, oferta, depoimento, bio. Também dispara quando o usuário mencionar "Light Copy", "Lightcopy", "VTSD", "Ladeira", "Ladeirísticos", "elementos literários", "mandala de anúncios", "manual da copy", "vícios proibidos", "Quadro e Decorado", "Furadeira", "Urgências Ocultas", ou pedir para "tirar cara de IA" de um texto. Se o usuário só quer polir um texto pronto, use a parte de revisão. Se quer criar do zero, use o formato correspondente.
---

# Light Copy

Padrão de copy do VTSD. A regra que governa tudo está no Manual: **a melhor copy não parece copy, parece alguém inteligente te explicando uma coisa que você nunca tinha entendido direito.**

Você nunca vende no início. Você informa, avisa ou ensina. O produto não existe nos primeiros parágrafos. Só existe o leitor e a realidade dele.

Quando a copy ensina, a pessoa confia. Quando promete, ela desconfia.

---

## Passo 0. Contexto do produto (obrigatório, sempre)

Nenhuma copy sai sem contexto. Antes de escrever qualquer linha:

1. **Neste projeto (DesignSpace) o contexto do produto vive em `produtos/<slug>/`.** Leia `produtos/<slug>/briefing.md` e a pasta `identidade/`. Se o produto ainda não existir, pare e peça `/briefing-produto`. Não procure `meus-produtos/`, que é a convenção do projeto de origem deste pacote.
2. **Se existir uma skill de anúncio para esse produto, ela manda no tom.** Para o Fórmula de Lançamento Pago, leia `.claude/skills/anuncio-flp/SKILL.md`. A skill do produto tem precedência sobre qualquer suposição de tom.
3. Se faltar alguma peça do quebra-cabeça abaixo depois de ler o briefing, faça a entrevista curta. **Uma pergunta por vez**, nunca todas de uma vez. Se o usuário já respondeu algo na conversa, não repita a pergunta.

Entrevista mínima:

1. Qual o produto e para quem ele é?
2. Qual o **Quadro**: o resultado técnico e concreto que a pessoa alcança?
3. Qual o **Decorado**: o que muda na vida dela depois desse resultado? Fila de espera, faturamento, reconhecimento, tempo livre.
4. Qual a **Furadeira**: como o resultado acontece na prática? O mecanismo, o método, quantos passos.
5. Qual o **inimigo**: o conselho furado ou a crença errada que explica por que ela ainda não conseguiu?
6. Que prova você tem? Números, prazos, depoimentos com resultado concreto.
7. Qual o preço e o que está incluso?

Se o usuário não souber responder o Quadro ou a Furadeira, pare e resolva isso primeiro. Copy sem tese vira lero-lero.

---

## Passo 1. Escolha o formato

| O usuário quer | Leia |
|---|---|
| Página de vendas, captura ou obrigado | [references/formatos/pagina-de-vendas.md](references/formatos/pagina-de-vendas.md) + [references/template-pagina-vendas.md](references/template-pagina-vendas.md) |
| Anúncio para Meta Ads ou Google Ads | [references/formatos/anuncio.md](references/formatos/anuncio.md) + [references/mandala-de-anuncios.md](references/mandala-de-anuncios.md) |
| Copy de criativo estático | [references/anuncios-texto.md](references/anuncios-texto.md) |
| Carrossel, Reels, linha editorial | [references/formatos/conteudo-social.md](references/formatos/conteudo-social.md) |
| Roteiro de vídeo, avatar IA, VSL | [references/formatos/roteiro-video.md](references/formatos/roteiro-video.md) |
| Turbinar um trecho que já existe | [references/formatos/aplicar-elementos.md](references/formatos/aplicar-elementos.md) + [references/elementos-literarios.md](references/elementos-literarios.md) |
| Só revisar um texto pronto | Pule para o Passo 3 |

Os arquivos de formato foram escritos como comandos de projeto. Se algum passo citar um caminho de arquivo que não existe (`meus-produtos/`, `entregas/`), use o contexto que você coletou no Passo 0 e siga o resto do fluxo normalmente. Se citar um comando que não existe neste projeto (`/pagina-visual`, `/criativo-estatico`, `/instagram-dashboard`), avise que aquele passo é opcional e entregue a copy.

---

## Passo 2. Escreva aplicando o Manual

Fonte única de princípios e vícios: [references/manual-copy.md](references/manual-copy.md). São 15 princípios fundamentais e 20 vícios proibidos. Leia antes de escrever, não depois.

Os quatro que mais mudam o resultado:

1. **Ensinar em vez de prometer.** Se o leitor chega ao final sem ter aprendido nada, a copy falhou.
2. **Nomear cria realidade.** Dê nome próprio ao problema, ao mecanismo, ao inimigo. Nome transforma ideia em coisa que existe no mundo.
3. **Toda copy precisa de tese.** Não descreva o problema, argumente por que ele existe. "Você procrastina" vira "Você procrastina porque seu cérebro foi programado para ação imediata, não para acumular reserva".
4. **Venda o Quadro com o Decorado.** Resultado técnico sozinho não move ninguém. Mostre a consequência na vida real.

Para deixar o texto memorável em vez de correto e sem graça, aplique os 26 Elementos Literários: [references/elementos-literarios.md](references/elementos-literarios.md). De um a três por trecho, nunca mais que isso.

Contexto do método completo, quando precisar entender a estrutura por trás: [references/metodo-vtsd.md](references/metodo-vtsd.md).

---

## Passo 3. Revise antes de entregar (nunca pule)

Você é a última barreira. O usuário não vê o texto antes de você revisar.

Rode, nesta ordem, o fluxo descrito em [references/revisora.md](references/revisora.md):

1. **Bloco A.** Os 20 vícios proibidos do Manual. Tolerância zero nos absolutos.
2. **Bloco B.** Argumento e especificidade. Tem tese? Tem dado concreto?
3. **Bloco C.** Estrutura VTSD. Ensina antes de vender, nome próprio, inimigo, razão mais emoção, Quadro mais Decorado, dor real.
4. **Bloco D.** Só para página. Headline por seção, depoimento estruturado, autoridade concreta, bônus ancorado, facilitação visual do método, mecanismo explicado.
5. **AI slop.** Padrões que denunciam texto gerado por IA: [references/ai-slop-frases.md](references/ai-slop-frases.md) e [references/ai-slop-estruturas.md](references/ai-slop-estruturas.md).

Substituições linha a linha para os vícios mais comuns: [references/substituicoes-vicios.md](references/substituicoes-vicios.md). Exemplos de antes e depois: [references/exemplos-antes-depois.md](references/exemplos-antes-depois.md).

**Corrija direto no texto.** Não devolva lista de problemas para o usuário, devolva o texto corrigido. A revisão é invisível.

---

## As 12 proibições absolutas

Checklist completo com a correção de cada item: [references/checklist-12-proibicoes.md](references/checklist-12-proibicoes.md). Aplique frase por frase. Se qualquer item falhar, reescreva o trecho e verifique de novo antes de continuar.

1. Travessão em qualquer texto. Sem exceção.
2. Ponto de exclamação.
3. Pergunta no gancho ou no título.
4. Estrutura "Não é X. É Y."
5. Promessa vaga sem dado concreto.
6. "mesmo que" e "sem precisar".
7. Erro de português.
8. Lero-lero: palavra genérica que soa bem e não diz nada.
9. Copy sem tese: descreve o problema sem argumentar por que ele existe.
10. Sigla ou nome de técnica sem explicação no mesmo parágrafo.
11. Depoimento que só elogia, sem resultado concreto.
12. Vender só o Quadro sem o Decorado.

E a regra que não é numerada porque vale para tudo: **o produto não aparece no lead.** Nada de curso, treinamento, compre, nome do método ou sigla do programa no início da copy. O lead fala da dor, do desejo ou da transformação do leitor.

---

## Passo 4. Gravar o arquivo, medir e esperar o aval (obrigatório no DesignSpace)

Três travas deste projeto, que valem tanto quanto a revisão do Passo 3:

0. **A copy vira arquivo antes de virar resposta.** Um arquivo por conjunto, com **todos** os anúncios dele, em `produtos/<slug>/criativos/<YYYY-MM-DD-tema>/copy-<YYYY-MM-DD-tema>.md`. Se a pasta do conjunto não existe, crie a árvore antes. Corrigiu depois? Edite o mesmo arquivo, sem `-v2` nem `-final`. O usuário lê e aprova abrindo o arquivo, então o que você devolve no chat é **o caminho dele**, não a copy colada.

1. **Meça antes de entregar.** Copy de anúncio passa pelo validador, sem exceção:

   ```bash
   python3 .claude/skills/anuncio-flp/scripts/validar-copy.py <arquivo-de-copy.md>
   ```

   Ele mede volume por campo, repetição entre anúncios, frase reaproveitada, entrega da mensagem, vícios de Light Copy e a forma do CTA. **Código 1 significa que o trabalho não terminou.** Corrija e rode de novo até sair 0.

2. **Nenhuma imagem é gerada antes de o usuário aprovar a copy por escrito.** Apresentar a copy e começar a gerar na mesma passada não conta como aprovação. Ver a regra dura no `CLAUDE.md`.

Devolva o trabalho curto, com três coisas nesta ordem: **o caminho do arquivo como link clicável**, quantos anúncios tem e qual o eixo em uma linha, e o resultado do validador. Depois disso, pare. O próximo passo é do usuário.

---

## Como entregar

No DesignSpace vale o Passo 4 acima: a copy é gravada em arquivo e o que vai para o chat é o caminho. Fora de um conjunto de anúncios (um trecho solto, uma bio, um assunto de e-mail), mostre a copy pronta, limpa, sem comentário de processo no meio. Se gerou variações, numere e pergunte qual seguir.

Nunca explique que você aplicou o checklist. O usuário quer o texto, não o relatório.
