---
name: figma-destino
description: Pergunta e registra em qual arquivo Figma a peça deve ser criada, antes de qualquer criação. Use SEMPRE antes da primeira operação de escrita no Figma em cada sessão — criar frame, montar criativo, tela, componente, moodboard, guidelines — e sempre que o hook avisar que o destino não está registrado. Roda depois de /figma-status e antes de figma-builder, figma-master ou qualquer skill que monte arquivo.
---

# Destino no Figma

**Nada nasce no Figma sem o usuário ter dito onde.** Não é conferência de rotina, é a primeira pergunta de toda tarefa que termina em arquivo.

Um hook `PreToolUse` bloqueia `use_figma`, `create_new_file`, `figma_execute` e todas as tools de escrita enquanto não houver destino registrado nesta sessão. O registro morre a cada sessão nova — sessão nova, pergunta nova.

---

## 1. Pergunte — e pergunte cedo

Antes de gastar crédito de imagem, antes de escrever copy, antes de abrir o Figma. A pergunta é uma só:

> **Em qual arquivo do Figma eu crio essa peça?** Me manda o link. Se tiver página e seção específicas, me diz também.

Use `AskUserQuestion` quando fizer sentido oferecer opções — por exemplo o arquivo da última entrega registrada em `outputs/` ao lado de "outro arquivo" e "criar arquivo novo". **Opção sugerida não é resposta dada:** só vale o que o usuário escolher agora.

### O que não conta como resposta

| Não vale | Por quê |
|---|---|
| Link de sessão anterior | Sessão passada não autoriza sessão atual |
| File key na memória ou no `CLAUDE.md` | Ponteiro é atalho de leitura, não permissão de escrita |
| Arquivo citado num `outputs/` antigo | Registro do que foi feito, não do que fazer agora |
| Arquivo aberto no Figma desktop | Coincidência de foco, não decisão |
| "Deve ser o mesmo de sempre" | Suposição sua |

Se o usuário responder "não sei" ou "onde você achar melhor": proponha um arquivo concreto com o nome e a pasta, e **espere ele confirmar**. Se ele quiser arquivo novo, ele decide nome e pasta — crie e registre o link depois.

## 2. Registre

```bash
.claude/hooks/figma-destino.sh set "<link>" --pagina "<página>" --secao "<seção>"
```

O script extrai o file key, confirma o nome do arquivo pela API REST e libera a trava. Se a API não confirmar o nome, o registro acontece mesmo assim, mas rode `/figma-status` antes de construir — token quebrado costuma aparecer aí primeiro.

Link inválido, de comentário ou de busca é recusado: peça a URL do arquivo.

Consultar o destino ativo a qualquer momento:

```bash
.claude/hooks/figma-destino.sh show
```

## 3. Confirme que o desktop está no arquivo certo

`use_figma` e `figma_execute` rodam **no arquivo em foco no Figma desktop**, não no link registrado. Registro certo com desktop em outro arquivo escreve no lugar errado sem avisar.

Antes da primeira escrita, cheque com `figma_list_open_files` ou `figma_get_status`, ou confirme com o usuário. Divergiu, pare e avise — não escreva "só para testar".

## 4. Passe adiante

Subagente não conversa com o usuário: `figma-builder`, `figma-master`, `/design-replica`, `/ui-screen`, `/moodboard`, `/brand-kit`, `/ad-set` e `/anuncio-spp` recebem o destino **no prompt**, já resolvido. Link, página e seção, explícitos. Agente que não recebeu destino devolve pedindo — não escolhe.

## 5. Anote na entrega

O `outputs/YYYY-MM-DD-cliente-tarefa.md` registra em qual arquivo, página e seção a peça nasceu. É o que permite oferecer o mesmo destino como opção na próxima sessão — como sugestão a confirmar, nunca como padrão automático.

---

## Quando o hook bloquear

A mensagem do bloqueio é literal: pare, pergunte, registre, repita a chamada. Não contorne por outra tool, não use a REST para escrever, não crie arquivo novo para destravar. O bloqueio é a regra funcionando.
