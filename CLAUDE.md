# DesignSpace

Hub para executar tarefas complexas de design ponta a ponta: **UI/Produto**, **Marketing/Peças visuais** e **Branding/Identidade**.

O trabalho acontece através de conectores (Magnific, Figma), agentes especializados e skills de fluxo. Este arquivo é o mapa do stack — leia antes de começar qualquer tarefa.

---

## Stack

| Camada | Ferramenta | Papel |
|---|---|---|
| Geração visual | **Magnific** (MCP) | Gera, edita, faz upscale e trata imagens/vídeo. É a fonte de pixels. |
| Montagem / estrutura | **Figma** (MCP + plugin Desktop Bridge) | Onde a peça vira arquivo editável: telas, componentes, variantes, artes, guidelines. |
| Orquestração | Agentes em `.claude/agents/` | Executam papéis especializados sem poluir o contexto principal. |
| Fluxos | Skills em `.claude/skills/` | Roteiros repetíveis (moodboard, ad-set, tela de UI, brand kit). |

### Contas conectadas

- **Figma** — `Pedro Veloso` / `pedrolucas@vtsd.com.br` / time **Ready To Go** (seat Full, tier pro).
- **Magnific** — conta `Conta Extra 02`. Cheque saldo com `account_balance` antes de lotes grandes.

### Duas vias de acesso ao Figma — não confunda

| Via | Autenticação | Usa para |
|---|---|---|
| **Conector MCP** | OAuth (já autorizado) | Tudo do MCP: `use_figma`, `get_design_context`, `create_new_file`, `upload_assets`, `search_design_system`. **Não aceita token.** |
| **API REST** | `FIGMA_ACCESS_TOKEN` em `.env` | O que o MCP não cobre: listar projetos de um time, ler arquivo por ID, versões, comentários, webhooks. |

O token fica em `.env` (chmod 600, no `.gitignore`). **Nunca imprima o valor** — leia sempre do arquivo, jamais cole em comando, log ou resposta ao usuário.

Verifique ambas com `/figma-status`.

---

## Destino no Figma — regra dura

**Sempre perguntar em qual arquivo do Figma a peça deve ser criada, antes de criar qualquer coisa.** Vale para criativo, tela, componente, moodboard, guidelines, diagrama — qualquer coisa que vire nó no Figma. Sem exceção, em toda sessão.

A pergunta é a primeira da tarefa, não a última antes de montar:

> **Em qual arquivo do Figma eu crio essa peça?** Me manda o link. Se tiver página e seção específicas, me diz também.

Depois de responder, registre — é o que libera a trava:

```bash
.claude/hooks/figma-destino.sh set "<link>" --pagina "<página>" --secao "<seção>"
```

**Só a resposta do usuário nesta sessão conta.** Link de conversa anterior, file key da memória ou do `outputs/`, arquivo citado aqui no `CLAUDE.md` e arquivo por acaso aberto no desktop **não são autorização** — são atalho de leitura. Oferecer o arquivo da última entrega como opção é bom; assumir que ele continua valendo é o erro.

Um hook `PreToolUse` bloqueia `use_figma`, `create_new_file`, `figma_execute` e as demais tools de escrita enquanto não houver destino registrado, e o registro é apagado a cada sessão nova. Leitura — `get_screenshot`, `get_design_context`, `whoami`, `/figma-status` — continua livre. Se o bloqueio aparecer, ele está certo: pare, pergunte, registre, repita a chamada. Não contorne por outra tool nem crie arquivo novo para destravar.

`use_figma` e `figma_execute` escrevem **no arquivo em foco no Figma desktop**, não no link registrado. Confirme que os dois batem antes da primeira escrita.

Ritual completo, incluindo o que fazer quando o usuário não sabe onde quer: `/figma-destino`.

---

## Fluxo obrigatório de criação de anúncio

Nesta ordem, sem pular etapa:

0. **Perguntar duas coisas, antes de tudo:**
   - **Para qual produto é a criação.** Lista o que existe em `produtos/`. Se o produto não existir, rode `/briefing-produto` para criá-lo.
   - **Em qual arquivo do Figma a peça vai nascer.** Link, página e seção. Rode `/figma-destino` — a pergunta vem antes de gastar crédito de imagem, não na hora de montar.
1. **`/briefing-produto`** — extrai da landing page (URL) e/ou do Figma: nome, promessa, formato, datas, preço, como funciona, entregáveis, garantia, público, autoridade, prova, CTA, **nicho**, **paleta**, **tipografia** e **logo em SVG**. Salva em `produtos/<slug>/`. Confirmar as lacunas com o usuário antes de seguir.
2. **Pesquisar o nicho** — busca web e Pinterest por *flyer, banner, post, ads, identidade visual* daquele mercado. Extrair paleta praticada, tipografia, estética fotográfica e elementos recorrentes.
3. **Chamar o agente `copywriter-light`** — toda copy sai dele, sempre. Ele carrega a skill `/light-copy`, que é o pacote Light Copy completo (Manual da Copy, 12 proibições, 26 Elementos Literários, Mandala de Anúncios, revisora anti AI slop) e a fonte única do método. Nunca escrever copy no olho, nunca pular o agente.
3.1. **Validar a copy por medição, antes de gastar um único crédito de imagem.** Regra dura, ver abaixo.
3.2. **Gravar a copy inteira do conjunto num arquivo, entregar o caminho ao usuário e esperar o aval por escrito.** Etapa bloqueante: nenhuma imagem é gerada antes disso. Regra dura, ver abaixo.
3.3. **Aprovar o plano de composição no agente `auditor-originalidade`.** Cada peça declara estrutura, técnica de ilustração, enquadramento e paleta, e nenhuma combinação se repete no conjunto. Regra dura, ver abaixo.
4. **Carregar `/ref-ads-dna`** — o DNA visual do board de referências do usuário. Escolher a categoria (A–L) que serve o objetivo da campanha e puxar o DNA transversal: direção da luz, paleta de 2-3 cores, textura do assunto principal, formato vertical e zona de respiro para o texto. Daqui sai a **cena e o tratamento fotográfico** — nunca um layout pronto. A escolha da categoria passa antes pela regra de leitura imediata abaixo: o DNA define o acabamento, e a legibilidade define a cena.
5. **Desenhar layout original a partir da cena.** Ver a regra de originalidade abaixo.
6. **Conferir contra o benchmark** do cliente e auditar com `analisador-criativo`.

