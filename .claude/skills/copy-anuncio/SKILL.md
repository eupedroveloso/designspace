---
name: copy-anuncio
description: Criar pacotes completos de anúncios para Meta Ads e Google Ads usando a Mandala de 18 Tipos de Anúncios da metodologia VTSD. Gera 3 variações de copy com gancho, desenvolvimento e CTA calibrados por fase de funil, mais briefing visual para imagem ou vídeo. Use quando o pedido envolver anúncio, criativo de tráfego pago, campanha Meta, Google Ads, gancho de vídeo curto ou legenda de anúncio.
---

> **Fonte única do método: a skill `light-copy`.** O pacote Light Copy completo foi instalado em `.claude/skills/light-copy/` em 2026-08-26, e é ele que manda. As `references/` desta pasta são cópias parciais e mais antigas, mantidas só para os links internos desta skill não quebrarem. Em qualquer divergência, vale o `light-copy`.

# Anúncio. Mandala de 18 Tipos (VTSD)

Cria pacotes de anúncios usando os 18 tipos da Mandala VTSD mais a estrutura de campanha.

Esta skill é autossuficiente: tudo que ela precisa está na pasta `references/` ao lado deste arquivo. Não depende de nenhum outro arquivo do projeto onde foi instalada.

## Idioma

Toda a saída é em português do Brasil, com acentuação correta. Nunca entregue copy em inglês, salvo pedido expresso.

## Passo 0. Carregar as regras (obrigatório, antes de qualquer outra coisa)

Leia, nesta ordem, antes de escrever qualquer gancho:

1. `references/manual-copy.md`. Princípio central, 15 princípios fundamentais, 20 vícios proibidos e o checklist final em Blocos A, B, C e D. É a fonte única de verdade da copy.
2. `references/checklist-light-copy.md`. As 12 proibições absolutas do Light Copy.
3. `references/mandala-18-tipos.md`. Os 18 tipos, os 4 objetivos, os 3 momentos de consumo, CTAs por fase e estrutura de campanha.

Consulte conforme a necessidade, durante a geração:

- `references/elementos-literarios.md`. Os 26 elementos. Aplicar de 1 a 3 por peça, de forma silenciosa.
- `references/formatos-meta-ads.md` e `references/formatos-google-ads.md`. Limites de caractere e dimensões.
- `references/formatos-virais-instagram.md`. Estruturas de retenção para vídeo curto.
- `references/exemplos-criativos.md`. Referências de peça pronta.

---

## 1. Contexto

**Passo 1. Procurar um briefing de produto já existente no projeto.**

Verifique, nesta ordem, se algum destes caminhos existe:

- `meus-produtos/.ativo` e, se existir, `meus-produtos/{ativo}/perfil.md` e `meus-produtos/{ativo}/idconsumidor.md`
- `perfil.md`, `produto.md` ou `briefing.md` na raiz do projeto
- qualquer arquivo em `docs/` ou `briefing/` com o Quadro e o público descritos

**Se encontrar:** leia e extraia internamente Quadro, Furadeira, Decorados, Urgências Ocultas, público, preço e tom. Confirme com o usuário em uma linha qual arquivo usou como base e siga para o passo 2.

**Se não encontrar nada:** faça a entrevista curta de contexto, UMA pergunta por vez.

```
Qual o nicho ou tema do produto?
(ex: "Tarô", "Emagrecimento", "Finanças para autônomos")
```

```
Quem é o público que vai ver esse anúncio?
(ex: "Mulheres de 30 a 50 anos que estudam tarô há 1 a 3 anos")
```

```
Qual a transformação principal que o produto entrega? (o Quadro)
(ex: "Fazer leituras de tarô com confiança e cobrar por isso")
```

```
Qual o preço do produto?
(ex: "R$ 497", "gratuito", "R$ 97/mês")
```

**Passo 2. Verificar o histórico de anúncios.**

