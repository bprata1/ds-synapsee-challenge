# Desafio Técnico — Data Scientist **Synapsee**

---

## Contexto

Na Synapsee, além das frentes de pesquisa aplicada, também lidamos com problemas de analytics orientados a negócio, nos quais dados precisam ser transformados em diagnósticos, previsões e recomendações acionáveis.

Neste desafio, você vai construir uma solução de análise e predição de churn a partir de uma base tabular de clientes, cobrindo desde a exploração dos dados até uma plataforma funcional de inferência.

---

## Dataset

**Telco Customer Churn**
<https://www.kaggle.com/datasets/blastchar/telco-customer-churn>

- Base tabular com informações de clientes de telecom, incluindo perfil, serviços contratados, faturamento e status de cancelamento
- Dataset clássico, compacto e suficientemente rico para avaliar exploração, preparação de dados, modelagem e interpretação de resultados

---

## O que você deve entregar

### 1. PLANO.md — entregue antes de escrever qualquer código

Antes de começar, escreva um documento curto com:

- Sua leitura do problema e o que você pretende resolver
- As etapas que você vai executar, em ordem, com estimativa de tempo para cada uma
- Os critérios que você mesmo vai usar para saber se o resultado é bom

Envie este arquivo para nós antes de começar a desenvolver. Ele é parte da avaliação.

---

### 2. Análise exploratória (EDA)

Notebook com análise da distribuição das variáveis, relações entre atributos dos clientes e diferenças entre clientes com e sem churn. Mostre que você entende os dados antes de modelar.

### 3. Pipeline de features

Construa uma pipeline de preparação e engenharia de variáveis — por exemplo: tratamento de valores ausentes, encoding de variáveis categóricas, criação de atributos derivados e padronização, quando fizer sentido. Justifique cada escolha.

### 4. Modelo preditivo

Implemente e compare pelo menos **duas abordagens**. Use métricas adequadas e discuta overfitting, capacidade de generalização e trade-offs entre performance e interpretabilidade.

### 5. Score de risco

Proponha e calcule um score contínuo que represente o risco de churn do cliente. Não precisa ser complexo — precisa ser coerente, útil e bem explicado.

### 6. Plataforma de inferência

Uma interface simples (Streamlit ou similar) onde o usuário faz upload de um CSV de clientes e recebe:

- A classificação de churn
- O score de risco

### 7. Relatório final

Um documento em Markdown com o que funcionou, o que não funcionou e o que você faria diferente com mais tempo, mais dados ou maior contexto de negócio.

---

## Regras

- **Use IA à vontade** — Claude Code, Copilot, Cursor, ChatGPT. Encorajamos o uso dessas ferramentas.
- **Envie o PLANO.md antes de começar a codar.** Ele é parte da avaliação.
- **Suba tudo em um repositório Git** com um README claro de como rodar o projeto.
- **Você apresentará os resultados ao vivo.** Faremos perguntas sobre suas decisões analíticas, de modelagem, os trade-offs envolvidos e o que você aprendeu no processo.
- **Prazo:** combinado individualmente

---

## Critérios de avaliação

- Qualidade do planejamento e aderência ao plano (PLANO.md vs. entrega)
- Rigor na análise exploratória e justificativa das decisões de preparação e features
- Comparação honesta entre abordagens de modelagem
- Coerência do score de risco
- Funcionamento da plataforma de inferência
- Clareza do raciocínio — verificada ao vivo
- ⁠⁠Se respeitou o próprio prazo dado