### Organização das pastas de ADs — regra dura

Estrutura fixa e permanente, definida pelo usuário em 2026-08-26. Vale para toda leva de anúncios, sem exceção. **Crie a árvore antes de gerar a primeira peça.**

```
produtos/<slug>/
├── briefing.md
├── identidade/                     logo.svg · paleta.md · tipografia.md
└── criativos/
    └── <YYYY-MM-DD-tema>/          o conjunto
        ├── copy-<conjunto>.md      copy aprovada, na raiz do conjunto
        ├── _registro-composicoes.tsv
        ├── README.md               opcional, mapa do conjunto
        ├── <estilo-1>/
        │   ├── feed/               1080×1350
        │   └── stories/            1080×1920
        └── <estilo-2>/
            ├── feed/
            └── stories/
```

Os quatro níveis, nesta ordem: **produto → conjunto → estilo → formato.**

| Nível | Regra |
|---|---|
| **Conjunto** | `YYYY-MM-DD-tema`. A data é a da produção, não a da campanha |
| **Estilo** | sempre existe, mesmo quando o conjunto tem um estilo só. Nome descritivo, não `linha-B` sozinho |
| **Formato** | `feed/` e `stories/` sempre, mesmo que uma das duas ainda esteja vazia |
| **Raiz do conjunto** | só copy, registro de composições e README. Nenhum PNG solto |
| **Trabalho intermediário** | pasta com prefixo `_`, e nada dentro dela entra na entrega |

Nome de arquivo: `<produto>-<NN>-<slug-da-head>.png`. Ex.: `flp-07-perfil-vazio.png`.

**Peça solta na raiz de `criativos/` é defeito.** Se apareceu uma, ela pertence a algum conjunto: descubra qual e mova, ou crie o conjunto.

**Imagem de anúncio nunca entra no Git.** Regra do usuário, 2026-08-26. O `.gitignore` bloqueia `png`, `jpg`, `webp`, `gif`, `mp4` e `mov` dentro de `produtos/`, `outputs/` e `briefs/`. As peças vivem no disco e no Magnific.

O que sobe de um conjunto é o texto que explica a peça: copy aprovada, `_registro-composicoes.tsv`, README e a árvore de pastas, preservada por um `.gitkeep` em cada `feed/` e `stories/`. Quem clonar o repositório recebe o mapa completo do conjunto e nenhuma imagem.

Única exceção: `.claude/skills/ref-ads-dna/references/images/`, o board de referência de 2,7 MB. É material de skill, não criativo de campanha.

### Copy aprovada pelo usuário antes de qualquer imagem — regra dura

Acrescentada em 2026-08-26, depois de cerca de 6.000 créditos gastos em peças refeitas três vezes porque a imagem saiu antes de a copy estar fechada.

**Nenhuma imagem é gerada antes de o usuário aprovar a copy por escrito.** É etapa bloqueante, não recomendação. Vale para peça única, lote, teste de estilo, piloto e regeração.

A sequência, sem atalho:

| Ordem | O que acontece | Quem libera |
|---|---|---|
| 1 | A copy sai do agente `copywriter-light`, pela skill `/light-copy` | o agente |
| 2 | **A copy inteira do conjunto é gravada em um arquivo** | o agente |
| 3 | O validador roda nesse arquivo e sai com código 0 | `validar-copy.py` |
| 4 | O caminho do arquivo é **entregue ao usuário** e o trabalho **para** | — |
| 5 | O usuário lê o arquivo e responde aprovando | **só o usuário** |
| 6 | Aí sim gera imagem | — |

**O que não conta como aprovação:**

- Apresentar a copy e começar a gerar na mesma passada
- Silêncio, ou o usuário responder sobre outro assunto
- Aprovação de um lote anterior, ou de outra versão da mesma copy
- O usuário ter pedido "faz os 30 anúncios" no começo da conversa. O pedido autoriza o trabalho, não pula a conferência da copy
- Aprovação de piloto valendo para o lote inteiro. Piloto aprovado libera o piloto

**Quando a copy muda depois de aprovada, a aprovação cai.** Head reescrita, CTA trocado, eixo novo, público novo: reescreve o arquivo, roda o validador de novo e devolve o caminho. Aprovação é da versão, não do arquivo.

**Se o usuário disser para pular esta etapa**, ele pode. É a verba dele. Registre que foi decisão dele e siga.

### A copy do conjunto vira arquivo, sempre

Regra do usuário, 2026-08-26. **Toda copy nasce como arquivo, nunca como texto solto no chat.** O usuário aprova lendo o arquivo, não rolando a conversa.

Um arquivo por conjunto, com **todos** os anúncios dele. Vinte anúncios de captação viram um arquivo com os vinte, não vinte arquivos nem uma amostra de três.

**Onde:** na raiz do conjunto, seguindo a convenção de pastas.

```
produtos/<slug>/criativos/<YYYY-MM-DD-tema>/copy-<YYYY-MM-DD-tema>.md
```

