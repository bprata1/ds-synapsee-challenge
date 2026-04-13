# PLANO.md - Desafio Data Scientist (Synapsee)

## 1. O que entendi do problema e o que vou resolver

A empresa precisa identificar preventivamente quais clientes de telecomunicações têm maior probabilidade de cancelar seus serviços (Churn). O objetivo não é apenas criar um modelo de "caixa-preta", mas sim fornecer diagnósticos acionáveis baseados no perfil, serviços contratados e histórico de faturamento do cliente.

Vou construir um pipeline ponta a ponta que engloba a análise exploratória (para entender o comportamento de quem cancela), a engenharia de features, o treinamento e comparação de dois modelos preditivos (focando no trade-off entre interpretabilidade e performance), e a derivação de um "Score de Risco" de 0 a 100. O produto final será uma plataforma de inferência em Streamlit para simulações via upload de CSV, acompanhada de um relatório detalhado de decisões.

## 2. Etapas de execução e estimativa de tempo (Total planejado: 14 horas)

* **Etapa 1: Entendimento e Análise Exploratória (EDA) (3h)** - Carregar os dados, avaliar nulos ocultos (ex: espaços em branco na variável de cobrança total), analisar o desbalanceamento da variável alvo e mapear as variáveis que mais influenciam o cancelamento.
* **Etapa 2: Pipeline de Features (3h)** - Criar o pipeline de pré-processamento, realizando *encoding* de variáveis categóricas, escalonamento numérico e criação de atributos derivados (ex: ticket médio gasto) para facilitar o aprendizado dos modelos.
* **Etapa 3: Modelagem Preditiva (4h)** - Treinar e comparar pelo menos duas abordagens (ex: Regressão Logística para *baseline*/interpretabilidade vs. XGBoost/Random Forest para performance). Foco em lidar com o desbalanceamento das classes.
* **Etapa 4: Lógica do Score de Risco (2h)** - Extrair as probabilidades contínuas do modelo escolhido (`predict_proba`) e calibrá-las para criar uma regra matemática robusta e de fácil interpretação para o negócio (Score de Risco de 0 a 100).
* **Etapa 5: Plataforma de Inferência e Relatório (2h)** - Desenvolver e testar a interface no Streamlit, garantindo que o upload funcione corretamente, e redigir o `draft-relatorio.md` consolidando as lições aprendidas e trade-offs.

## 3. Critérios de Sucesso (Testes de Aceitação)

O projeto será considerado entregue com qualidade se passar estritamente nestes quatro testes práticos:

1. **Teste de Performance Base (Métrica de Negócio):** O modelo escolhido deve atingir um **Recall da classe 1 (Churn)** e um **Macro F1-Score** superiores a 70% nos dados de teste. Acurácia não será o critério principal devido ao desbalanceamento natural do problema.
2. **Teste de Robustez (Tolerância a Overfitting):** A queda de performance (F1-Score) do modelo entre os dados de Treinamento e os dados de Teste não pode ser superior a 10 pontos percentuais, provando que o modelo tem alta capacidade de generalização.
3. **Teste de Coerência do Score:** A lógica matemática do score de risco deve ser monotonicamente coerente com a probabilidade (quanto maior a probabilidade de churn do modelo, maior deve ser a nota entre 0 e 100). Clientes classificados na classe "Churn=Yes" devem possuir scores estritamente maiores do que a média dos clientes "Churn=No".
4. **Teste de Usabilidade (Deploy Funcional):** A interface no Streamlit deve receber o upload de um CSV com novos clientes no mesmo formato da base original e retornar a classe prevista e o score de risco sem gerar `runtime errors` ou falhas de compilação.
