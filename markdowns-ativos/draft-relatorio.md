# Relatório Técnico de Desenvolvimento e Trade-offs

Este documento consolida o histórico de decisões arquiteturais e analíticas para fins de auditoria e apresentação final.

---

## Decisões Aprovadas — Etapa 1 (EDA)

### Etapa 1 - Tratamento de Nulos em `TotalCharges`

* **Contexto:** 11 registros com `TotalCharges` em branco. Todos possuem `tenure=0` (clientes recém-chegados sem cobrança acumulada). São nulos semânticos, não erros de cadastro.
* **Alternativas Consideradas:**
  * (A) Imputar com 0 — Coerente semanticamente (sem tempo de vida = sem cobrança). Simples e interpretável.
  * (B) Remover as 11 linhas — Perda de 0.15% da base, mas elimina informação de perfil de clientes novíssimos.
* **Trade-off:** Opção A preserva todos os registros e é fiel à lógica de negócio. Opção B é mais conservadora, mas descarta informação de um segmento relevante (clientes recém-chegados).
* **Decisão Final:** ✅ Opção **A — Imputar com 0**. Aprovada pelo usuário.
* **Impacto Esperado:** Mantém integridade do dataset (7043 registros) e permite criação da feature derivada `TicketMedio`.

### Etapa 1 - Multicolinearidade e Criação de `TicketMedio`

* **Contexto:** `tenure` e `TotalCharges` possuem correlação de Pearson de ~0.83. Manter ambas introduz redundância e instabilidade nos coeficientes de modelos lineares.
* **Alternativas Consideradas:**
  * (A) Manter ambas — redundância no modelo, mas nenhuma perda de informação.
  * (B) Dropar `TotalCharges` e criar `TicketMedio = TotalCharges / tenure` — elimina colinearidade e gera feature com significado de negócio direto.
  * (C) Manter ambas + criar `TicketMedio` — decidir com seleção de features posterior.
* **Trade-off:** Opção B é mais limpa e interpretável. Opção C dá mais flexibilidade ao custo de manter variáveis correlacionadas. Opção A é a mais arriscada para modelos lineares.
* **Decisão Final:** ✅ Opção **B — Dropar `TotalCharges`, criar `TicketMedio`**. Aprovada pelo usuário.
* **Impacto Esperado:** Elimina multicolinearidade e adiciona feature com significado direto de negócio (gasto médio por mês de permanência).

### Etapa 1 - Estratégia de Balanceamento de Classes

* **Contexto:** Razão de desbalanceamento de 2.77:1 (73.5% No / 26.5% Yes). Moderado, mas capaz de enviesar modelos para a classe majoritária.
* **Alternativas Consideradas:**
  * (A) SMOTE no treino — Gera exemplos sintéticos da classe minoritária. Risco de data leakage se mal implementado.
  * (B) `class_weight='balanced'` — Penaliza erros na classe minoritária via pesos internos do modelo. Simples, sem alterar o dataset.
  * (C) Testar ambas abordagens e comparar.
* **Trade-off:** Opção B é mais segura e simples como baseline. SMOTE pode aumentar Recall mas introduz risco de overfitting em amostras sintéticas.
* **Decisão Final:** ✅ Opção **B — `class_weight='balanced'`** como baseline. Aprovada pelo usuário.
* **Impacto Esperado:** Decisão direta no Recall da classe 1 (SLA de ≥70%). Abordagem será aplicada na Etapa 3 (Modelagem).
