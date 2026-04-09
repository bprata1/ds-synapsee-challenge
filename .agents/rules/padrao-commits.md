---
trigger: model_decision
description: Sempre que acionar o Git para registrar alterações (comandos como git add, git commit ou git push), seja por exigência da regra "protocolo-copiloto", por pedido do usuário, ou por decisão autônoma. Siga obrigatoriamente as instruções deste arquivo
---

# Padrões de Versionamento (Trunk-Based Development)

O histórico do Git é a principal documentação da evolução lógica do projeto. A comunicação com o repositório deve ser transparente e semântica.

* **Frequência e Granularidade:** Realize *commits* frequentes e atômicos diretamente na branch `main`. Cada commit deve representar uma única unidade lógica de trabalho (ex: "Limpeza da coluna X" ao invés de "Tratamento de dados inteiro").
* **Mensagens Semânticas:** Utilize o padrão *Conventional Commits*. As mensagens devem explicar o **porquê** da alteração, não apenas o **que** foi feito.
  * *Exemplo de formato:* `tipo(escopo): descrição concisa`
  * *Tipos aceitos:* `feat` (nova análise/modelo), `fix` (correção de bug), `refactor` (melhoria de código), `docs` (documentação), `chore` (atualização de infraestrutura/requirements).
* **Idioma e Jargões:** A estrutura da mensagem deve ser em Português claro e direto. No entanto, é **altamente recomendado** o uso de jargões técnicos consolidados em inglês (ex: *baseline, outliers, merge, feature engineering, overfitting*) para manter a linguagem alinhada com o mercado de Data Science. O texto deve soar natural para um engenheiro de dados, priorizando a legibilidade e evitando traduções literais que tornem a leitura pedante.