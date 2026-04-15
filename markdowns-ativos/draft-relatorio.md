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

---

## Decisões Aprovadas — Etapa 2 (Pipeline de Features)

### Etapa 2 - Estratégia de Encoding e Colapso de Categorias

* **Contexto:** 14 variáveis categóricas para transformar matematicamente (binárias, ternárias e multiclasse).
* **Decisão Final:** ✅ Mapeamento manual para binárias e ternárias que possuíam o valor "No internet/phone service" (colapsadas para 0, eliminando esparsidade sem perda de sinal). One-Hot Encoding (com `drop_first=True`) para as multiclasses reais (`InternetService` e `PaymentMethod`). O contrato (`Contract`) recebeu codificação ordinal devido à queda monotônica do churn observada na EDA.
* **Impacto Esperado:** Dataset limpo, compacto e livre da explosão dimensional de dummies puras, otimizado para a performance de algoritmos baseados em árvores e logística.

### Etapa 2 - Estratégia de Escalonamento

* **Contexto:** Dados numéricos como `TotalCharges`, `TicketMedio` e `tenure` variam em ordens de grandeza distintas. Escaloná-los na base pode gerar "data leakage".
* **Decisão Final:** ✅ Adiar o escalonamento. Os dados exportados não sofrem normalização ou padronização.
* **Impacto Esperado:** A responsabilidade de escalar features numéricas será inserida na pipeline do modelo no Scikit-Learn durante a Etapa 3. Garante que os testes no Streamlit não precisarão aplicar scalers manualmente à base enviada.

### Etapa 2 - Feature Engineering: Criando `NumServicos`

* **Contexto:** Após as transformações, havia espaço para derivar valor a partir do engajamento do cliente com o portfólio.
* **Decisão Final:** ✅ Criar a variável `NumServicos`, calculada pela soma das 8 flags binárias de serviços (Net e Telefone).
* **Impacto Esperado:** Captura linearmente o nível de "ancoragem" do cliente. Quanto maior a pontuação, maior o custo de mudança do cliente, fornecendo à modelagem uma representação clara da aderência aos produtos da operadora.

---

## Defesa Técnica da EDA — Insights de Negócio com Evidências

> Esta seção resume os achados da Etapa 1 em formato de storytelling, com evidências visuais e dados de suporte para a apresentação ao vivo.

### Quem é o "vilão" do Churn?

O perfil de maior risco de cancelamento é o **cliente de contrato mensal com fibra óptica e sem serviços de proteção**. Os dados comprovam:

| Feature | Categoria de Risco | Taxa de Churn | Média Global |
| --- | --- | --- | --- |
| Contract | Month-to-month | **42.7%** | 26.5% |
| InternetService | Fiber optic | **41.9%** | 26.5% |
| OnlineSecurity | No | **41.8%** | 26.5% |
| TechSupport | No | **41.6%** | 26.5% |
| PaymentMethod | Electronic check | **45.3%** | 26.5% |

Em contraste, contratos anuais (11.3%) e bianuais (2.8%) praticamente eliminam o churn. Pagamentos automáticos (cartão: 15.2%, transferência: 16.7%) também indicam maior fidelização.

![Taxa de Churn por Feature Categórica](../reports/figures/eda_categoricas_vs_churn.png)

### O Impacto do `tenure` (Tempo de Casa)

O `tenure` é a variável numérica com **maior correlação com Churn** (r = **-0.3522**, p < 10⁻²⁰⁵):

| Métrica | Churn = No | Churn = Yes |
| --- | --- | --- |
| Média de tenure (meses) | 37.6 | 18.0 |
| Mediana de tenure (meses) | 38 | **10** |
| Desvio padrão | 24.1 | 19.5 |

Clientes que cancelam têm mediana de **10 meses** — metade se vai antes de completar 1 ano. A distribuição KDE revela um pico massivo de churn nos primeiros 6 meses (a "janela de perigo") e estabilização após ~24 meses.

![Distribuição KDE das Variáveis Numéricas por Churn](../reports/figures/eda_kde_numericas.png)

![Boxplot das Variáveis Numéricas por Churn](../reports/figures/eda_numericas_vs_churn.png)

---

### Insight 1 — "O Combo Tóxico"

Um cliente com *contrato mensal + fibra óptica + sem suporte técnico + pagamento por electronic check* é um alvo quase certo de churn. Cada uma dessas 4 características individualmente já eleva a taxa acima da média (~26.5%), e combinadas representam o caso extremo.

**Dados de suporte:**

| Característica | Taxa de Churn Individual |
| --- | --- |
| Contract = Month-to-month | 42.7% |
| InternetService = Fiber optic | 41.9% |
| TechSupport = No | 41.6% |
| PaymentMethod = Electronic check | 45.3% |