Procure anúncios anteriores na pasta de saída definida no passo 6. Identifique quais ângulos, dores e benefícios já foram explorados.

**Regra de não repetição:** priorize ângulos ainda não usados. Se todos já foram usados, escolha os de maior potencial e avise que está retomando o tema.

Se não houver nada anterior: "É o primeiro pacote de anúncios. Vamos usar os ângulos mais relevantes para a fase escolhida."

---

## 2. Entrevista

**REGRA ABSOLUTA: uma pergunta por vez. Esperar a resposta antes da próxima. Nunca agrupar perguntas.**

**Bloco 1. Tipo de campanha:**
```
Perpétuo ou pico de vendas?

1. Perpétuo
2. Pico de vendas

Digite o número:
```

---

**Se Perpétuo. Perguntar em sequência, uma por vez:**

```
Qual o objetivo dos anúncios?

1. Descoberta. atrair novas pessoas que ainda não conhecem o produto
2. Relacionamento. criar conexão e autoridade com quem já segue
3. Conversão. vender
4. RMKT. converter quem já viu a página de vendas

Digite o número:
```

```
Qual o momento de consumo do público?

1. Prontidão. está pronto para comprar
2. Urgência Oculta. tem o problema, mas ainda não busca solução
3. Oportunidade. público amplo, ainda não está pronto para comprar

Digite o número:
```

```
Qual o tipo de anúncio?

1. Imagem estática
2. Vídeo

Digite o número:
```

---

**Se Pico de Vendas. Perguntar a fase:**

```
Qual fase do pico de vendas?

1. Captura
2. Aquecimento
3. Lembrete
4. Venda
5. Remarketing

Digite o número:
```

**Se Captura ou Aquecimento. Perguntar em sequência, uma por vez:**

```
Qual o nome do evento?
(ex: "Workshop Tarô Desperto", "Semana da Leitura Segura")
```

```
Qual a promessa do evento?
(ex: "Aprender a fazer sua primeira tiragem completa em 3 dias")
```

```
Qual a data do evento?
(ex: "dia 15 de abril", "de 21 a 25 de maio")
```

**Se Venda ou Remarketing. Perguntar:**

```
Qual é a oferta?
(ex: "Curso Tarô em Duas Pontes por R$ 497 com bônus exclusivo até domingo")
```

---

**Confirmação antes de gerar, para qualquer caminho:**
```
Resumo do que vou criar:
- Tipo: [perpétuo ou pico de vendas]
- Objetivo/Fase: [objetivo ou fase]
- Momento: [momento de consumo, se perpétuo]
- Formato: [tipo de anúncio. se vídeo: "Vídeo (duração definida na geração)"]
- [dados do evento ou oferta, se aplicável]
- Quantidade: 3 variações com tipos diferentes da Mandala da Criatividade

1. Tudo certo, pode gerar
2. Quero ajustar algo
```

**REGRA:** nunca indicar duração do vídeo no resumo de confirmação. A duração é definida apenas na geração da copy.

---

## 3. Regras de Copy

**Fonte única e obrigatória:** `references/manual-copy.md`. Toda variação passa pelo checklist dos Blocos A, B, C e D antes de virar entregável.

**Reforços específicos de anúncio:**

- **Gancho nos primeiros 3 segundos:** afirmação contra-intuitiva, paradoxo, revelação ou quebra-padrão. NUNCA pergunta, NUNCA frase óbvia.
- **Inimigo concreto ou método antigo:** o anúncio precisa de um culpado externo (sistema, método ensinado, mito do nicho), nunca "você é o problema".
- **Entregar valor real no próprio post ou vídeo:** quem lê ou assiste aprende algo concreto. Anúncio que só promete não converte.
- **Produto não aparece no gancho:** nada de "curso", "treinamento" ou nome do método nos 3 segundos iniciais. Só a realidade do leitor.
- **CTA adequado à fase do funil.** Ver tabela na seção 4.

