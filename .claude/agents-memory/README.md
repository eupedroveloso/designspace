# Memória dos agentes

Contexto que sobrevive entre sessões. Existe porque o mesmo aprendizado estava sendo redescoberto a cada conversa: preferência de figurino, prompt que funcionou, armadilha do arquivo do Figma, cor de acento que o usuário reprovou.

## Dois níveis

| Nível | Caminho | Guarda |
|---|---|---|
| **Global** | `.claude/agents-memory/<agente>.md` | Vale para qualquer produto: preferência do usuário, padrão validado, armadilha de ferramenta |
| **Por produto** | `produtos/<slug>/agentes/<agente>.md` | Só daquele produto: decisões da campanha, o que já foi usado, o que foi reprovado ali |

O slug do produto vem de `produtos/.ativo`.

## Como o agente usa

**Passo 0 de toda execução**, antes de qualquer outra coisa: ler a memória global, ler `produtos/.ativo`, ler a memória do produto ativo. Arquivo que não existe simplesmente não existe, não é erro.

**Antes de encerrar:** anexar o que aprendeu. Aprendizado genérico vai para a global; decisão específica da campanha vai para a do produto.

## Formato de uma nota

Uma linha por aprendizado, com data absoluta na frente:

```markdown
- 2026-08-05 — Usuário reprovou halo claro atrás de texto escuro. Deixa a peça com cara falsa. Contraste se resolve com scrim local na matiz da cena.
```

## Regras

- **Nunca gravar token, chave, senha ou o conteúdo do `.env`.** Nem parcialmente.
- Data sempre absoluta em `YYYY-MM-DD`. Nada de "ontem" ou "semana passada".
- Máximo ~500 linhas por arquivo. No limite, consolide as notas antigas em vez de truncar.
- Registrar o que **muda decisão futura**. Log de execução não é memória.
- Se o usuário disser "ignore a memória", não carregue e não atualize nesta sessão.

## Relação com `outputs/`

Não se confundem. `outputs/` é o registro do que foi entregue, com data e link, e serve de histórico da campanha. A memória é o que o agente precisa **saber antes de começar** para não repetir erro. Combinação visual já usada mora nos dois: em `outputs/` como registro da peça, aqui como restrição para a próxima.
