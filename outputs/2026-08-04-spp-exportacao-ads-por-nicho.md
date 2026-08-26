# SPP — exportação do banco de anúncios por nicho

**Data:** 2026-08-04
**Produto:** Seu Produto Pronto com IA
**Tipo:** extração de acervo (não é criação de peça nova)

## O que foi feito

Exportadas todas as peças da seção **`Export`** do Figma e organizadas em pastas por nicho.

- **Origem:** https://www.figma.com/design/npntxOrWtAEi5mRQcwRxl8/Seu-Produto-Pronto?node-id=2713-430 (seção `Export`)
- **Destino:** `produtos/seu-produto-pronto-com-ia/criativos/2026-08-04-ads-por-nicho/<nicho>/{feed,stories}/` *(era `criativos/ADS/<nicho>/` até 2026-08-26)*
- **Volume:** 132 PNG · 11 nichos · 324 MB
- **Método:** API REST do Figma, endpoint `/v1/images`, PNG escala 1×. O conector MCP e o plugin bridge não foram usados — render server-side não depende do desktop.

## Estrutura entregue

Matriz fechada: **11 nichos × 3 fases × 2 criativos × 2 formatos = 132**. Todo nicho tem exatamente 12 arquivos.

Nichos: advogado, arquiteto, dentista, educador-fisico, fisioterapeuta, infoprodutor, medico, nutricionista, professor, psicologo, veterinario.

Nome: `<topo|meio|fundo>-<01|02>-<feed|story>-<L>x<A>.png`. Feed é 1080×1350, story é 1080×1920. O mesmo `nn` nos dois formatos é a mesma peça. O mapa de qual conceito cada par representa está no `README.md` dentro da pasta ADS.

## Verificação

- Dimensão de todos os 132 arquivos confere com o nome.
- Nicho conferido visualmente nos 11 — cada peça tem o pill `TARJA profissao`.
- Fase de funil cruzada entre duas fontes independentes (linha da matriz e nomes de camada `fase-nn-conceito`): zero conflito.

## Atualização — 16h do mesmo dia

`dentista/fundo-01` (feed e story) re-exportado a partir do nó original `node-id=2325-536` (grupo Dentista → Fundo Funil), porque a arte ganhou a linha "POR APENAS R$97,00" às 15h58 e a cópia da seção `Export` ficou defasada.

**A seção `Export` guarda cópias achatadas, não as peças vivas** — editar a arte no grupo de nicho original não atualiza a cópia da `Export`. Varredura por camada nova confirmou que só esse par divergiu; o resto da pasta continua em dia.

A versão story dessa peça está em **letterbox**: arte 4:5 centralizada num canvas 9:16, com faixas cinza e texto pequeno demais para celular. Precisa de adaptação vertical de verdade antes de subir.

## Defeito encontrado no Figma, para corrigir

`educador-fisico/meio-01` (feed e story) tem o **pill errado na arte**: diz `PROFESSOR` numa peça de academia com copy de educador físico. A peça foi adaptada e o pill não acompanhou.

## Armadilhas do arquivo, para a próxima vez

- **A ordem das linhas de funil inverte no meio da seção.** Nas 7 primeiras colunas de nicho (advogado a fisioterapeuta) a matriz é topo → meio → fundo de cima para baixo. Nas 4 últimas (dentista, nutricionista, arquiteto, médico) é fundo → meio → topo. Assumir uma ordem só produz metade do acervo com a fase trocada — foi exatamente o erro da primeira tentativa desta exportação.
- **Bloco duplicado de nutricionista** dentro da própria seção `Export`, empilhado nas mesmas coordenadas. O de baixo tem 5 frames vazios, o de cima está completo. Vale apagar o incompleto.
- Nem toda peça tem camada viva: parte está achatada num único retângulo, e é o **nome desse retângulo** que carrega `fase-nn-conceito-formato`. Nas peças com camada viva, o nicho vem do TEXT chamado `TARJA profissao`. Usar as duas fontes juntas cobre o acervo inteiro.
- `get_metadata` do conector MCP estoura o parser de SSE nos nós grandes desse arquivo. A API REST com `depth` controlado resolve.