**Estrutura obrigatória para TODO vídeo, cerca de 45 a 60 segundos, 150 a 200 palavras:**

```
[0 a 3s]    GANCHO      → Afirmação contra-intuitiva ou quebra-padrão.
                          Texto na tela e fala simultâneos.
[4 a 15s]   TEASE       → Expande o gancho, cria tensão, contextualiza o problema.
[16 a 42s]  ENTREGA     → Ensina, demonstra ou revela algo real e concreto.
                          NUNCA apenas prometer. ENTREGAR dentro do vídeo.
[43 a 48s]  REGANCHO    → Texto na tela sintetizando a ideia central
                          (âncora visual para quem assiste sem som).
[49 a 55s]  CTA         → Convite direto adequado à fase. Sem urgência forçada.
```

**Para Descoberta:** duração alvo de 35 a 45 segundos. Para Captura, Conversão e demais fases: 45 a 60 segundos.

**Três estruturas de roteiro:**

| Estrutura | Quando usar | Lógica de retenção |
|---|---|---|
| **Loop Perfeito** | Revelação, insights | O final conecta ao gancho, incentiva replay |
| **Tutorial de 3 Passos** | Procedimento, ensino | Cada passo avança a narrativa, a pessoa assiste até o fim |
| **Quebra-Padrão** | Contraste, paradoxo | Começo inesperado, força a pausa no scroll |

Usar estruturas diferentes nas 3 variações sempre que possível. Detalhamento em `references/formatos-virais-instagram.md`.

---

## 4. Geração, após aprovação do resumo

Use a Mandala de 18 Tipos, descrita em `references/mandala-18-tipos.md`.

**Antes de escrever, de forma silenciosa:** abra `references/elementos-literarios.md` e escolha de 1 a 3 elementos que combinem com o tipo da Mandala, a fase do funil e o tom do produto. Aplique-os no gancho, no desenvolvimento ou no CTA. Nunca revele ao usuário quais elementos foram usados nem que a lista foi consultada.

**Para Meta Ads, gere 3 variações usando tipos diferentes da Mandala:**

- Variação 1: ex. Comparação, Certo vs Errado
- Variação 2: ex. Prova, Demonstração
- Variação 3: ex. Problema-Solução, Curiosidade

**Cada variação inclui:**

- Texto principal em Light Copy, sem ponto de exclamação, sem pergunta no gancho
- Headline, máximo de 40 caracteres
- Descrição
- CTA adequado à fase

**CTAs por fase:**

| Fase | CTA típico |
| --- | --- |
| Descoberta | Seguir, curtir, comentar, compartilhar |
| Relacionamento | Comentar, DM, salvar, lives |
| Captura / Aquecimento | Quero participar, garantir minha vaga, me inscrever |
| Conversão / Venda | Comprar agora, garantir vaga, quero começar |
| Remarketing | Comprar agora, retomar oferta, última chance |

**Estrutura de todo anúncio VTSD, texto ou legenda. Padrão de profundidade obrigatório:**

- **GANCHO:** premissa não óbvia. NUNCA uma pergunta, NUNCA algo óbvio para quem já está no nicho. Uma ou duas frases fortes.
- **DESENVOLVIMENTO:** mínimo de 2 parágrafos substanciais com argumento específico, concreto e não óbvio. Não pode ser resumo vago, precisa entregar valor por si só mesmo sem o vídeo. Raso, curto e genérico são proibidos.
- **CTA:** convite direto adequado à fase do funil.

**REGRA DE QUALIDADE:** todo anúncio deve entregar valor real. Nenhum anúncio pode ser óbvio, raso ou curto demais. O desenvolvimento precisa ter profundidade suficiente para que a pessoa aprenda, entenda ou se reconheça, mesmo lendo só a legenda.

**Exemplos de gancho ERRADO:**

