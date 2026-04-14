---
trigger: manual
---

# Padrão de Atualização do Manual (README.md)

O `README.md` é a vitrine do projeto e o manual do avaliador. Ele atua como um registro de grandes marcos (milestones) e não como um log diário.

## Regras de Atualização

1. **Preservação de Estrutura:** Mantenha a espinha dorsal do documento intacta. Atualize pontualmente o "Status Atual", preencha o "Pipeline" e adicione novos resultados, sem destruir as seções existentes.

2. **Setup Rigoroso:** A seção de "Como Rodar" é inegociável e não deve ser alterada a menos que uma nova dependência de sistema seja adicionada. Ela deve sempre instruir o usuário a criar o ambiente virtual (`venv`), ativar o ambiente e instalar o `requirements.txt`.

3. **Estrutura de Blocos Obrigatória (Não remova nenhuma destas seções):**

   * **Visão Geral & Status:** O que o projeto resolve e a fase atual.

   * **O Dataset:** Fonte e descrição (fixo, não altere após definido).

   * **Pipeline e Metodologia:** Atualize as etapas com "[Concluído]" ou descrições breves conforme avançamos nas etapas do Plano.

   * **Como Reproduzir (Setup):** Comandos de terminal exatos.

   * **Resultados e Entregáveis:** Métricas finais do modelo preditivo e links para relatórios.

   * **Histórico de Marcos:** Resumo de alto nível (milestones) extraídos do `draft-relatorio.md`.
