---
name: copy-card
description: Cria o conteúdo textual que vai dentro do card de design — Head, Subhead e CTA — usando a Mandala de 18 Tipos (metodologia VTSD), calibrado pela fase do funil (Topo, Meio ou Fundo). Use sempre que uma peça precisar de texto: criativo, banner, card de campanha, arte de lançamento, peça de anúncio. Roda antes do visual-generator e do figma-builder.
---

# Copy de card

Gera o texto que vai **dentro do design**. Head, Subhead e CTA. Nada de legenda de rede social, nada de anúncio de plataforma.

## Idioma

Português do Brasil, acentuação correta. Nunca entregue copy em inglês, salvo pedido expresso.

---

## Passo 0. Carregar as regras (obrigatório, antes de escrever qualquer palavra)

Leia, nesta ordem:

1. `references/manual-copy.md` — princípio central, 15 princípios, 20 vícios proibidos, checklist A/B/C/D. **Fonte única de verdade.**
2. `references/checklist-light-copy.md` — as 12 proibições absolutas do Light Copy.
3. `references/anatomia-do-card.md` — o que é Head, Subhead e CTA, com limites e formato de entrega.
4. `references/mandala-18-tipos.md` — os 18 tipos distribuídos por fase do funil e os CTAs de cada fase.

Consulte durante a geração:
- `references/elementos-literarios.md` — os 26 elementos. Aplicar de 1 a 3 por peça, silenciosamente.
- `references/exemplos-leads-4-categorias.md` — régua de especificidade e inimigo concreto.

---

## 1. Contexto

**Procure o briefing antes de perguntar qualquer coisa.** Nesta ordem:

1. `briefs/` — brief da tarefa atual (gerado por `/brief`)
2. `brand/<cliente>.md` — brand kit: tom, essência, público, do/don't
3. `outputs/` — cards anteriores do mesmo cliente

**Se encontrar:** extraia internamente o Quadro (transformação técnica), o Decorado (consequência na vida), o público, a dor real, o preço e o tom. Confirme em uma linha qual arquivo usou como base e siga.

**Se não encontrar nada:** rode a entrevista curta abaixo. **Uma pergunta por vez. Espere a resposta antes da próxima. Nunca agrupe.**

```
Qual o nicho ou tema do projeto?
```
```
Quem vai ver esse card?
```
```
Qual a transformação principal que o projeto entrega?
```
```
Qual a oferta ou o próximo passo que o card leva? (preço, evento, cadastro, conversa)
```

**Não repetir ângulos.** Varra `outputs/` e identifique quais ângulos, dores e premissas já foram usados com esse cliente. Priorize os ainda não explorados. Se todos já foram usados, escolha os de maior potencial e avise que está retomando o tema.

---

## 2. Fase do funil

**Esta é a única pergunta obrigatória** quando o brief não define a fase. Ela determina o nível de consciência e, portanto, o tom inteiro do card.

```
Qual a fase do funil desse card?

1. Topo    — não sabe que tem o problema. O card revela e nomeia.
2. Meio    — sabe do problema, avalia caminhos. O card argumenta.
3. Fundo   — pronto para decidir. O card prova e converte.

Digite o número:
```

Se o brief já define a fase, não pergunte. Confirme em uma linha e siga.

**Pergunte também o rótulo do botão** se o projeto não usa "Saiba mais":

```
O botão do projeto é "Saiba mais" ou outro rótulo?
(ex: Cadastre-se, Fale conosco, Comprar, Quero participar)
```

---

## 3. Confirmação antes de gerar

```
Resumo do que vou criar:
- Projeto/Cliente: [nome]
- Fase do funil: [Topo | Meio | Fundo]
- Brand kit: [arquivo ou: nenhum]
- Botão: [rótulo]
- Quantidade: 3 variações com tipos diferentes da Mandala

1. Pode gerar
2. Quero ajustar algo
```

---

## 4. Geração

Escolha **3 tipos diferentes** da Mandala, todos adequados à fase escolhida. Ver a distribuição por fase em `references/mandala-18-tipos.md`.

