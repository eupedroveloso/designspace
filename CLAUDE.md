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
3. **Rodar `/copy-anuncio`** — toda copy sai da skill (metodologia VTSD, Mandala de 18 Tipos). Nunca escrever copy no olho.
4. **Carregar `/ref-ads-dna`** — o DNA visual do board de referências do usuário. Escolher a categoria (A–L) que serve o objetivo da campanha e puxar o DNA transversal: direção da luz, paleta de 2-3 cores, textura do assunto principal, formato vertical e zona de respiro para o texto. Daqui sai a **cena e o tratamento fotográfico** — nunca um layout pronto. A escolha da categoria passa antes pela regra de leitura imediata abaixo: o DNA define o acabamento, e a legibilidade define a cena.
5. **Desenhar layout original a partir da cena.** Ver a regra de originalidade abaixo.
6. **Conferir contra o benchmark** do cliente e auditar com `analisador-criativo`.

Estrutura de produto:
```
produtos/<slug>/
├── briefing.md
├── identidade/  logo.svg · paleta.md · tipografia.md
└── criativos/
```

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
| `analisador-criativo` | **Pente fino antes da entrega.** Audita copy e design com número medido: nicho, contexto, CTA, volume de texto, legibilidade, contraste, margens, densidade e zonas seguras de Stories/Reels. |

Lance agentes em paralelo quando os trabalhos forem independentes (ex.: gerar 3 direções visuais distintas).

---

## Skills

| Skill | Fluxo |
|---|---|
| `/figma-status` | Check das 3 camadas de conexão com o Figma. Rode antes de tocar em qualquer arquivo. |
| `/figma-destino` | **Pergunta e registra em qual arquivo a peça nasce.** Obrigatória antes de qualquer criação no Figma, em toda sessão. Um hook bloqueia a escrita até o destino estar registrado. |
| `/briefing-produto` | **Etapa 0 de tudo.** Extrai o briefing completo de uma LP ou do Figma — incluindo nicho, paleta, tipografia e logo em SVG. Salva em `produtos/<slug>/`. |
| `/anuncio-spp` | **Sistema de anúncios "Seu Produto Pronto com IA"** — grid, tokens, componentes, efeitos e relação copy↔cena, engenheirados dos 16 originais. Use para qualquer criativo dessa marca. |
| `/ref-ads-dna` | **DNA visual do board "Ref Ads"** (196 peças catalogadas). 12 categorias de abordagem criativa mais as regras transversais de luz, paleta, textura e formato. Complemento de estilo: roda antes de gerar imagem ou desenhar a cena, e não monta a peça sozinha. |
| `/design-replica` | Replicar um design de referência pixel a pixel. **Se o original existir no Figma, leia as propriedades reais em vez de inferir da imagem.** |
| `/brief` | Pedido solto → brief estruturado em `briefs/`. |
| `/copy-anuncio` | **Obrigatória para toda copy de anúncio.** Metodologia VTSD, Mandala de 18 Tipos, Manual da Copy e checklist Light Copy. Roda antes do design. |
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
