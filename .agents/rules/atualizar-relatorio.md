---
trigger: model_decision
description: Acione obrigatoriamente esta regra de formatação ao executar o "Gatilho B" do protocolo-copiloto, para registrar os trade-offs e decisões técnicas no arquivo draft-relatorio.md
---

# Padrão de Redação: Relatório de Decisões e Trade-offs

O arquivo `markdowns-ativos/draft-relatorio.md` é a base da sua defesa técnica ao vivo. Ele deve documentar o raciocínio por trás das escolhas.

## Regras de Registro

1. **Foco no Raciocínio:** Não registre apenas o código; registre as alternativas que foram descartadas e o motivo da escolha atual.
2. **Formato Append-Only:** Adicione novos blocos ao final do arquivo, mantendo o histórico de evolução do projeto.
3. **Estrutura de Bloco Obrigatória:**
   * **### [Fase do Projeto] - [Título da Decisão]**
   * **Contexto:** Breve descrição do problema técnico.
   * **Alternativas Consideradas:** Liste pelo menos duas opções discutidas.
   * **Trade-off:** Prós e contras que levaram à escolha (ex: "A Regressão Logística foi escolhida em vez de Random Forest pela maior interpretabilidade dos coeficientes, apesar da acurácia 2% menor").
   * **Impacto Esperado:** Como isso afeta o resultado final ou os SLAs do projeto.
