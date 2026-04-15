# Desafio Técnico Data Scientist: Predição de Churn em Telecom

> **Visão Geral:** Este repositório contém o pipeline analítico ponta a ponta desenvolvido para o desafio técnico da Synapsee. O objetivo principal é prever a probabilidade de cancelamento de serviços (Churn) de clientes de telecomunicações, identificando perfis de risco e derivando um Score de Risco contínuo (0-100), culminando na entrega de uma aplicação interativa preditiva em Streamlit.

## 🚦 Status do Projeto
* **Fase atual:** Etapa 2 (Pipeline de Features) concluída. Base limpa, variáveis codificadas e estruturadas pensando no deploy produtivo. Próximo passo: Modelagem Preditiva (Etapa 3).

---

## 📊 O Dataset
* **Fonte:** [Telco Customer Churn — IBM/Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
* **Descrição:** 7.043 registros de clientes de uma operadora de telecom, com 21 variáveis (dados demográficos, serviços contratados, faturamento e tenure). Variável alvo: `Churn` (Yes/No), com desbalanceamento moderado de 2.77:1 (~73.5% No / 26.5% Yes).

## 🧠 Pipeline e Metodologia

1. **Análise Exploratória (EDA):** [Concluída] Varredura sistêmica de qualidade, ranking de features (Cramér's V + ponto-bisserial), detecção de multicolinearidade e mapeamento do perfil de churn. Notebook: `notebooks/01_eda.ipynb`. Figuras: `reports/figures/`.
2. **Feature Engineering:** [Concluída] Função unificada para produção contendo imputação, criação do `TicketMedio` e do `NumServicos` (índice de ancoragem), encoding cuidadoso (OHE e ordinal) minimizando esparsidade. Dataset 100% numérico processado salvo. Notebook: `notebooks/02_feature_engineering.ipynb`.
3. **Modelagem:** [Próximo] Comparação de pelo menos dois algoritmos com `class_weight='balanced'`. O escalonamento ocorrerá em pipelines internas.
4. **Score de Risco:** [A definir] Escala contínua 0-100 baseada nas probabilidades do modelo.

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

5. **Execução da Aplicação (Streamlit):**
   ```bash
   # Comando disponível após o deploy da Etapa 4
   # streamlit run app.py
   ```

---

## 🏆 Resultados e Entregáveis
* **Métricas do Modelo Final:** [Pendente — Etapa 3] SLA: Recall ≥70% na classe Churn, Macro F1 ≥70%, queda máxima de 10pp entre treino e teste.
* **Relatório Técnico:** O detalhamento das decisões arquiteturais e trade-offs assumidos durante o desenvolvimento está documentado no arquivo `markdowns-ativos/draft-relatorio.md`.

---

## 📌 Histórico de Marcos (Milestones)
* **[2026-04-12]** Infraestrutura de versionamento, logs autônomos e registro de trade-offs arquitetada com sucesso.
* **[2026-04-14]** **Etapa 1 (EDA) concluída.** Varredura completa de qualidade de dados (zero anomalias além de 11 nulos semânticos em TotalCharges). Ranking de features por correlação e Cramér's V. Três decisões estruturais aprovadas: (1) imputação de TotalCharges com 0, (2) criação de `TicketMedio` e drop de `TotalCharges` para mitigar multicolinearidade, (3) `class_weight='balanced'` como estratégia de balanceamento.
* **[2026-04-15]** **Etapa 2 (Pipeline de Features) concluída.** Função `preprocess_features` criada de maneira unificada e "production-ready" prevendo os requisitos do Streamlit. Variáveis multiclasse (Internet e Pagamento) resolvidas com One-Hot Encoding dropando bases. Categóricas binárias e ternárias convertidas manualmente preservando o sinal denso. Escalonamento foi deliberadamente adiado para evitar data leakage no pipeline. Variável composta `NumServicos` gerada para servir como Índice de Ancoragem preditivo. CSV exportado com 24 features 100% puras numericamente.