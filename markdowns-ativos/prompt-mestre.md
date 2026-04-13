# Diretrizes Centrais do Projeto: Desafio Synapsee (Data Scientist)

## 1. Contexto e Objetivo Core

O desafio consiste em processar a base "Telco Customer Churn" (Kaggle) para construir um pipeline analítico ponta a ponta. O objetivo é prever a probabilidade de cancelamento de serviços (Churn) com base no perfil do cliente, serviços contratados e histórico de faturamento, além de derivar uma lógica matemática coerente para um "Score de Risco" (escala contínua de 0 a 100).

## 2. Escopo de Entregas Obrigatórias

O projeto deve estritamente conter as seguintes entregas:

* **EDA (Notebook):** Um arquivo Jupyter (`.ipynb`) com análise exploratória, distribuição das variáveis, relações entre atributos e, principalmente, diferenças comportamentais entre clientes com e sem churn.

* **Pipeline de Features:** Script de pré-processamento abrangendo tratamento de valores ausentes, encoding de categóricas, escalonamento e criação de atributos derivados (feature engineering). Cada escolha deve ter sua justificativa documentada.

* **Modelagem Preditiva:** Treinamento, validação e comparação obrigatória de pelo menos **duas abordagens diferentes** de algoritmos (priorizando o trade-off entre interpretabilidade e performance). Estratégias para lidar com desbalanceamento de classes são obrigatórias.

* **Score de Risco:** Proposta, cálculo e documentação de um score contínuo que represente o risco de churn de forma útil e bem explicada.

* **Plataforma de Inferência:** Uma interface simples em `Streamlit` onde o usuário faz upload de um CSV de clientes e recebe a classificação de churn e o score de risco.

* **Relatório Final:** Documento Markdown registrando o que funcionou, o que não funcionou, trade-offs e próximos passos (o que seria feito com mais tempo/dados).

## 3. Restrições e Mindset (Pragmatismo)

* **Gestão de Tempo Restrita:** O projeto deve ser concluído rapidamente. Foco absoluto no "básico bem feito".

* **Defesa Técnica ao Vivo:** O usuário precisará explicar o código, as decisões analíticas e a modelagem para uma banca avaliadora. Portanto, o código deve ser extremamente limpo, interpretável e com decisões documentadas (zero "black-boxes").

* **Governança Estrita:** Todas as decisões arquiteturais de alto impacto devem passar pelo crivo do usuário (via Ponto de Controle) antes de serem codificadas.

## 4. Critérios de Aceitação (SLAs)

1. **Baseline de Negócio:** Recall da classe 1 (Churn) e Macro F1-Score mínimos de 70% nos dados de teste. (Acurácia não é a métrica principal devido ao desbalanceamento).
2. **Robustez:** Queda máxima de 10 pontos percentuais de performance (F1-Score) entre Treino e Teste, comprovando capacidade de generalização e baixa tolerância a overfitting.
3. **Coerência do Score:** A lógica matemática deve garantir que o Score de Risco seja monotonicamente coerente (ex: clientes classificados como "Churn=Yes" devem possuir scores estritamente maiores do que a média dos clientes "Churn=No").
4. **Deploy:** A interface Streamlit deve conseguir receber o upload de um CSV (no formato da base original) e prever os resultados sem erros de compilação ou exceções.
