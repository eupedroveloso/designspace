# ADS — Seu Produto Pronto com IA · exportação por nicho

Exportado do Figma em **2026-08-04**, a partir da seção **`Export`** do arquivo `Seu-Produto-Pronto` — https://www.figma.com/design/npntxOrWtAEi5mRQcwRxl8/Seu-Produto-Pronto?node-id=2713-430

**132 PNG · 11 nichos · 324 MB.** Render em escala 1× pelo endpoint `/v1/images` da API REST do Figma: pixel exato do frame.

## Estrutura

A seção `Export` é uma matriz fechada e regular. Cada nicho entrega **12 arquivos**:

> 3 fases de funil × 2 criativos por fase × 2 formatos

- **Feed** — 1080×1350 (4:5)
- **Story** — 1080×1920 (9:16)

Os 11 nichos: advogado, arquiteto, dentista, educador-fisico, fisioterapeuta, infoprodutor, medico, nutricionista, professor, psicologo, veterinario.

## Nome do arquivo

```
<fase>-<nn>-<formato>-<largura>x<altura>.png
```

- **fase** — `topo`, `meio` ou `fundo`.
- **nn** — o criativo dentro da fase, `01` ou `02`. O mesmo `nn` em feed e em story é **a mesma peça nos dois formatos**, então dá para casar o par direto na hora de subir a campanha.
- **formato** — `feed` ou `story`.

Exemplo: `dentista/topo-01-feed-1080x1350.png` e `dentista/topo-01-story-1080x1920.png` são a mesma peça.

## Verificação feita

- **Dimensão** — os 132 arquivos batem com o tamanho declarado no nome.
- **Nicho** — cada peça carrega o pill `TARJA profissao` com o nome da profissão. Conferido visualmente nos 11 nichos.
- **Fase de funil** — deduzida pela linha da matriz e cruzada com os nomes de camada `fase-nn-conceito-formato` que sobraram das peças achatadas: **zero conflito** entre as duas fontes.

## Atualização de 2026-08-04, 16h

`dentista/fundo-01-feed` e `dentista/fundo-01-story` foram **re-exportados** a partir do nó original (`node-id=2325-536`, grupo Dentista → Fundo Funil), não da seção `Export`. A arte ganhou a linha **"POR APENAS R$97,00"** às 15h58, e a cópia que vive na seção `Export` ficou com a versão antiga.

Vale saber para as próximas: **a seção `Export` guarda cópias achatadas, não as peças vivas.** Quando a arte é editada no grupo de nicho original, a cópia da `Export` não acompanha. Uma varredura no arquivo confirmou que, fora esse par, nenhuma outra peça foi alterada depois da exportação — o resto da pasta está em dia.

## Pontos de atenção

**Story do `dentista/fundo-01` está em letterbox.** A imagem que entrou é a arte 4:5 centralizada dentro de uma tela 9:16, com faixas cinza em cima e embaixo, e não uma adaptação real para story. O texto fica pequeno demais para leitura em celular. Refazer a versão vertical antes de subir.

`educador-fisico/meio-01-feed` e `educador-fisico/meio-01-story` estão com o **pill errado na arte**: dizem `PROFESSOR`, mas a cena é academia e a copy é de educador físico ("Você ia levar seis meses pra montar seu produto digital sozinho"). O arquivo está na pasta certa — **o defeito é no Figma**, o pill não foi atualizado quando a peça foi adaptada. Corrigir no arquivo antes de subir essa peça.

## O que ficou de fora, e por quê

- Um **segundo bloco de nutricionista** empilhado exatamente sobre o primeiro, dentro da própria seção `Export`. Os dois têm as mesmas 12 posições; o de baixo tem **5 frames vazios** e o de cima está completo. Exportei o completo. O incompleto continua no arquivo e vale apagar.
- Tudo que está fora da seção `Export` — seção "97 Reais", peças de contagem regressiva, frames de exemplo de área segura, template base e a seção ADS Advantage.

## Mapa de conceitos

O que cada par representa, segundo o nome de camada que veio do Figma. Onde aparecem dois nomes, as camadas do feed e do story divergem entre si no arquivo original; onde aparece `—`, a peça não tem camada achatada com nome.

### advogado

| Arquivo | Conceito declarado no Figma |
|---|---|
| `topo-01-feed` + `topo-01-story` | — |
| `topo-02-feed` + `topo-02-story` | madrugada |
| `meio-01-feed` + `meio-01-story` | dois-caminhos |
| `meio-02-feed` + `meio-02-story` | tres-produtos |
| `fundo-01-feed` + `fundo-01-story` | adiantar-criar / custo-equipe |
| `fundo-02-feed` + `fundo-02-story` | prova-venda |

### arquiteto

