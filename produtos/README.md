Um diretório por produto, no formato `<slug>/`.

```
.ativo                   slug do produto ativo (uma linha, sem barra)
<slug>/
├── briefing.md          extraído da LP e/ou do Figma pela skill /briefing-produto
├── identidade/
│   ├── logo.svg
│   ├── paleta.md
│   └── tipografia.md
├── criativos/           registro das peças produzidas
└── agentes/             memória dos agentes neste produto (ver .claude/agents-memory/README.md)
```

Nenhuma copy e nenhum criativo começa sem o briefing do produto.

## Produto ativo

`.ativo` guarda o slug do produto corrente, numa linha só:

```
seu-produto-pronto-com-ia
```

Toda skill e todo agente lê esse arquivo antes de perguntar qualquer coisa, e usa `produtos/{ativo}/` como caminho base. Para trocar de produto, basta reescrever a linha.

Se o slug apontar para pasta inexistente, ou o arquivo não existir, o caminho é `/briefing-produto` — nunca inventar o contexto do produto.
