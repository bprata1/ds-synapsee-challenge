# Desafio Técnico Data Scientist: Predição de Churn em Telecom

> **Visão Geral:** Este repositório contém o pipeline analítico ponta a ponta desenvolvido para o desafio técnico da Synapsee. O objetivo principal é prever a probabilidade de cancelamento de serviços (Churn) de clientes de telecomunicações, identificando perfis de risco e derivando um Score de Risco contínuo (0-100), culminando na entrega de uma aplicação interativa preditiva em Streamlit.

## 🚦 Status do Projeto

* **Fase atual:** ✅ Projeto finalizado. Todas as 5 etapas concluídas com sucesso. Interface de inferência operacional via Streamlit.

---

## 📊 O Dataset

* **Fonte:** [Telco Customer Churn — IBM/Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
* **Descrição:** 7.043 registros de clientes de uma operadora de telecom, com 21 variáveis (dados demográficos, serviços contratados, faturamento e tenure). Variável alvo: `Churn` (Yes/No), com desbalanceamento moderado de 2.77:1 (~73.5% No / 26.5% Yes).

## 🧠 Pipeline e Metodologia

1. **Análise Exploratória (EDA):** [Concluída] Varredura sistêmica de qualidade, ranking de features (Cramér's V + ponto-bisserial), detecção de multicolinearidade e mapeamento do perfil de churn. Notebook: `notebooks/01_eda.ipynb`. Figuras: `reports/figures/`.
2. **Feature Engineering:** [Concluída] Função unificada para produção contendo imputação, criação do `TicketMedio` e do `NumServicos` (índice de ancoragem), encoding cuidadoso (OHE e ordinal) minimizando esparsidade. Dataset 100% numérico processado salvo. Notebook: `notebooks/02_feature_engineering.ipynb`.
3. **Modelagem Preditiva:** [Concluída] Logistic Regression vs Random Forest. LR selecionada como campeã (Recall=78%, Macro F1=71%, Gap=1.5pp). RF descartada por overfitting (gap=18pp). Modelo salvo em `models/campeao.joblib`. Notebook: `notebooks/03_modelagem.ipynb`.
4. **Score de Risco e Inferência:** [Concluída] Transformação direta e monotônica de probabilidade em um Score de Risco (0-100) e segmentação em 3 Tiers (Baixo, Médio, Alto). Módulo `src/inference.py` padronizado. Notebook: `notebooks/04_score_risco.ipynb`.
5. **Aplicação (Deploy):** [Concluída] Dashboard interativo via Streamlit com upload de CSV, KPIs executivos, tabela de ação (fila de retenção filtrada por base ativa), filtro por Tier + download e seletor individual. Arquivo: `app.py`.

---

## ⚙️ Como Reproduzir (Setup Local)

Para garantir a reprodutibilidade do projeto e a correta versão das dependências, é **estritamente recomendado** o uso de um ambiente virtual.

1. **Clone o repositório e entre na pasta:**

   ```bash
   git clone <seu-repo>
   cd <pasta-do-repo>
   ```

2. **Crie o ambiente virtual:**

   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**
   * **Windows:** `venv\Scripts\activate`
   * **Linux/Mac:** `source venv/bin/activate`

4. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Execute a interface de inferência:**

   ```bash
   streamlit run app.py
   ```

   O app abrirá automaticamente em `http://localhost:8501`. Para testar, utilize o arquivo `data/raw/sample_upload_batch.csv` (50 clientes) fazendo upload no widget.

---

## 🛠️ Stack Tecnológico

| Categoria | Tecnologia |
| --- | --- |
| Linguagem | Python 3.12 |
| Manipulação de Dados | Pandas, NumPy |
| Modelagem | Scikit-learn (Logistic Regression, Pipeline, StandardScaler) |
| Visualização | Matplotlib, Seaborn |
| Serialização | Joblib |
| Interface Web | Streamlit |
| Notebooks | Jupyter (nbformat, nbconvert) |
| Versionamento | Git (commits semânticos) |

---

## 🏆 Resultados e Entregáveis

* **Modelo Campeão:** Logistic Regression (`C=0.01`, `solver=lbfgs`, `class_weight='balanced'`)
* **Métricas no Holdout (20%):**

| Métrica | Valor | SLA | Status |
| --- | --- | --- | --- |
| Recall (Churn) | **78.07%** | ≥ 70% | ✅ PASS |
| Macro F1-Score | **70.94%** | ≥ 70% | ✅ PASS |
| Gap Treino/Teste | **1.47pp** | ≤ 10pp | ✅ PASS |
| ROC-AUC | **0.8384** | — | — |

* **Segmentação (Score de Risco):**
  * **Baixo Risco (0-30):** 41.6% da base ~ Monitoramento Passivo
  * **Risco Médio (31-70):** 35.2% da base ~ Retenção Preventiva
  * **Alto Risco (71-100):** **23.3% da base (1.640 clientes)** ~ Ação Imediata

* **Relatório Técnico:** O detalhamento das decisões arquiteturais e trade-offs assumidos durante o desenvolvimento está documentado no arquivo `markdowns-ativos/draft-relatorio.md`.

---

## 📌 Histórico de Marcos (Milestones)

* **[2026-04-12]** Infraestrutura de versionamento, logs autônomos e registro de trade-offs arquitetada com sucesso.
* **[2026-04-14]** **Etapa 1 (EDA) concluída.** Varredura completa de qualidade de dados (zero anomalias além de 11 nulos semânticos em TotalCharges). Ranking de features por correlação e Cramér's V. Três decisões estruturais aprovadas: (1) imputação de TotalCharges com 0, (2) criação de `TicketMedio` e drop de `TotalCharges` para mitigar multicolinearidade, (3) `class_weight='balanced'` como estratégia de balanceamento.
* **[2026-04-15]** **Etapa 2 (Pipeline de Features) concluída.** Função `preprocess_features` criada de maneira unificada e "production-ready" prevendo os requisitos do Streamlit. Variáveis multiclasse (Internet e Pagamento) resolvidas com One-Hot Encoding dropando bases. Categóricas binárias e ternárias convertidas manualmente preservando o sinal denso. Escalonamento deliberadamente adiado para evitar data leakage. Variável composta `NumServicos` gerada como Índice de Ancoragem preditivo. CSV exportado com 24 features numéricas.
* **[2026-04-15]** **Etapa 3 (Modelagem Preditiva) concluída.** Logistic Regression vs Random Forest comparadas com RandomizedSearchCV e validação estratificada 5-fold. LR selecionada como campeã por ser a única a atender os 3 SLAs simultaneamente (Recall=78%, Macro F1=71%, Gap=1.5pp). RF descartada por overfitting severo (gap=18pp). Modelo salvo em `models/campeao.joblib` com probabilidades naturalmente calibradas para o Score de Risco.
* **[2026-04-15]** **Etapa 4 (Score de Risco) concluída.** Definida transformação do `.predict_proba()` em `Risk_Score` inteiro (0-100) e clusterização da base em 3 tiers de risco (identificando 1.640 clientes no grupo de 'Alto Risco'). Módulo escalável `src/inference.py` finalizado contendo o pipeline end-to-end `predict_and_score`.
* **[2026-04-15]** **Etapa 5 (Deploy Streamlit) concluída.** Interface de inferência operacional com upload de CSV, KPIs executivos, Tabela de Ação filtrada por base ativa (ex-clientes ocultados), filtro por Tier + download CSV e seletor individual na sidebar. Módulo de produção `src/inference_app.py` com validação de schema e robustez OHE.