- "Sabe aquela sensação de travar na leitura?" ❌ (pergunta)
- "Você já se sentiu insegura com o tarô?" ❌ (pergunta)
- "Aprender tarô é difícil." ❌ (óbvio)
- "Você não sabe quanto cobrar?" ❌ (pergunta e óbvio)
- "Cobrar é difícil para tarotistas." ❌ (óbvio)

**Exemplos de gancho CERTO:**

- "A leitora que mais trava raramente é a que sabe menos." ✓ (contra-intuitivo)
- "Decorar os 78 significados é o caminho mais rápido para travar na leitura." ✓ (paradoxo)
- "Você não trava na tiragem por saber pouco. Você trava porque aprendeu na ordem errada." ✓ (revelação)
- "Parei de estudar os significados das cartas por 30 dias. Minha leitura melhorou." ✓ (quebra-padrão)
- "O método que todo mundo ensina primeiro no tarô é o que mais gera travamento na leitura real." ✓ (premissa não óbvia)

**Para Google Ads:**

- 15 títulos, máximo de 30 caracteres cada
- 4 descrições, máximo de 90 caracteres cada
- Palavras-chave e negativas

Limites completos em `references/formatos-google-ads.md`.

---

## 5. Auto-revisão obrigatória, antes de exibir

Antes de mostrar qualquer coisa ao usuário:

1. Gere as 3 variações completas internamente. Nada é exibido ainda.
2. Aplique o checklist de `references/manual-copy.md`, Blocos A, B, C e D, frase por frase.
3. Aplique as 12 proibições de `references/checklist-light-copy.md`, frase por frase.
4. Corrija tudo direto no texto. Não entregue lista de problemas nem peça autorização para corrigir.
5. Se um alerta depender de um dado que só o usuário tem (número de alunos, depoimento real com resultado), peça esse dado específico antes de entregar o bloco afetado.

**Invisibilidade obrigatória:** nunca diga que rodou o checklist. Entregue apenas a versão final.

---

## 6. Aprovação e salvamento

Após mostrar os anúncios gerados, pergunte:

```
1. Aprovar e salvar
2. Quero ajustar algo
```

Só salve após a aprovação.

**Onde salvar.** Use, na ordem, a primeira pasta que existir:

1. `meus-produtos/{ativo}/entregas/criativos/`
2. `entregas/anuncios/`
3. `anuncios/` na raiz do projeto, criando a pasta se necessário

Nome do arquivo: `anuncios-meta-[formato]-[objetivo]-[produto].md`

Informe sempre o caminho completo do arquivo salvo, como texto copiável.

---

## 7. Briefing visual

Após salvar a copy, pergunte qual ferramenta o usuário vai usar e gere os prompts adaptados.

**Se Imagem Estática:**

```
Qual IA você vai usar para gerar a imagem?

1. Midjourney
2. ChatGPT (DALL-E)
3. Leonardo AI
4. Adobe Firefly
5. Canva AI (Magic Media)
6. Stable Diffusion / ComfyUI
7. Outra, me diga qual

Sugestão: para anúncios com pessoas reais e estética fotográfica, o Midjourney
e o Leonardo AI costumam entregar os melhores resultados. Para quem já usa o
Canva no dia a dia, o Canva AI é a opção mais prática.

Digite o número:
```

**Se Vídeo:**

```
Qual IA você vai usar para gerar o vídeo?

1. HeyGen (avatar com seu rosto ou avatar pronto, melhor para talking head)
2. Pika (geração a partir de prompt, rápido e gratuito para começar)
3. Kling (vídeo realista, ótimo para cenas com pessoas)
4. RunwayML (controle avançado de edição e geração)
5. Luma Dream Machine (realismo alto, bom para ambientes e produtos)
6. Vou gravar eu mesmo, preciso do prompt como briefing de direção
7. Outra, me diga qual

Sugestão: se você quer um talking head com script lido por avatar, o HeyGen é
o mais indicado, ele aceita o roteiro direto. Se quiser gerar o vídeo a partir
de uma descrição visual, Pika ou Kling entregam resultados mais rápidos sem
precisar de configuração.

Digite o número:
```