Se a pasta do conjunto ainda não existe, crie a árvore antes. O arquivo de copy é a primeira coisa que entra nela.

**O que vai dentro,** por anúncio. Só isto, nada além:

| Campo | O que é |
|---|---|
| **HEAD** | a copy que vai grande no card |
| **SUBHEAD** | a copy de apoio, logo abaixo |
| **CTA** | a chamada, na forma exata da campanha |
| tipo da Mandala | uma linha, no título do bloco. Serve para garantir variedade de ângulo |
| **CENA** | o que a imagem mostra. Não é copy, é o briefing do gerador de imagem, e sai da própria Head |

**Legenda do Meta, headline e descrição do Meta não entram.** Decisão do usuário, 2026-08-26: o arquivo é a copy do card, e só. Se um dia a campanha precisar do texto do post, ele vira um arquivo próprio.

No topo do arquivo, um cabeçalho curto: produto, data, fase do funil, formato, público e eixo da campanha. É o que deixa a leitura rápida.

**Como entregar ao usuário.** Uma mensagem curta com três coisas, nesta ordem:

1. **O caminho do arquivo**, como link clicável, para ele abrir e ler
2. Quantos anúncios tem e qual é o eixo, em uma linha
3. O resultado do validador

Depois disso, **pare**. Nada de colar os vinte anúncios no chat, nada de começar a gerar imagem, nada de perguntar "posso seguir?" no meio de um relatório.

**Quando a copy é corrigida, o arquivo é o mesmo.** Edite o arquivo existente e avise que ele mudou. Arquivo `-v2`, `-final`, `-revisado` só polui a pasta. Versão anterior que valha a pena guardar vai para uma pasta `_` de trabalho.

### Validar a copy antes de gerar imagem — regra dura

Acrescentada em 2026-08-26, depois de gerar 40 peças com copy que voltou.

**Nenhuma imagem é gerada antes de a copy passar no validador.** Crédito gasto em peça com copy errada não volta.

```bash
python3 .claude/skills/anuncio-flp/scripts/validar-copy.py <arquivo-de-copy.md>
```

O script mede, por anúncio, e reprova com código de saída 1:

| O que mede | Limite |
|---|---|
| **Volume de texto** | HEAD até 58 caracteres, SUBHEAD até 165, soma até 210 |
| **Repetição entre ADs** | HEADs com 62% ou mais de similaridade reprovam |
| **Frase reaproveitada** | sequência de 4 palavras repetida em 3 ou mais anúncios vira alerta |
| **Entrega da mensagem** | SUBHEAD que não diz o que a pessoa ganha reprova |
| **Vícios de Light Copy** | travessão, exclamação, HEAD em forma de pergunta, emoji |
| **CTA** | precisa bater com a forma exata da campanha |

Os limites saem da peça de 1080 de largura: HEAD roda em display condensado de 88 a 120 px, o que dá cerca de 22 caracteres por linha com teto de três linhas; SUBHEAD roda de 46 a 56 px, cerca de 50 caracteres por linha, mesmo teto. Texto acima disso não é escolha estética, é peça que o lead não lê no feed.

**Saiu 1, não gere.** Corrija a copy, rode de novo, e só então gaste crédito.

### Tom da imagem e da copy — regra dura

Acrescentada em 2026-08-26, depois de três peças reprovadas de uma vez.

**Toda peça comunica algo positivo, construtivo e bem-humorado.** Nada pode parecer enganação, golpe, esquema de enriquecimento rápido ou promessa furada. Vale igualmente para a imagem e para a copy.

**Metáforas proibidas, sem exceção:**

| Proibido | Por quê |
|---|---|
| Pessoas entrando em máquina, moedor, esteira, funil ou triturador | desumaniza o público, e o público é o cliente |
| Maço de dinheiro sendo contado na mão | cara de esquema, não de negócio |
| Cofre transbordando, mala de dinheiro, chuva de cédulas, pilha de notas | linguagem de golpe financeiro |
| Cédula estrangeira, dólar | o público é brasileiro, e dólar reforça a estética de esquema |
| Cassino, roleta, dado, bilhete premiado | vender negócio como aposta |
| Tom noir, sombrio, ameaçador, terror, tensão | o produto é sobre construir, não sobre medo |
| Pessoa isolada e derrotada como metade "errada" de uma comparação | humilha quem a peça quer converter |

**O que colocar no lugar.** A referência é o próprio anúncio real do cliente, em que os dois aparecem numa oficina, sorrindo, com um laptop na bancada: gente construindo alguma coisa, com bom humor e leveza.

- Construção e oficina: bancada, ferramenta, marcenaria, algo sendo montado a quatro mãos
- Conquista cotidiana e comemoração simples, sem ostentação
- Objeto do dia a dia numa situação absurda porém gentil, que é onde mora o humor da charge
- Sala cheia e animada, fila alegre na porta de um evento, plateia que ri
- Crescimento como broto, planta, construção que sobe, mapa sendo desenhado

**Como representar faturamento sem parecer golpe.** Nunca pela imagem do dinheiro em si. Use o efeito dele: a agenda que enche, a sala que lota, o negócio que fica pronto, o produto que sai da bancada, a comemoração de quem conseguiu. Se precisar de um símbolo de venda, prefira o comprovante discreto, a notificação no celular ou o aperto de mão.

**Na charge, o humor é gentil.** O absurdo é da situação, nunca à custa de uma pessoa. Ninguém é ridicularizado, ninguém é vítima, ninguém apanha.

### Mudança de proporção — regra dura

