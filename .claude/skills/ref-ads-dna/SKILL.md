---
name: ref-ads-dna
description: Referência técnica de estilo visual extraída do board "Ref Ads" (Pinterest, 196 peças catalogadas) do usuário. Use esta skill SEMPRE que for gerar, planejar ou avaliar um criativo de anúncio (imagem estática, prompt para IA generativa, ou peça no Figma) e o usuário pedir para seguir "o estilo do meu board de referências", "a linha visual que eu já uso", "nossa identidade de anúncios" ou mencionar o board "Ref Ads". Esta skill é um COMPLEMENTO técnico — ela não gera o anúncio sozinha, ela fornece o DNA visual (composição, luz, paleta, textura, categorias) para a skill que efetivamente monta o anúncio (ex: a skill que gera anúncios no Figma, ou qualquer skill de criativo do ChatGPT). Contém 196 imagens de referência extraídas do board original em references/images/. No projeto DesignSpace é etapa obrigatória de todo anúncio — etapa 4 do fluxo do CLAUDE.md, entre a copy e o desenho do layout — mesmo quando o usuário não cita o board.
---

# Ref Ads — DNA Visual Técnico

Esta skill documenta a análise técnica completa de 196 peças salvas pelo usuário no board Pinterest **"Ref Ads"** (br.pinterest.com/eupedroveloso0141/ref-ads). O board funciona como o banco de referências visuais do usuário para criação de anúncios — mistura peças publicitárias profissionais reais (Aldi, WWF, McDonald's, FedEx, BMW, Dollar Shave Club, Colgate, Jack Daniels, Adidas, Coca-Cola, Ziploc, KitKat, Apple Pay), exemplos de prompts de IA generativa para criativos ("PROMPT" / cinematic 4D), e humor/memes visuais usados como inspiração de linguagem e timing de piada.

O objetivo desta skill é traduzir esse acervo em regras técnicas replicáveis, para que qualquer agente de geração de imagem (ChatGPT, Nano Banana Pro, Midjourney) ou de montagem em Figma consiga produzir peças novas que "pareçam tiradas do mesmo board".

## Regra obrigatória: todo texto na imagem é em PT-BR

> **Dentro do DesignSpace esta regra é condicional — leia a seção 4 antes de aplicá-la.** No pipeline daqui o texto do anúncio é vetor editável no Figma e o prompt de imagem termina em `no text, no numbers, no readable characters, no logos` (regra de ouro 5.1). A regra de PT-BR abaixo vale para texto que é *objeto da cena* (placa, embalagem, jornal, tela de celular) e para prompt que o usuário vai colar em outra IA.

Qualquer texto que aparecer DENTRO da imagem gerada — headline, CTA, legendas, elementos de UI simulados (notificação de celular, post de rede social, capa de jornal/revista, placa, embalagem de produto) — deve ser sempre escrito em **português do Brasil**, nunca em inglês, mesmo que o restante do prompt técnico (descrição de luz, câmera, textura etc.) esteja em inglês para melhor compreensão do modelo de IA. Ou seja: o prompt técnico pode ser em inglês, mas qualquer string de texto que o prompt manda a IA renderizar dentro da imagem deve vir entre aspas em PT-BR (ex: `a small sign that reads "SÓ HOJE"` em vez de `"TODAY ONLY"`). Se o usuário não especificar o copy exato, o agente deve inventar um headline/CTA curto em PT-BR coerente com a campanha, nunca deixar em inglês por padrão.

## Como usar

1. Quando o usuário pedir um anúncio "no estilo Ref Ads" (ou pedir apenas um anúncio sem especificar estilo, mas o contexto for a conta/projeto deste usuário), identifique qual das 12 categorias abaixo melhor serve o objetivo da campanha (ver "Mapa de categorias").
2. Puxe o **DNA técnico transversal** (seção 2) como base obrigatória de qualquer prompt ou spec de Figma — ele vale para praticamente todas as categorias.
3. Some as **regras específicas da categoria escolhida** (seção 3).
4. Se estiver gerando um prompt de texto para colar em uma IA de imagem, monte-o na ordem: [categoria/conceito] + [assunto e ação] + [DNA técnico: luz, lente, textura, paleta] + [enquadramento e formato] + [onde entra o texto/CTA, se houver].
5. Se estiver montando no Figma (via skill complementar), use o DNA técnico para decidir grid, hierarquia tipográfica, área de respiro para texto, e paleta de cores do frame — mesmo quando a imagem em si já vier pronta de uma IA.
6. Consulte `references/images/img_XXX.jpg` para exemplos visuais brutos por número — os números citados nas categorias abaixo apontam para arquivos específicos dessa pasta (ex: "img_047.jpg" = donkey lendo jornal no vaso).

---

## 1. Mapa de categorias (12 clusters identificados)

O board não é um estilo único — é uma biblioteca de 12 abordagens recorrentes. Escolha a categoria pelo objetivo do anúncio, não pelo gosto pessoal:

**A. Personificação animal / objeto (humor absurdo cotidiano)**
Animais ou objetos inanimados realizando uma atividade humana banal, com seriedade fotográfica total (nenhum wink pro espectador). Ex: burro lendo jornal sentado no vaso sanitário (img_047), cachorro dachshund lendo "Dog News" no vaso com óculos (img_015), caracol pilotando scooter na estrada (img_011), galinha pilotando moto com capacete e óculos KFC (img_013), formiga sendo observada com lupa gigante (img_020), ratinho tomando café dentro de uma xícara (img_140). Usar quando o objetivo é gerar compartilhamento orgânico / graça imediata sem precisar de copy.

**B. Metáfora física literal do conceito (still-life conceitual)**
O conceito abstrato da campanha (economia, poluição, tempo, medo, confiança) é transformado numa cena física única e fotografável, sem precisar de texto para explicar. Ex: sacola plástica transformando-se em água-viva no oceano (img_035), pasta de dente Colgate saindo como geleira no topo de uma montanha (img_170), cofre bancário aberto com dinheiro empilhado dentro (img_075), mala cheia de dinheiro sendo carregada dentro do porta-malas de um carro (img_082), ferro de passar sozinho no meio do deserto (img_172). Usar para campanhas institucionais, financeiras, de sustentabilidade — onde o produto é abstrato.

**C. Peça publicitária de marca real (copy + hero shot + logo)**
Estrutura clássica de anúncio impresso/digital: hero shot do produto ou cena-conceito ocupando 70-80% do frame, headline curta (3-8 palavras) na base ou topo, logo pequeno no canto. Ex: Aldi "porque 2 em cada 10 gatos não ligam" com gato + latas de ração (img_034), WWF "The Hidden Cost" com orangotango segurando colher de café (img_036), FedEx "Now you know which one came first" com galinha e ovo saindo da caixa (img_113), Dollar Shave Club "Your new stash" com barbeador dourado tipo bigode (img_119). Usar quando o anúncio precisa comunicar um benefício claro de produto com autoridade de marca estabelecida.

**D. Still de "filme de ação" hiper-realista (cinematic 4D / prompt de IA)**
Fotografia de still de cinema: pessoa em movimento extremo (caindo, correndo, voando, sendo arremessada), grão de imagem sutil, iluminação dramática de contraluz ou luz dura lateral, poeira/detritos suspensos no ar reforçando a sensação de movimento congelado. Muitos destes pins vêm rotulados literalmente "PROMPT" — são referências de como pedir esse estilo pra IA. Ex: homem pulando de prédio com detritos ao redor (img_106), grupo correndo em pânico numa selva/cidade (img_108, img_110), astronauta acorrentado caindo (img_089). Usar para campanhas de app, jogo, energético, ou qualquer marca que queira "impacto de trailer de filme".

**E. Editorial surreal / escala impossível (arte publicitária de autor)**
Composição de forte impacto visual fora do mundo normal: escalas trocadas, elementos fundidos, situação impossível tratada com estética de still fotográfico premium — cor controlada, iluminação de estúdio, pós-produção limpa. Ex: estátua clássica grega comendo pipoca (img_128 aproximado), mulher-estátua de gesso curvada sobre uma pedra (img_030), Estátua da Liberdade em chamas "American Story" (img_129), rosto composto por centenas de peças de quebra-cabeça (img_137). Esta é a categoria mais próxima da skill `criativo-surreal` já existente do usuário — use as duas em conjunto.

**F. Comparação / dualidade visual**
Duas metades, dois estados, ou dois personagens em contraste direto na mesma peça — usado pra comunicar antes/depois, certo/errado, ou escolha. Ex: leão sorrindo de um lado enquanto carro é destruído do outro (implícito na sequência de leões img_050), tubarão avançando sobre nadador em água escura (img_052, img_161), boneco de neve/gelo formando rosto assustador. Usar com a skill `jeito-certo-jeito-errado` já existente.

**G. Produto flutuante / em ação (still-life publicitário puro)**
Produto (celular, garrafa, cartão, embalagem) fotografado em movimento, explodindo em partes, ou flutuando contra fundo liso de estúdio — luz de still-life comercial, sombra suave no chão, sem cenário além do fundo colorido liso. Ex: cartão SIM saindo do celular (img_108), iPhone com apps voando ao redor (img_092), Apple Pay "Ding. Done." com celular pop-art (img_109), garrafa de perfume congelada em bloco de gelo no deserto (img_162). Usar para lançamento de produto físico, fintech, e-commerce.

**H. Personagem 3D estilizado tipo "toy" (render Pixar/claymation)**
Boneco 3D com proporções levemente caricatas, materiais macios (feltro, plástico fosco, massa de modelar), iluminação de estúdio 3D suave, usado pra dar simpatia/mascote a uma marca. Ex: personagem "Creative Force Kit" em blister de brinquedo (img_126), astronauta de feltro em cena aconchegante (img_143 aprox), bonequinho segurando bandeja de comida (img_079). Usar quando a marca quer tom lúdico/família, ou como avatar de campanha recorrente.

**I. UGC fotográfico amador (vida real, sem produção aparente)**
Foto que parece tirada com celular por uma pessoa comum, luz natural ou de ambiente doméstico, nenhuma composição "publicitária" visível, texto sobreposto estilo TikTok quando presente. Ex: mulher cozinhando com panela pegando fogo enquanto dança (img_025), gato tomando banho sozinho (img_058 aprox), "Baby Mama" com bebê no colo. Usar em conjunto com a skill `ugc-rotina-real` já existente do usuário.

**J. Tipografia + minimalismo corporativo**
Fundo liso ou textura sutil, uma palavra ou frase curta em destaque tipográfico máximo, pouquíssimos elementos gráficos de apoio. Ex: "CORPORATE" em letras garrafais sobre still de homem caindo (img_187), "PROFESSOR" em verde institucional (img_183), retrato dividido em blocos de cor sólida "Idol of my dreams" (img_141 aprox). Usar para campanhas B2B, institucionais, ou quando o texto É o criativo.

**K. Pôster de "filme"/série (key art)**
Estrutura de cartaz de cinema: título grande na base ou topo, personagem central em pose de força/tensão, tratamento de cor cinematográfico (teal & orange, monocromático, ou saturação alta). Ex: "Iron Man" pôster fake (img_153), "GLASS" M. Night Shyamalan style (img_160), "Kannur Squad" (img_127 aprox). Usar quando o anúncio quer emprestar a linguagem de "lançamento de blockbuster" para o produto.

**L. Still de terror/tensão controlada**
Elementos de horror/thriller (barbante, vendas, quartos escuros, texturas orgânicas incômodas) aplicados a um produto ou causa social para gerar desconforto proposital. Ex: rosto enfaixado com código de barras (img_178), boneco de barbante amarrado numa cadeira "FEAR MADE FUN" (img_169), "Worms make unwelcome guests" com verme saindo de fresta. Usar para campanhas de prevenção, seguros, ou pest control — nunca para produtos de consumo positivo.

---

## 2. DNA técnico transversal (aplica-se à maioria das categorias)

Estes atributos aparecem de forma consistente em praticamente todas as 196 peças analisadas, independente da categoria — são o "sotaque" visual do board inteiro:

**Fotorrealismo cinematográfico como padrão-ouro.** Mesmo peças 100% geradas por IA (as rotuladas "PROMPT") buscam ativamente esconder a origem sintética: grão de filme sutil, imperfeições de lente, profundidade de campo rasa (f/1.4–f/2.8 equivalente), leve vinheta nas bordas. Evitar aparência "renderizada limpa demais" ou "vetor plano" — a única exceção deliberada é a categoria H (toy 3D), onde o estilizado é o ponto.

**Iluminação dramática de contraluz ou luz dura lateral.** A maioria das peças usa uma fonte de luz principal forte e direcional (contraluz criando silhueta parcial, ou luz lateral dura criando sombra definida de um lado do rosto/objeto), quase nunca luz frontal chapada. Isso cria contraste alto e uma "leitura" imediata do assunto principal mesmo em thumbnail pequeno.

**Metáfora literal acima de metáfora abstrata.** A regra criativa do board inteiro: em vez de sugerir uma ideia com símbolos, o board resolve o conceito virando ele numa cena física concreta e fotografável (o "e se isso fosse real" — animal fazendo tarefa humana, dinheiro literalmente vazando, medo literalmente amarrado numa cadeira). Ao escrever prompts, sempre perguntar: "qual é a versão literal e fotografável dessa ideia abstrata?"

**Paleta restrita e intencional (2-3 cores dominantes por peça).** Raramente mais de três cores competem no frame. Um fundo neutro (preto, cinza-chumbo, bege, ou cor sólida saturada única) sustenta um ponto de cor de contraste no assunto principal ou no elemento de marca. Cores saturadas puras (vermelho BMW, amarelo Dollar Shave Club, azul Ziploc) são usadas como bloco sólido de fundo quando a marca quer memorabilidade instantânea; tons dessaturados/terrosos quando o objetivo é credibilidade/realismo (categorias B, D, E).

**Textura tátil hiper-detalhada no assunto principal.** Pele, pelo, metal escovado, gotas de água, poeira suspensa, fibras de tecido — o assunto principal quase sempre tem riqueza de microtextura visível mesmo a distância, enquanto o fundo é deliberadamente mais liso/desfocado para criar hierarquia de foco.

**Composição centrada com respiro generoso.** O assunto principal ocupa entre 40% e 70% do frame, raramente sangra até a borda sem intenção (exceção: still-life de produto em categoria G, que pode cortar agressivamente). Há quase sempre uma "zona de silêncio" — área de negativo espaço reservada — onde entraria headline/CTA, mesmo quando a peça de referência não tem texto.

**Formato vertical dominante (4:5 ou 9:16).** A esmagadora maioria das peças é vertical, otimizada para Stories e Feed mobile — raras exceções horizontais aparecem em contexto de apresentação/Behance (case studies), não em peças finais de anúncio.

**Tipografia, quando presente, é minimalista e curta — e sempre em PT-BR.** Quando há headline, ela tem entre 2 e 8 palavras, fonte sans-serif bold ou serif editorial (nunca script/decorativa), alto contraste com o fundo (branco sobre escuro, preto sobre claro), posicionada na base ou topo — nunca sobrepondo o rosto/foco principal do assunto. Logo, quando presente, é pequeno e desviado para um canto, nunca centralizado. Todo o texto renderizado dentro da imagem é sempre em português do Brasil (ver regra obrigatória no início desta skill) — nunca gerar headline, CTA ou UI simulada em inglês por padrão.

**Humor por justaposição, não por exagero.** Nas peças de humor (categoria A), o absurdo funciona porque tudo ao redor do elemento "errado" é tratado com seriedade fotográfica total — o animal não está sorrindo pra câmera, a cena não tem elementos cartoon extras. É a contenção do resto da cena que faz a piada funcionar.

---

## 3. Checklist técnico para gerar uma peça nova "estilo Ref Ads"

Ao montar um prompt de IA de imagem ou um brief para o Figma, confirmar que a peça nova responde a estas 7 perguntas (nessa ordem):

1. **Qual categoria (A–L) serve o objetivo desta campanha específica?**
2. **Qual é a versão física-literal do conceito, se a categoria for B, D ou E?**
3. **Qual fonte de luz principal e de que direção ela vem (contraluz / lateral dura)?**
4. **Quais são as 2-3 cores dominantes e qual delas carrega a marca?**
5. **Onde fica a zona de respiro para texto/CTA, o texto (se houver) tem no máximo 8 palavras, e está em português do Brasil?**
6. **O formato é vertical (4:5 ou 9:16), salvo justificativa contrária?**
7. **A textura do assunto principal está hiper-detalhada e o fundo está mais liso/desfocado por contraste?**

---

## 4. Integração com o DesignSpace

Esta skill não monta peça. Ela alimenta quem monta com decisões de estilo já tomadas, para que o Figma e o Magnific recebam specs concretas em vez de "faça bonito":

- Ao montar o frame no Figma, usar a paleta de 2-3 cores definida no passo 4 do checklist como as cores de fundo/destaque do componente.
- Reservar a "zona de silêncio" do passo 5 como a área de safe-zone de texto no grid do Figma.
- Se a imagem de fundo/hero vier de uma IA generativa, o prompt para essa IA deve ter sido montado seguindo a seção 2 (DNA técnico) antes de ser importado como asset no Figma.
- Ao escolher componente de tipografia no Figma, usar sans-serif bold ou serif editorial (nunca decorativa), conforme a regra de tipografia da seção 2.

### Onde ela entra no fluxo

É a **etapa 4** do fluxo obrigatório de criação de anúncio do `CLAUDE.md`: depois de `/briefing-produto`, da pesquisa de nicho e de `/copy-anuncio`, e antes de desenhar o layout. A copy já existe quando o DNA é carregado — a Head é que define qual categoria (A–L) e qual cena servem a campanha, nunca o contrário.

| Quem consome | O que tira daqui |
|---|---|
| `visual-generator` | Categoria, luz, paleta, textura e formato do prompt do Magnific. As miniaturas de `references/images/` servem de grounding — abrir 3-5 da categoria antes de descrever a cena. |
| `/anuncio-spp` | Só a **cena e o tratamento fotográfico**. Grid, tipografia, tokens e efeitos daquela marca continuam vindo da própria skill. Atenção à zona de respiro: ver a exceção abaixo. |
| `figma-master` / `figma-builder` | Paleta do frame, safe-zone do texto e escolha de família tipográfica. |
| `analisador-criativo` | O checklist da seção 3 vira o Eixo 3 da auditoria — sempre como AJUSTAR ou OBSERVAÇÃO, nunca como bloqueio. |
| `/design-replica`, `/moodboard` | Vocabulário para nomear o que está sendo replicado ou agrupado (categoria, direção de luz, tipo de paleta). |

### Prioridade de categorias, por causa da cegueira de banner

As 12 categorias da seção 1 não valem o mesmo neste projeto. O `CLAUDE.md` tem uma regra dura de leitura imediata: a peça precisa ser entendida em um segundo, sem a copy. Isso reordena o board.

**Primeira escolha, porque entregam reconhecimento imediato:** **I** (UGC fotográfico), **C** (marca com hero shot e cena reconhecível), **A** (personificação com humor), **F** (comparação), **J** (tipografia, quando o texto É o criativo). Todas colocam gente, cenário reconhecível ou um contraste óbvio na frente do espectador.

**Use com cuidado:** **B** (metáfora física literal), **E** (editorial surreal), **D** (still de ação), **G**, **H**, **K**, **L**. São as categorias mais bonitas do board e as que mais falham no feed, porque pedem decodificação. Só entram quando a metáfora lê sozinha e na hora, sem o headline. O critério é o próprio board: a sacola plástica virando água-viva (img_035) lê em um segundo; um objeto isolado representando um conceito abstrato, não.

**Regra de desempate.** Se a cena pode ser resolvida com uma pessoa do nicho em uma situação reconhecível, ela vence a versão simbólica da mesma ideia. Rosto humano com emoção legível e olhar para a câmera é o que a pesquisa de eye-tracking aponta como o interruptor mais confiável do desvio de olhar, e o olhar da pessoa ainda direciona a atenção de quem vê.

### Exceção de zona de respiro no sistema SPP

A seção 2 manda reservar o espaço negativo do texto no **topo** da peça, que é onde o board resolve a maioria das composições. O sistema `/anuncio-spp` faz o contrário: ancora o bloco de texto em y≈652 e a linha de CTA em y=956 de um canvas de 1080, ou seja, no **terço inferior**, e a peça se lê de baixo para cima.

Quando a peça for daquela marca, peça o respiro embaixo no prompt de imagem, com o assunto principal ocupando os dois terços de cima. Pedir respiro no topo por hábito produz uma imagem cuja área vazia cai justamente onde a cena deveria estar, e uma cena densa exatamente onde o texto vai entrar.

### Duas fronteiras que não se cruzam

**Estilo sim, layout não.** O `CLAUDE.md` proíbe reaproveitar layout, estrutura ou sequência de blocos de peça anterior. Esta skill não é exceção: dela vêm luz, paleta, textura, categoria e enquadramento — o *sotaque* visual. A sequência de blocos continua nascendo da cena e da ideia, peça a peça.

**Texto é vetor, não pixel.** No DesignSpace o headline e o CTA são camadas de texto no Figma, e o prompt de fundo termina em `no text, no numbers, no readable characters, no logos`. A regra de PT-BR do início desta skill se aplica em dois casos: quando o texto é objeto físico da cena (placa, embalagem, jornal, tela de celular, faixa) e quando o entregável é um prompt para o usuário colar em outra IA — aí toda string entre aspas vai em português.

As skills de criativo citadas na seção 1 (`criativo-surreal`, `jeito-certo-jeito-errado`, `ugc-rotina-real`, `pov`, `meme`) são do plugin do usuário e resolvem com o prefixo `anthropic-skills:` — elas geram texto para colar no ChatGPT, então nelas a regra de PT-BR vale integralmente.

---

## 5. Referências visuais brutas

A pasta `references/images/` contém 196 imagens (img_001.jpg a img_196.jpg) extraídas diretamente do board original em resolução de thumbnail (~178px de largura — suficiente para grounding visual de estilo, não para uso direto como asset final). Os números citados nas categorias da seção 1 apontam para arquivos específicos dessa pasta.

Se for necessário resolução maior de um pin específico para replicar fielmente uma composição, peça ao usuário o link direto do pin (formato `pinterest.com/pin/<id>/`) para reabrir e capturar em qualidade superior.