**REGRA ABSOLUTA para prompts de background gerados por IA:**

- NUNCA pedir texto, números, letras, datas ou caracteres legíveis no prompt
- NUNCA pedir calendários, relógios com números, telas com texto visível
- SEMPRE incluir no final: `no text, no numbers, no readable characters, no logos`
- O background deve ser uma CENA, TEXTURA ou ATMOSFERA, nunca um design com informação

**Sintaxe por ferramenta:**

**Midjourney.** `[descrição da cena], [estilo], [iluminação], [câmera e ângulo], [paleta], [referência de fotógrafo se aplicável] --ar 1:1 --v 6 --style raw`. Para stories, `--ar 9:16`. Evitar verbos de ação, descrever o estado visual resultante. Incluir termos técnicos de fotografia: `shallow depth of field`, `soft side lighting`, `editorial photography`.

**ChatGPT (DALL-E).** Parágrafo descritivo: "Create a photorealistic image of [cena]. The style is [estilo]. Lighting is [iluminação]. The composition shows [enquadramento]. Color palette: [paleta]. Aspect ratio: [proporção]." Não aceita parâmetros técnicos, tudo vai no texto corrido.

**Leonardo AI.** Estrutura similar ao Midjourney, sem parâmetros `--`. Indicar o modelo: `Leonardo Diffusion XL` para fotos realistas, `PhotoReal` para pessoas. Separar elementos por vírgula. Adicionar negative prompt separado.

**Adobe Firefly.** Inglês descritivo e simples, sem sintaxe especial. Enfatizar estilo com termos reconhecidos: `professional photography`, `studio light`, `clean background`. Proporção vai no campo de configuração, não no prompt.

**Canva AI (Magic Media).** Prompts curtos e diretos. Cena principal mais estilo visual em uma ou duas frases. Não suporta parâmetros técnicos.

**Stable Diffusion / ComfyUI.** `[masterpiece, best quality, photorealistic], [cena], [estilo], [iluminação], [câmera]`. Negative prompt obrigatório: `(worst quality, low quality, blurry, distorted face:1.4), watermark, text`.

**HeyGen.** Não gerar prompt de imagem. Gerar o roteiro formatado para colar no campo de texto do avatar, com `[pausa]` e `[ênfase]` marcados.

**Pika.** Inglês, cena em movimento: `[sujeito] [ação], [ambiente], [estilo cinematográfico], [iluminação], [câmera: movimento e ângulo]`.

**Kling.** `[cena inicial], [movimento da câmera], [ação do sujeito], [ambiente], [estilo], [iluminação]`. Performa melhor com pessoas em ação realista.

**RunwayML.** `[sujeito e ação], [ambiente detalhado], [estilo de câmera], [iluminação cinematográfica]`. Indicar se é Image to Video ou Text to Video. Termos que funcionam: `cinematic`, `smooth camera movement`, `natural lighting`.

**Luma Dream Machine.** `[descrição da cena], [movimento da câmera], [iluminação], [atmosfera visual]`. Melhor com ambientes e produtos, menos preciso com pessoas falando.

**Se for gravar o próprio vídeo.** Briefing de direção completo em português: enquadramento, iluminação, postura, tom de voz, ritmo de fala, gestos, fundo, roupas recomendadas, texto na tela e momento de inserção.

Apresente os prompts prontos para copiar e colar, um por variação. Salve na mesma pasta da copy, como `prompts-visuais-[formato]-[ia-escolhida]-[produto].md`.

---

## 8. Próximo passo

Informe o caminho dos arquivos salvos e sugira a ação seguinte: criar a página de destino, gerar mais variações para teste A/B ou montar a estrutura de campanha descrita em `references/mandala-18-tipos.md`.