Acrescentada em 2026-08-26. **Nunca estique, replique ou espelhe pixel de borda para mudar a proporção de uma peça.** Isso produz listras visíveis na lateral e denuncia a montagem.

Espaço novo se preenche com **preenchimento generativo por IA**, sempre:

```
images_expand(creationIdentifier, aspectRatio, prompt)
```

Proporções que a tool aceita: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`, `21:9`. Ela **não** aceita 4:5.

| Destino | Caminho |
|---|---|
| **Feed 1080×1350 (4:5)** | gere em `3:4`, expanda para `1:1` com IA, recorte as laterais até 4:5. O conteúdo original fica inteiro e as bordas novas são geradas. |
| **Stories 1080×1920 (9:16)** | **use a peça de Feed como base e expanda para `9:16`.** Não gere a arte de novo do zero: sai mais barato, e o par Feed/Stories fica visualmente idêntico, que é o que a campanha precisa. |

No `prompt` do expand, descreva a continuação da cena, não a peça inteira. Exemplo: "continuação do papel creme com a mesma textura de jornal" ou "continuação da parede da sala, mesma luz".

`images_crop` corta sem gerar pixel, e serve para o ajuste fino depois do expand. Esticar em software de imagem está proibido.

### Estrutura e técnica nunca se repetem — regra dura

Acrescentada em 2026-08-26, depois de um lote inteiro de 20 anúncios voltar por ter a mesma composição.

**Trocar conteúdo não é trocar composição.** Cena diferente, copy diferente e cor de fundo diferente **não** compensam estrutura idêntica. Foi exatamente esse o erro: 20 peças com a mesma divisão horizontal, a mesma ordem de blocos e a mesma técnica.

Toda peça declara quatro atributos, e nenhuma combinação se repete no conjunto:

| Atributo | O que varia |
|---|---|
| **Estrutura** | onde o texto vive e como o quadro se divide. Vinte opções listadas em `/anuncio-flp` |
| **Técnica de ilustração** | charge, HQ, caricatura 3D, flyer, pop art, colagem, cartaz vintage, vetorial, fotorrealismo, isométrico |
| **Enquadramento** | plano médio, close extremo, plano geral, cenital, contra-plongée, escala impossível |
| **Paleta dominante** | qual cor governa o quadro |

Limites que reprovam o lote:

- duas peças **vizinhas** com a mesma estrutura ou a mesma técnica
- uma estrutura em mais de **20%** do lote
- uma técnica em mais de **25%** do lote
- menos de **seis técnicas distintas** num lote de 12 ou mais

**Uma peça aprovada não é um template.** O que se herda dela é o nível de acabamento, a paleta e o tom. A estrutura e a técnica se reinventam a cada peça.

O agente `auditor-originalidade` aprova o plano antes da geração e audita o lote depois, mantendo `_registro-composicoes.tsv` na pasta do conjunto.

### Originalidade — regra dura

**Todo anúncio é original e feito do zero.** Proibido reaproveitar layout, estrutura ou sequência de blocos de peça anterior, de outro nicho ou de outra conversa.

Sinais de que virou template: mesma sequência vertical da peça anterior; card de vidro com 3 bullets; pill de chapéu no topo mais barra de rodapé com CTA centralizado; composição resolvida como "texto de um lado, foto do outro".

**Arquétipo validado não é gabarito.** O `/anuncio-spp` tem arquétipos com parâmetros medidos, e eles existem para calibrar decisão, não para ser copiados. O que se herda é o **sistema** — pisos de tamanho, contraste, respiro, escurecimento de duas paradas, camadas isoladas, Quadro e Decorado. O que se reinventa a cada peça é a **abordagem**: nicho, categoria do board, objeto na cena, composição, onde mora a informação de serviço e o desenho da headline. Peça nova ao lado da anterior com a mesma sequência vertical de blocos é template, e volta.

O layout nasce da **cena e da ideia** — tipografia integrada à imagem, recortes, sobreposições, escala dramática, elementos invadindo uns aos outros. Referência de padrão: flyers publicitários, não posts de template.

### A imagem decide onde o texto vai — regra dura

Acrescentada em 2026-08-05, depois de três peças reprovadas de uma vez.

**O texto não tem posição padrão.** Nem topo, nem base, nem centralizado por hábito. A posição sai da imagem, e se descobre **medindo antes de escrever a primeira letra**:

```bash
./venv/bin/python .claude/skills/anuncio-spp/scripts/analise-composicao.py imagem.png
```

O script devolve o centro de massa do assunto, o lado do **contrapeso** e o ranking de zonas livres. Assunto no terço direito → texto à esquerda. Assunto no terço esquerdo → texto à direita. Assunto centralizado → texto acima ou abaixo, nunca ao lado. Assunto na base → texto no topo.

**A foto se ajusta ao texto, não o contrário.** Se o assunto invade a zona escolhida, mova a foto por `imageTransform` em CROP, escale até 1,25× ou expanda no Magnific. Empurrar o texto para a sobra é o defeito.

**Contraste se mede no pior caso, nunca na média.** Amostre o fundo em três níveis (p10, p50, p90) e valha o menor: 4,5:1 para corpo, 3:1 para texto grande, **7:1 quando o desvio do fundo passa de 0,08**. Saturação não é contraste — acento quente sobre cena quente é o caso mais perigoso, porque engana quem desenha a 100 % de zoom e o lead vê a 37 %.

Boas práticas completas de design editorial — contrapeso, eixo de alinhamento, escada de respiro, alinhamento ótico, enquadramento e medida de linha — em `.claude/skills/anuncio-spp/references/design-editorial.md`.

### A composição sai da copy — regra dura

**A ideia manda na cena.** Enquadramento, ponto de vista, escala e o que entra no quadro saem do que a headline diz. Copy de comparação pede duas coisas no quadro; copy de escala pede vazio; copy de rotina pede desordem real; copy de virada pede movimento.

**O texto encontra lugar na cena que a ideia produziu, e não o contrário.** Zona homogênea existe naturalmente em quase toda fotografia: sombra profunda, céu, parede fora de foco, área desfocada pela profundidade de campo, massa escura de um objeto grande. Procure onde já existe.

**Proibido pedir superfície na cena só para segurar tipografia.** Mesa, bancada, tampo ou parede lisa ocupando a faixa do texto é vício de composição, reprovado em 2026-08-04, e produz peças que se repetem. Se a mesma solução aparece em duas peças seguidas da campanha, é template.

**Halo claro atrás de texto escuro está proibido** — deixa a imagem com aparência falsa. O único auxílio de contraste permitido é o degradê de duas paradas na matiz da cena.

### Distinção visual entre anúncios — regra dura, exigência de campanha

**Anúncios da mesma campanha precisam parecer visualmente diferentes uns dos outros.** Não é preferência estética: é exigência do tipo de campanha **Andromeda do Meta Ads**, que pede variedade visual real entre os criativos do conjunto. Peça nova que "lembra" a anterior desperdiça verba e volta.

Trocar o nicho, a copy e o objeto **não basta** — foi exatamente o erro cometido em 2026-08-03, quando duas peças de nichos diferentes saíram com a mesma temperatura de cor, o mesmo enquadramento e a mesma mesa no primeiro plano.

**Seis alavancas visuais. A peça nova muda pelo menos quatro:**

| Alavanca | Exemplos de extremos |
|---|---|
| **Paleta e temperatura** | quente âmbar ↔ frio azul-acinzentado ↔ neutro alto contraste |
| **Chave de luz** | low-key com queda para sombra ↔ high-key claro e arejado ↔ luz dura de sol |
| **Ângulo de câmera** | altura dos olhos ↔ contra-plongée baixa ↔ plongée de cima ↔ flat lay |
| **Tipografia** | Albert Sans ↔ Exo 2 ↔ Anton ↔ Manrope, e caixa alta ↔ caixa baixa |
| **Tratamento do texto** | branco sobre scrim escuro ↔ tinta escura com halo em fundo claro |
| **Direção de arte** | retrato fotográfico ↔ still-life ↔ comparação em duas metades ↔ humor ↔ tipografia protagonista |

**Como conferir, sem achismo:** exporte a peça nova e a anterior e compare **matiz média, luminância média e desvio da luminância**. Matiz a menos de 20° de distância somada a luminância média a menos de 0,05 de distância significa que as duas vão parecer irmãs no feed. Volte e mude de alavanca.

Registre no `outputs/` qual combinação já foi usada em cada peça da campanha, para a próxima não repetir.

### Leitura imediata — regra dura

**A peça precisa ser entendida em um segundo, sem a copy.** O feed é um ambiente de cegueira de banner: o usuário treinou o olho para desviar de qualquer coisa com estrutura de anúncio. Peça que exige decodificação já perdeu, porque ninguém para para decifrar charada.

Teste obrigatório antes de gerar: descreva a cena para alguém que não leu o briefing. Se a pessoa não disser **de quem é aquilo e o que está acontecendo** na primeira frase, a cena está errada e se resolve antes de gastar crédito. Metáfora não é proibida, mas precisa ler sozinha e na hora. Sacola plástica virando água-viva lê. Laje de concreto sobre maca de procedimento não lê.

O que atravessa a cegueira de banner, nessa ordem de eficácia:

1. **Rosto humano com emoção legível**, de preferência olhando para a câmera. É o interruptor mais confiável do padrão de desvio segundo a pesquisa de eye-tracking, e o olhar da pessoa ainda direciona a atenção de quem vê.
2. **Pessoa e cenário do nicho, reconhecíveis na hora.** Dermatologista tem que ver dermatologista, jaleco, maca, consultório. Símbolo abstrato não gera reconhecimento.
3. **Quebra de padrão dentro da cena.** Algo fora do lugar esperado, que faz o olho voltar depois de já ter passado.
4. **Hierarquia com foco único dominante.** Dois assuntos competindo viram ruído e o olho segue a rolagem.

Proibido: objeto solitário representando ideia abstrata, escala impossível usada como enigma, cena que só faz sentido depois de ler o headline.

**A imagem também precisa continuar legível.** Escurecimento global da cena está proibido, incluindo a vinheta radial no fill do frame que os originais do `/anuncio-spp` usavam. Ela mata o cenário que faz a peça ser reconhecida pelo nicho, e é esse reconhecimento que atravessa a cegueira de banner. O contraste do texto se resolve **localmente**, com scrim só na faixa onde o texto está. Se o texto cai numa área clara, inverta o texto para tinta escura com halo em vez de escurecer a foto.

**O trabalho pesado é da imagem, não do Figma.** Se o texto só lê com rampa complicada de degradê, o defeito está na foto. Peça no prompt uma chave que ilumina o assunto e **cai para a sombra em direção à base**, por gradiente contínuo de luz, deixando o terço inferior quase preto. O escurecimento no Figma é então um único degradê de **duas paradas**, a mesma cor de 0 % a 100 %. Rampa de três ou quatro paradas produz sombra dura e transição percebida.

**Todo escurecimento usa a matiz dominante da cena, nunca preto neutro ou frio.** Vale para sombra de texto, scrim, fill de barra de vidro e halo. Amostre a média de RGB da região, converta para HSV, guarde a matiz e derive: preto da cena com saturação × 1,35 e valor ≈ 0,055; halo claro com saturação × 0,45 e valor ≈ 0,99. Preto azulado sobre cena âmbar denuncia texto colado por cima. A receita completa está na seção 4 do `efeitos.md`.

### Mancha de texto — regra dura

Acrescentada em 2026-08-25, depois de a subhead sair estreita demais em duas peças seguidas.

**A subhead ocupa a mesma largura da head.** Não é sobre corpo de fonte, é sobre a **largura do bloco de texto**. Head com mancha larga e subhead com mancha curta embaixo deixa a peça desequilibrada, com um degrau visível no lado direito da coluna. As duas manchas terminam aproximadamente na mesma vertical.

**Proibido quebrar linha sem necessidade.** A linha só quebra quando a próxima palavra não cabe na largura da coluna. Quebra decorativa, quebra para "ficar bonitinho" e quebra herdada do jeito que o texto foi escrito no prompt são todas defeito. Se a subhead está quebrando cedo, o problema é a largura da caixa, não o texto.

**Como pedir no prompt de imagem:**

> The supporting paragraph must fill the SAME column width as the headline above it, with its lines running edge to edge of that column. Break a line only when the next word does not fit. Do not break lines early and do not leave a short ragged block under a wide headline.

**Como conferir antes de entregar.** Meça a caixa de cada bloco e compare a largura:

```
largura da subhead / largura da head  >=  0,90
```

Abaixo de 0,90 a peça volta. Vale para qualquer bloco de apoio sob um bloco maior, não só head e subhead.

### Produto digital na cena é mockup de verdade — regra dura

Acrescentada em 2026-08-25, depois de uma peça de UGC sair com a tela do notebook em placeholder cinza.

**Quando a cena mostra um produto digital, o produto existe.** Página de vendas, e-book, app, dashboard, curso: a tela mostra um **mockup real e específico**, com layout resolvido, cor, imagem e texto em PT-BR. Barra cinza de placeholder, lorem ipsum, retângulo vazio e "tela genérica de site" estão proibidos.

**O produto pertence a alguém da cena.** Se a peça mostra uma pessoa, o produto na tela é **o produto dela**, coerente com quem ela é e com o cenário. Mulher numa cozinha com caderno de anotações vende algo que combina com aquela cozinha, e a foto de capa da página é a dela. Produto anônimo na tela é a mesma falha da foto genérica de banco de imagem.

**O texto do mockup segue a regra de ouro 5.1:** é renderizado pelo modelo de imagem, em português do Brasil. Nunca sobreponha texto vetorial a uma tela fotografada.

**Como pedir no prompt:** descreva o mockup como uma peça de design de verdade, item por item — foto de capa, headline em PT-BR entre aspas, botão com o texto entre aspas, paleta. Mantenha as strings da tela curtas, para o modelo não errar a grafia enquanto renderiza também o texto do anúncio.

**O que conta como exceção:** elemento gráfico de fundo em peça ilustrada, quando ele é adereço de composição e não o produto sendo mostrado. Silhueta de página num colagem de quadrinho pode ser silhueta. Tela de notebook em primeiro plano numa foto, não.

### A cena do UGC vem da copy — regra dura

Acrescentada em 2026-08-25, depois de duas peças de UGC saírem com foto genérica.

**Foto de pessoa qualquer segurando celular não é UGC, é banco de imagem.** UGC funciona porque a cena parece um momento real de alguém que viveu aquilo que a copy diz. Se a foto podia ilustrar qualquer anúncio de qualquer nicho, ela está errada.

**A cena precisa mostrar o que a copy afirma.** Antes de escrever o prompt, responda: *que momento concreto essa headline descreve, e o que estaria visível nele?* O que aparece no quadro sai daí.

| Copy diz | A cena mostra |
|---|---|
| "sai com o lançamento no ar" | a página publicada na tela do notebook, virada para a câmera |
| "chega sem produto" | o caderno de rascunho de lado, a tela ainda em branco |
| "monta o anúncio em uma tarde" | o criativo aberto na tela, o celular com o preview do feed |
| "sem seguidor" | o painel de campanha, não o perfil de rede social |

**Objeto de cena carrega o contexto.** Notebook, tela, caderno, quadro, papel: é o objeto que amarra a foto à promessa. Pessoa sozinha olhando para a câmera, sem nada em volta que diga do que se trata, não passa.

**O texto dentro do objeto segue a regra de ouro 5.1:** ou é renderizado pelo modelo em PT-BR, ou não existe (barras e blocos de placeholder). Nunca texto vetorial fingindo estar na tela.

## Regras de ouro

0. **Rode `/figma-status` antes da primeira operação de Figma em cada sessão** — e sempre que uma chamada do Figma falhar. Confirma as três camadas: conector MCP (OAuth), token REST e plugin Desktop Bridge.
0.1. **Pergunte o link do arquivo de destino antes de criar qualquer coisa no Figma, sempre.** `/figma-destino`. Só a resposta do usuário nesta sessão vale — link antigo, memória e arquivo aberto no desktop não autorizam nada. Ver a regra dura acima.
1. **Antes de `use_figma`, carregue `/figma-use`.** Não é opcional — pular causa falhas difíceis de debugar. O mesmo vale para `create_new_file` (`/figma-create-new-file`), `generate_diagram` (`/figma-generate-diagram`) e `get_design_context` (`/figma-design-to-code`).
2. **Nunca invente identificadores do Magnific.** UUIDs, `identifier` e referências de pasta são para a próxima chamada de tool, não para o usuário. Ao falar com o usuário use nome, título e `webUrl`.
3. **Encadeamento imagem → Figma** usa o `identifier` da creation (ou a `url` de `creations_get`/`creations_wait`), **nunca** a `webUrl`.
4. **Todo trabalho começa por um brief.** Se o pedido veio solto, rode `/brief` antes de gastar créditos gerando imagem.
5. **Toda peça respeita o brand kit ativo** em `brand/`. Se não houver brand kit para o cliente/projeto, pergunte ou crie um antes de gerar.
5.1. **Copy antes de pixel, e duas trilhas de texto.** Peça com texto passa por `/copy-card` antes do `visual-generator`. A Head define o enquadramento da imagem, não o contrário.

O texto da peça se divide em duas trilhas que **nunca se misturam**:

- **Texto editável no Figma: só Head, SubHead e CTA.** É a copy do anúncio. Sempre vetor, sempre camada viva.
- **Texto que pertence a um objeto da cena** (tela de tablet ou celular, capa, placa, embalagem, jornal) é **renderizado pelo modelo de imagem, em português do Brasil**, ou simplesmente não existe. Nunca sobreponha texto vetorial a um objeto fotografado para fingir superfície: o Figma não tem perspectiva, textura nem interação de luz para isso ficar real, e o resultado denuncia a peça.

Consequência prática nos prompts: o `no text, no numbers, no readable characters, no logos` continua valendo para tudo, **exceto** quando a cena tem um objeto que precisa carregar texto. Nesse caso descreva exatamente o que a tela ou a capa mostra, em PT-BR, e feche com "no other text anywhere in the picture".
5.2. **Estilo vem do board, layout vem da cena.** `/ref-ads-dna` decide luz, paleta, textura, categoria e enquadramento da imagem — nunca a sequência de blocos da peça. Repetir o *sotaque* visual do board é o objetivo; repetir o *layout* é o defeito que a regra de originalidade proíbe. A regra de PT-BR daquela skill vale só para texto que faz parte da cena (placa, embalagem, jornal, UI simulada) ou para prompt que o usuário vai colar em outra IA — dentro do DesignSpace o texto continua sendo vetor no Figma, e o prompt de fundo continua terminando com `no text, no numbers, no readable characters, no logos`.
5.2.1. **Logo só quando pedido.** Não coloque lockup nem marca na peça por hábito. Se o usuário não pediu, a peça sai sem logo.
5.2.2. **Sombra de texto não é automática.** Meça antes: se o fundo sob o texto já entrega contraste, não existe sombra. Empilhar sombra sobre fundo escuro engorda a letra e suja a contraforma sem ganhar nada. A sombra é exceção para texto que precisa cair sobre região clara ou movimentada.
5.3. **Uma imagem, 1080×1350, com acabamento publicitário.** Toda geração de criativo entrega **uma única** peça, no formato de feed 4:5, gerada em `imagen-nano-banana-2` e entregue exatamente em 1080×1350. Nada de lote de variações para o usuário escolher. E o prompt sempre carrega o acabamento: luz direcionada de estúdio, color grading cinematográfico, bloom controlado nas altas luzes, partículas suspensas no facho, micro-contraste no assunto, grão sutil e vinheta leve. Peça de anúncio tem cara de campanha impressa, não de render cru. O bloco de termos pronto para colar está no agente `visual-generator`.
6. **Custo é real.** Use `simulate_cost` antes de lotes. Drafts em modelo barato, final em modelo caro — ver tabela abaixo.

---

## Modelos Magnific — quando usar cada um

| Slug | Nome | Use para | Tempo |
|---|---|---|---|
| `imagen-nano-banana-2` | **Nano Banana Pro** | **Default de criação, por decisão do usuário.** Toda peça final sai daqui: fotorrealismo, edição guiada por referência, produto, personagem, fidelidade de marca. | ~50s |
| `imagen-nano-banana-2-lite` | Nano Banana 2 Lite | Drafts, alto volume, iteração barata. Explore aqui antes de fechar no Pro. | ~9s |
| `seedream-5-pro` | Seedream 5 Pro | Alternativa de fotorrealismo. **Não aceita 4:5** e cai sozinho para 3:4. | ~51s |
| `recraft-v4-1` | Recraft v4.1 | Ilustração e tipografia, quando o resultado não é foto. | ~15s |
| `gpt-2` | GPT-2 | Texto legível, infográfico, diagrama, mockup de UI. Não-fotorrealista. | ~79s |

Fluxo de custo saudável: explore em `imagen-nano-banana-2-lite` → escolha a direção → feche o vencedor em `imagen-nano-banana-2` (Nano Banana Pro), passando o draft como referência de imagem.

**Cuidado com os nomes.** Nano Banana Pro é `imagen-nano-banana-2`. O slug `imagen-nano-banana-2-flash` é o Nano Banana 2 comum, não o Pro. Confirme com `images_models_list` em vez de deduzir pelo nome.

**Proporção.** O Pro aceita 4:5 e resolve o feed de 1080×1350 direto, sem corte. Ele também aceita `resolution` em 1k, 2k e 4k. O preview do Magnific volta quadrado mesmo quando o render respeita a proporção pedida, então confira o arquivo final e não a miniatura.

---

## Estrutura de pastas

```
DesignSpace/
├── brand/        # Brand kits por cliente/projeto (paleta, tipografia, tom visual, do/don't)
├── briefs/       # Briefs estruturados das tarefas (entrada de todo trabalho)
├── assets/       # Inputs locais: fotos, logos, referências enviadas pelo usuário
├── outputs/      # Registro de entregas: links Figma, creations, decisões
├── .env          # FIGMA_ACCESS_TOKEN — chmod 600, gitignored, nunca impresso
└── .claude/
    ├── agents/   # Agentes especializados
    ├── skills/   # Fluxos repetíveis
    ├── hooks/    # figma-destino.sh — a trava do destino no Figma
    ├── state/    # Destino ativo da sessão. Gitignored, apagado a cada sessão nova
    └── settings.json