| Arquivo | Conceito declarado no Figma |
|---|---|
| `topo-01-feed` + `topo-01-story` | oito-meses |
| `topo-02-feed` + `topo-02-story` | cliente-nao-volta |
| `meio-01-feed` + `meio-01-story` | nao-e-colega / obra-marcada |
| `meio-02-feed` + `meio-02-story` | ordem-decisoes |
| `fundo-01-feed` + `fundo-01-story` | trinta-horas |
| `fundo-02-feed` + `fundo-02-story` | guia-vira-projeto |

### dentista

| Arquivo | Conceito declarado no Figma |
|---|---|
| `topo-01-feed` + `topo-01-story` | teto-agenda |
| `topo-02-feed` + `topo-02-story` | sabado |
| `meio-01-feed` + `meio-01-story` | orientacao |
| `meio-02-feed` + `meio-02-story` | jeito-antigo / seu-protocolo |
| `fundo-01-feed` + `fundo-01-story` | custo-equipe |
| `fundo-02-feed` + `fundo-02-story` | clinica-fechada |

### educador-fisico

| Arquivo | Conceito declarado no Figma |
|---|---|
| `topo-01-feed` + `topo-01-story` | — |
| `topo-02-feed` + `topo-02-story` | desmarca |
| `meio-01-feed` + `meio-01-story` | — |
| `meio-02-feed` + `meio-02-story` | — |
| `fundo-01-feed` + `fundo-01-story` | tres-agendas |
| `fundo-02-feed` + `fundo-02-story` | descanso |

### fisioterapeuta

| Arquivo | Conceito declarado no Figma |
|---|---|
| `topo-01-feed` + `topo-01-story` | — |
| `topo-02-feed` + `topo-02-story` | — |
| `meio-01-feed` + `meio-01-story` | dois-dias |
| `meio-02-feed` + `meio-02-story` | tres-materiais |
| `fundo-01-feed` + `fundo-01-story` | tres-esperas |
| `fundo-02-feed` + `fundo-02-story` | troca-de-paciente |

### infoprodutor

| Arquivo | Conceito declarado no Figma |
|---|---|
| `topo-01-feed` + `topo-01-story` | — |
| `topo-02-feed` + `topo-02-story` | — |
| `meio-01-feed` + `meio-01-story` | — |
| `meio-02-feed` + `meio-02-story` | — |
| `fundo-01-feed` + `fundo-01-story` | — |
| `fundo-02-feed` + `fundo-02-story` | sexta-sabado |

### medico

| Arquivo | Conceito declarado no Figma |
|---|---|
| `topo-01-feed` + `topo-01-story` | dez-anos |
| `topo-02-feed` + `topo-02-story` | escala |
| `meio-01-feed` + `meio-01-story` | cfm |
| `meio-02-feed` + `meio-02-story` | macaneta |
| `fundo-01-feed` + `fundo-01-story` | plantao |
| `fundo-02-feed` + `fundo-02-story` | limite-fisico |

### nutricionista

| Arquivo | Conceito declarado no Figma |
|---|---|
| `topo-01-feed` + `topo-01-story` | base-igual |
| `topo-02-feed` + `topo-02-story` | domingo |
| `meio-01-feed` + `meio-01-story` | tres-produtos |
| `meio-02-feed` + `meio-02-story` | fora-da-consulta |
| `fundo-01-feed` + `fundo-01-story` | terceira-consulta |
| `fundo-02-feed` + `fundo-02-story` | sem-crn |

### professor

| Arquivo | Conceito declarado no Figma |
|---|---|
| `topo-01-feed` + `topo-01-story` | tabela-2040 |
| `topo-02-feed` + `topo-02-story` | domingo |
| `meio-01-feed` + `meio-01-story` | — |
| `meio-02-feed` + `meio-02-story` | tres-produtos |
| `fundo-01-feed` + `fundo-01-story` | — |
| `fundo-02-feed` + `fundo-02-story` | intervalo |

### psicologo

| Arquivo | Conceito declarado no Figma |
|---|---|
| `topo-01-feed` + `topo-01-story` | alta |
| `topo-02-feed` + `topo-02-story` | — |
| `meio-01-feed` + `meio-01-story` | — |
| `meio-02-feed` + `meio-02-story` | tres-materiais |
| `fundo-01-feed` + `fundo-01-story` | custo-equipe / organizar-criar |
| `fundo-02-feed` + `fundo-02-story` | entre-sessoes |

### veterinario

| Arquivo | Conceito declarado no Figma |
|---|---|
| `topo-01-feed` + `topo-01-story` | — |
| `topo-02-feed` + `topo-02-story` | whatsapp |
| `meio-01-feed` + `meio-01-story` | seis-meses |
| `meio-02-feed` + `meio-02-story` | tres-materiais |
| `fundo-01-feed` + `fundo-01-story` | — |
| `fundo-02-feed` + `fundo-02-story` | plantao |