**Evidência visual:** Os gráficos de taxa de churn por categórica mostram que todas essas categorias ultrapassam a linha tracejada (média global) por larga margem.

![Taxa de Churn por Feature Categórica](../reports/figures/eda_categoricas_vs_churn.png)

---

### Insight 2 — "Os Primeiros 6 Meses Decidem Tudo"

A maior concentração de cancelamentos acontece em clientes com menos de 6 meses de casa. A empresa precisa tratar esses clientes como em "UTI" — cada mês que passa sem cancelar reduz exponencialmente o risco.

**Dados de suporte:**

* Mediana de tenure para Churn=Yes: **10 meses**
* Mediana de tenure para Churn=No: **38 meses**
* Correlação ponto-bisserial tenure × Churn: **r = -0.3522** (p < 10⁻²⁰⁵)

**Implicação para o negócio:** Programas de retenção devem ser mais agressivos no primeiro semestre de contrato. Após ~24 meses, o risco de cancelamento se torna residual.

![Distribuição KDE — tenure por Churn](../reports/figures/eda_kde_numericas.png)

---

### Insight 3 — "O Paradoxo da Fibra Óptica"

O serviço mais premium (Fiber optic) tem a **maior taxa de cancelamento** (41.9%), enquanto DSL (19.0%) e sem internet (7.4%) retêm mais. Isso sugere uma **desconexão entre preço e valor percebido**.

**Dados de suporte:**

| Tipo de Internet | Taxa de Churn | MonthlyCharges Médio* |
| --- | --- | --- |
| Fiber optic | **41.9%** | ~$80-90 |
| DSL | 19.0% | ~$50-60 |
| No | 7.4% | ~$20 |

*Faixas estimadas a partir dos boxplots.

Clientes pagam mais caro por fibra, mas sem os serviços complementares (segurança online: 14.6% de churn com, 41.8% sem; suporte técnico: 15.2% com, 41.6% sem), a insatisfação dispara. O churn não é do serviço em si — é da falta de "ecossistema de valor" ao redor dele.

![Boxplot Numéricas vs Churn](../reports/figures/eda_numericas_vs_churn.png)

---

### Tabela de Correlações — Top 5 Features com Maior Impacto no Churn

#### Variáveis Categóricas (Cramér's V)

| Rank | Feature | Cramér's V | Interpretação |
| --- | --- | --- | --- |
| 1 | Contract | **0.4101** | Month-to-month dispara churn; contratos longos retêm |
| 2 | OnlineSecurity | **0.3474** | Ausência de segurança online eleva churn em ~3x |
| 3 | TechSupport | **0.3429** | Ausência de suporte técnico tem efeito similar |
| 4 | InternetService | **0.3225** | Fiber optic paradoxalmente lidera cancelamentos |
| 5 | PaymentMethod | **0.3034** | Electronic check concentra 45% de churn |

#### Variáveis Numéricas (Correlação Ponto-Bisserial)

| Feature | Correlação (r) | p-valor | Direção |
| --- | --- | --- | --- |
| tenure | **-0.3522** | 8.00e-205 | Mais tempo de casa → menos churn |
| TotalCharges | **-0.1995** | 4.88e-64 | Mais gasto acumulado → menos churn (correlação com tenure) |
| MonthlyCharges | **+0.1934** | 2.71e-60 | Cobranças mensais altas → mais churn |

![Ranking de Relevância das Features](../reports/figures/eda_ranking_features.png)

---

### Resumo da Varredura de Qualidade de Dados

Varredura sistêmica executada em **100% das colunas** (21 variáveis) para demonstrar rigor metodológico:

| Verificação | Resultado |
| --- | --- |
| NaN explícitos (`isnull`) | 0 |
| Nulos ocultos (espaços em branco) | 11 em `TotalCharges` (tenure=0) — tratados |
| Marcadores disfarçados (`?`, `NA`, `N/A`, `null`, `-`) | 0 |
| Valores negativos (todas as numéricas) | 0 |
| `SeniorCitizen` fora de {0, 1} | 0 |
| `tenure` acima de 10 anos | 0 (máx: 72 meses = 6 anos) |
| `MonthlyCharges` == 0 | 0 |
| Duplicatas de `customerID` | 0 |

**Conclusão:** Base limpa. Único tratamento aplicado: imputação de TotalCharges com 0 nos 11 registros com tenure=0.

![Heatmap de Correlação](../reports/figures/eda_heatmap_correlacao.png)

![Distribuição de Churn](../reports/figures/eda_churn_distribuicao.png)
