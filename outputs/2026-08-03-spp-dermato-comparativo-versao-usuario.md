# Comparativo — minha versão × versão do usuário

**Data:** 2026-08-03
**Peças:** minha `2654:155` × ajustada pelo usuário `2654:849`, mesmo arquivo `Seu Produto Pronto`.

Tudo abaixo foi medido nos dois frames, não observado.

## Os seis deltas

| Item | Minha versão | Versão do usuário | O que aprendi |
|---|---|---|---|
| **Headline** | 2 corpos: "Sua agenda" 38 + "TEM TETO." 100, Medium + Black | **1 corpo: 100 px ExtraBold nas duas linhas**, entrelinha 89 (0,89 do corpo), "teto" em laranja | Palavra-chave curta não sustenta salto de escala |
| **Data** | empilhada no bloco, y 1078 | **topo do frame, y 16, 33 px Bold**, contraste 4,94:1 | Informação de serviço vai para área livre da imagem |
| **Quadro** | 1 linha de 38 em medida de 840 | **2 linhas de 38 em medida de 606** | Medida mais estreita, leitura mais fácil |
| **Respiro** | gaps de 4 a 12, improvisados | **22 px entre todos os grupos** | Ritmo único e repetido |
| **CTA** | 960 de largura, caixa alta, centralizado | **788 de largura, caixa baixa, alinhado à esquerda**, só "Saiba Mais" em peso alto, altura 136, padding 20/24 | Caixa alta cansa; faixa mais estreita dá hierarquia |
| **Notificações** | nenhuma (eu tinha removido por falta de espaço) | **3 em cascata**, 257×44, gap 51, opacidade decrescente, na área livre ao lado do corpo | Uma diz "vendeu"; três dizem "vende sem parar" |

Mais: imagem levemente reduzida para ganhar margem, e scrim de y661 até a base em 0→1,00.

## O erro de raiz que isso expõe

Passei três rodadas empurrando o corpo de "TETO." de 92 para 168 px tentando fazer a mancha da palavra-herói superar a da linha de cima, porque **minha própria regra mandava isso**. A regra estava incompleta: ela vale para o desenho de salto de escala, e "teto" tem 4 letras. Com palavra curta o desenho certo é outro — headline homogênea com hierarquia por cor.

Contraste da versão do usuário: data 4,94:1, headline branca 3,17:1, "teto" laranja 6,51:1, Quadro 11,59:1, CTA 17,69:1. Rodapé com L 0,0058 e desvio 0,0078, ou seja, foto viva.

## Correção de método na auditoria

Medi o Decorado em 2,32:1 e era artefato meu: numa linha que mistura branco e acento, um limiar único classifica os glifos laranja como fundo. O certo é medir cada trecho de cor separadamente. Já corrigido no `revisor-final`.

## Onde cada aprendizado foi gravado

- `regras-de-composicao.md` — os dois desenhos de headline e o critério de escolha pelos 6 caracteres; ritmo de 22 px; aproveitar área livre da imagem antes de espremer o texto; CTA em caixa baixa, largura 788, alinhado à esquerda.
- `vocabulario-visual.md` — cascata de 3 notificações, com parâmetros, e a permissão explícita de ela ficar abaixo do piso de tamanho por ser textura e não mensagem.
- `revisor-final.md` — identificar o desenho de headline antes de cobrar dominância de mancha; ritmo de 22 px; exceção de piso para objeto de contexto; e a armadilha de medir linha de duas cores.