```

Convenção de nome: `YYYY-MM-DD-cliente-tarefa`. Ex.: `briefs/2026-08-03-acme-lancamento-app.md`.

---

## Git — fluxo de branches

`main` é a branch padrão. **Nunca commite direto nela.** Toda alteração nasce na `pedro`, sobe para a `pedro`, e só depois vai para a `main`:

```bash
git add -A && git commit          # sempre na pedro
git push origin pedro
git checkout main && git merge --ff-only pedro && git push origin main
git checkout pedro                # volta, é onde o trabalho acontece
```

O merge é sempre `--ff-only`. Se ele recusar, as duas divergiram — alguém commitou na `main` direto. Pare e avise em vez de forçar.

Commit e push acontecem **quando o usuário pede**, não a cada alteração.

---

## Agentes

| Agente | Quando usar |
|---|---|
| `visual-generator` | Gerar, iterar e refinar imagens no Magnific. Cuida de prompt, modelo, referências e seleção. |
| `figma-builder` | Construir/editar dentro do Figma: telas, componentes, variantes, artes, tokens. |
| `brand-guardian` | Auditar uma peça contra o brand kit antes de entregar. |
| `figma-master` | Construção de alta fidelidade no Figma. Nunca economiza esforço; simples e genérico não é entregável. |
| `auditor-originalidade` | **Garante que nenhuma peça repita estrutura, técnica ou composição de outra.** Roda antes de gerar (aprovando o plano) e depois (auditando o lote). Obrigatório em qualquer conjunto com mais de uma peça. |
| `copywriter-light` | **Toda copy do projeto sai daqui.** Carrega a skill `/light-copy` (Manual da Copy, 12 proibições, 26 Elementos Literários, Mandala de Anúncios, revisora). Roda antes de qualquer geração de imagem, e a copy dele ainda precisa do aval do usuário antes de virar pixel. Nunca escreva copy no olho. |
| `analisador-criativo` | **Pente fino antes da entrega.** Audita copy e design com número medido: nicho, contexto, CTA, volume de texto, legibilidade, contraste, margens, densidade e zonas seguras de Stories/Reels. |

Lance agentes em paralelo quando os trabalhos forem independentes (ex.: gerar 3 direções visuais distintas).

---

## Skills

| Skill | Fluxo |
|---|---|
| `/figma-status` | Check das 3 camadas de conexão com o Figma. Rode antes de tocar em qualquer arquivo. |
| `/figma-destino` | **Pergunta e registra em qual arquivo a peça nasce.** Obrigatória antes de qualquer criação no Figma, em toda sessão. Um hook bloqueia a escrita até o destino estar registrado. |
| `/briefing-produto` | **Etapa 0 de tudo.** Extrai o briefing completo de uma LP ou do Figma — incluindo nicho, paleta, tipografia e logo em SVG. Salva em `produtos/<slug>/`. |
| `/anuncio-flp` | **Sistema de anúncios "Fórmula de Lançamento Pago"** — tom, vocabulário oficial, frases-âncora, CTA fixo e regras visuais extraídos dos anúncios reais do cliente. Obrigatória para qualquer peça desse produto. |
| `/anuncio-spp` | **Sistema de anúncios "Seu Produto Pronto com IA"** — grid, tokens, componentes, efeitos e relação copy↔cena, engenheirados dos 16 originais. Use para qualquer criativo dessa marca. |
| `/ref-ads-dna` | **DNA visual do board "Ref Ads"** (196 peças catalogadas). 12 categorias de abordagem criativa mais as regras transversais de luz, paleta, textura e formato. Complemento de estilo: roda antes de gerar imagem ou desenhar a cena, e não monta a peça sozinha. |
| `/design-replica` | Replicar um design de referência pixel a pixel. **Se o original existir no Figma, leia as propriedades reais em vez de inferir da imagem.** |
| `/brief` | Pedido solto → brief estruturado em `briefs/`. |
| `/light-copy` | **Fonte única do método de copy.** Pacote Light Copy completo (VTSD): Manual da Copy com 15 princípios e 20 vícios, as 12 proibições absolutas, os 26 Elementos Literários, a Mandala de Anúncios, a revisora anti AI slop e os formatos de página, anúncio, social e roteiro. O agente `copywriter-light` carrega esta skill antes de escrever qualquer palavra. |
| `/copy-anuncio` | Fluxo legado de pacote de anúncio para Meta e Google. O método vem do `/light-copy`; as `references/` desta skill são cópias antigas. |
| `/copy-card` | Variante enxuta: só Head + Subhead + CTA que vão **dentro** do card, por fase do funil. |
| `/moodboard` | Direção visual → grid de referências no Figma/FigJam. |
| `/ad-set` | Criativo aprovado → variações por formato/canal. |
| `/ui-screen` | Descrição de tela → tela montada no Figma com design system. |
| `/brand-kit` | Consolidar identidade em `brand/` + página de guidelines no Figma. |

---

## Plugin Desktop Bridge

`use_figma` executa JavaScript no contexto do arquivo Figma e depende do **plugin Figma Desktop Bridge rodando no app desktop**, com o arquivo alvo aberto e em foco.

Se as chamadas falharem ou travarem:
1. Confirme que o Figma **desktop** (não o navegador) está aberto no arquivo certo.
2. Confirme que o plugin bridge está rodando naquele arquivo.
3. Rode `whoami` para descartar problema de permissão/rate limit.

Não fique repetindo a mesma chamada — se falhar 2-3 vezes, avise o usuário e diga exatamente o que checar.