Exemplo de composição para Meio: Comparação, Certo/Errado, Explicação.

**Antes de escrever, de forma silenciosa:** abra `references/elementos-literarios.md` e escolha de 1 a 3 elementos que combinem com o tipo, a fase e o tom da marca. Aplique na Head, na Subhead ou no CTA. **Nunca revele quais elementos usou nem que consultou a lista.**

Cada variação sai neste formato, e só neste:

```
VARIAÇÃO 1 — [Tipo da Mandala] — [Topo | Meio | Fundo]

HEAD:     [4 a 9 palavras]
SUBHEAD:  [1 a 2 linhas com o dado concreto]
CTA:      Clique em "Saiba mais" e [complemento]
```

### As regras que definem a qualidade

- **Head** — premissa não óbvia. Nunca pergunta. Nunca óbvia para quem já está no nicho. O produto não aparece: nem nome, nem "curso", nem "método", nem sigla.
- **Subhead** — carrega o argumento concreto: número, prazo, mecanismo ou inimigo concreto. Subhead vaga anula Head boa.
- **Head + Subhead entregam o contexto completo.** Quem só olha o card, sem clicar, entende o assunto e por que importa. Card que só faz sentido depois do clique falhou.
- **CTA** — calibrado pela fase. Nunca promete o que a Head e a Subhead não sustentaram. Urgência só no Fundo, e só se for real.
- **Inimigo concreto** — o culpado é externo (o método que ensinaram, o jeito antigo, o mito do nicho), nunca "você é o problema".
- **Especificidade** — "R$ 1.600" ganha de "muito dinheiro". "Em 3 dias" ganha de "rápido".
- **Nomear cria realidade** — crie nome próprio para o conceito ou problema sempre que couber.

---

## 5. Auto-revisão obrigatória, antes de exibir

Nada é mostrado antes disso:

1. Gere as 3 variações internamente.
2. Aplique o checklist de `manual-copy.md`, Blocos A, B e C, frase por frase.
3. Aplique as 12 proibições de `checklist-light-copy.md`, frase por frase.
4. Confira os limites de palavra de `anatomia-do-card.md`. Head acima de 9 palavras quebra a hierarquia do design — corte.
5. Corrija tudo direto no texto. Não entregue lista de problemas nem peça autorização para corrigir.
6. Se um alerta depender de dado que só o usuário tem (número de alunos, depoimento com resultado real, faturamento), peça esse dado específico antes de entregar a variação afetada.
7. **Acione a skill `revisora` com o texto completo, como último passo.** Ela roda a checagem de AI slop e a de acentuação pt_BR, que o checklist manual não cobre, e devolve o texto corrigido. É esse texto que vai para a tela.

**Invisibilidade obrigatória:** nunca diga que rodou o checklist nem que existe uma revisora. Entregue só a versão final.

---

## 6. Aprovação e salvamento

Após mostrar as 3 variações:

```
1. Aprovar e salvar
2. Quero ajustar algo
```

Só salve após aprovação. Salve em `outputs/YYYY-MM-DD-cliente-copy-card-[fase].md`, com o tipo da Mandala de cada variação registrado. Informe o caminho completo como texto copiável.

---

## 7. Passagem para o design

Copy aprovada é entrada do trabalho visual. Ofereça o próximo passo:

- **`visual-generator`** monta o background no Magnific. Passe o mood e a paleta do brand kit. **Nunca peça texto ao modelo de imagem** — todo prompt de fundo termina com `no text, no numbers, no readable characters, no logos`. O texto entra no Figma, não no pixel gerado.
- **`figma-builder`** monta o card. Cada bloco vira camada editável nomeada (`Head`, `Subhead`, `CTA`), amarrada aos tokens tipográficos do brand kit.
- **`/ad-set`** expande o card aprovado para os demais formatos.
- **`brand-guardian`** audita antes da entrega. Contraste da Head sobre a imagem é o achado mais comum.

Sugira as 3 variações como teste A/B quando a peça for para tráfego pago.
