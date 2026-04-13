---
trigger: model_decision
description: Acione obrigatoriamente esta regra de formatação ao executar o "Gatilho A" do protocolo-copiloto, para registrar a linha do tempo da manipulação de dados no arquivo logs.md.
---

# Padrão de Preenchimento: State Tracking (Logs)

O arquivo `markdowns-ativos/logs.md` é a fita de gravação (imutável) do projeto. Ele registra o "O QUÊ" e "QUANDO" aconteceu.

## Regras Estritas de Edição
1. **Append-Only:** Nunca apague ou altere um registro anterior. Insira novos blocos sempre ao final do arquivo.
2. **Concisão Extrema:** Não escreva prosa. Use estilo telegráfico.
3. **Estrutura Obrigatória do Bloco:**
   * **[AAAA-MM-DD HH:MM] - [Fase Atual / Ação Resumida]**
   * **Dataframe(s) Ativo(s):** `nome_do_df` | Shape: `(linhas, colunas)`
   * **Alteração:** O que foi criado, removido ou modificado (ex: "Dropadas 3 colunas de ID", "Criada feature X").
   * **Descrição:** Um texto muito breve explicando o porque da alteração para dar um contexto mínimo necessário a quem lê.