# Relatório Final — Desafio Data Scientist Synapsee

> **Autor:** Bernardo Prata  
> **Data de entrega:** 15 de Abril de 2026  
> **Escopo:** Pipeline analítico ponta a ponta para predição de Churn em Telecom, desde a exploração de dados até uma plataforma funcional de inferência.

---

## 1. O que Funcionou

### 1.1 Planejamento como Investimento, não Burocracia

O `PLANO.md` entregue antes do código foi essencial para definir os SLAs internos (Recall ≥ 70%, Macro F1 ≥ 70%, Gap Treino/Teste ≤ 10pp). Ter critérios objetivos de sucesso antes de abrir o Jupyter evitou a armadilha clássica de "iterar indefinidamente buscando +0.5pp de AUC". Todos os 3 SLAs foram atingidos com o modelo final.

| SLA | Meta | Resultado | Status |
| --- | --- | --- | --- |
| Recall (Churn) | ≥ 70% | **78.07%** | ✅ |
| Macro F1-Score | ≥ 70% | **70.94%** | ✅ |
| Gap Treino/Teste | ≤ 10pp | **1.47pp** | ✅ |

### 1.2 O Básico Bem Feito Venceu a Complexidade

A Logistic Regression (C=0.01, `class_weight='balanced'`) superou a Random Forest em todos os critérios que importam para produção:

- **Generalização:** Gap de 1.5pp vs 18pp da RF.
- **Recall:** 78% vs 65% — 13pp a mais de churners capturados.
- **Interpretabilidade:** Coeficientes traduzíveis diretamente em narrativa de negócio.
- **Calibração:** Probabilidades naturalmente calibradas, dispensando etapa de calibração posterior (Platt Scaling / Isotonic Regression).

A decisão de não incluir XGBoost foi deliberada: a margem teórica de ganho (1-3pp de Macro F1) não justificava a complexidade de tuning (9+ hiperparâmetros) nem a dificuldade de defesa técnica ("boosting com gradiente + regularização L1/L2" vs "regressão com penalidade").

### 1.3 Features Criadas com Significado de Negócio

As duas features engenheiradas — `TicketMedio` e `NumServicos` — funcionaram não apenas como preditores, mas como ferramentas de comunicação com stakeholders:

- **`TicketMedio`** (TotalCharges / tenure): Responde "quanto o cliente gasta por mês em média desde que entrou". Expõe upsell/downsell invisível nas variáveis brutas.
- **`NumServicos`** (soma das 8 flags de serviço): Índice de ancoragem — quanto mais serviços, maior a fricção de saída. Na apresentação, isso se traduz em: *"Cancelar a internet é fácil. Cancelar a internet, o telefone, o backup e os canais de TV ao mesmo tempo gera atrito."*

### 1.4 Modularização para Produção (MLOps)

A separação entre `inference.py` (módulo analítico) e `inference_app.py` (módulo de produção que preserva o `customerID`) deu segurança operacional ao deploy. A regra é simples: notebooks importam o primeiro; Streamlit importa o segundo. Mudanças na UI não quebram o pipeline de validação, e vice-versa.

O `@st.cache_resource` no carregamento do modelo evita que o `.joblib` seja relido do disco a cada interação do usuário — sem ele, cada clique no Streamlit travaria o app por 1-2 segundos.

### 1.5 Score de Risco Operacionalmente Útil

A transformação `predict_proba × 100` foi deliberadamente simples. A pergunta "como esse score foi calculado?" tem uma resposta que cabe em uma frase. Os 3 Tiers (Baixo 0-30 / Médio 31-70 / Alto 71-100) transformaram uma lista de 7.043 clientes em filas de ação gerenciáveis:

| Tier | Clientes | Ação |
| --- | --- | --- |
| Alto Risco (71-100) | 1.640 (23.3%) | Ligação imediata |
| Risco Médio (31-70) | 2.476 (35.2%) | Campanha preventiva |
| Baixo Risco (0-30) | 2.927 (41.6%) | E-mail automático |

### 1.6 Robustez no Deploy

Três camadas de proteção no Streamlit garantem que a aplicação não "crasha" na apresentação:

1. **Validação de schema** (`validate_columns`): Detecta colunas faltantes antes de qualquer processamento.
2. **Robustez OHE**: Garante que todas as colunas dummy esperadas existam mesmo em batches parciais (ex: CSV só com clientes DSL).
3. **Filtro de base ativa**: A Tabela de Ação exclui ex-clientes (Churn=1) da fila de retenção — bug de regra de negócio detectado e corrigido durante teste E2E.

---

## 2. O que Não Funcionou (ou Funcionou Parcialmente)

### 2.1 Random Forest: Promessa vs Realidade

A RF teve Macro F1 ligeiramente superior (+1.3pp no teste), mas:

- **Overfitting severo:** Gap de 18pp entre treino e teste (SLA: ≤10pp). As 200 árvores "decoraram" os padrões do treino.
- **Recall insuficiente:** 65% (SLA: ≥70%). Para cada 100 churners reais, a RF deixa 35 escaparem.

A tentativa de regularização via `max_depth`, `min_samples_leaf` e `max_features` não foi suficiente para reduzir o gap a um nível aceitável dentro do orçamento de tempo. Com mais iterações de tuning, é possível que a RF convergisse, mas o custo-benefício não se justificava frente à LR já aprovada.

### 2.2 Precision: O Trade-off Consciente

A LR tem Precision de 51% — de cada 100 alertas de churn, ~49 são falsos positivos. Este é o preço da vigilância: o `class_weight='balanced'` deliberadamente prioriza Recall (não perder churners) em detrimento de Precision. No contexto de negócio, o custo de ligar para um cliente satisfeito oferecendo um desconto é muito menor do que o custo de perder um insatisfeito que ninguém contactou.

Ainda assim, uma Precision acima de 60% seria operacionalmente mais confortável para equipes de retenção com capacidade limitada de discagem.

### 2.3 Interface sem Gráficos de Distribuição

O MVP do Streamlit focou em tabelas e métricas, sem incluir visualizações como:

- Histograma da distribuição de scores na base enviada.
- Gráfico de barras comparando Tiers.
- Gauge visual do score individual na sidebar.

A decisão foi funcional (entregar ação > entregar estética), mas reconheço que gráficos de contexto ajudariam o gestor a entender a "saúde geral" da base antes de agir.

---

## 3. O que Faria Diferente com Mais Tempo

### 3.1 Feature Engineering Avançada

- **Interações cruzadas:** `tenure × Contract` capturaria que clientes novos em contrato mensal são ordens de magnitude mais arriscados que novos em contrato anual. A LR não captura interações automaticamente.
- **Binning de tenure:** Criar faixas ("0-6 meses", "7-12", "13-24", "24+") ao invés de usar o contínuo, dado o forte efeito não-linear observado na EDA (pico de churn concentrado nos primeiros 6 meses).
- **Ratio features:** `MonthlyCharges / média_do_contrato` poderia revelar clientes pagando acima da média do seu segmento.

### 3.2 Modelos Adicionais

- **XGBoost ou LightGBM** com tuning rigoroso (Optuna + early stopping) — potencial de +2-4pp de Macro F1 sem sacrifice de generalização, se bem regularizado.
- **Stacking:** Ensemble que combine LR (calibrada) com Gradient Boosting, usando as probabilidades do primeiro como feature do segundo.
- **Threshold otimizado:** O corte padrão de 0.5 é arbitrário. Otimizar o limiar via curva Precision-Recall para maximizar o F1 no ponto específico que equilibra custo de falso positivo vs falso negativo.

### 3.3 Validação Temporal

O split atual é aleatório estratificado. Em produção real, o churn tem dinâmica temporal — um modelo treinado em dados de janeiro pode performar diferente em julho. Com mais dados:

- **Walk-forward validation:** Treinar em meses anteriores, testar no mês seguinte. Simula a realidade operacional.
- **Monitoramento de drift:** Implementar alertas quando a distribuição de scores mudar significativamente entre batches (Kolmogorov-Smirnov sobre a distribuição de `Risk_Score`).

---

## 4. O que Faria Diferente com Mais Dados

### 4.1 Dados Comportamentais

A base Telco é estática — um snapshot. Com dados transacionais:

- **Frequência de chamados ao suporte:** Clientes que ligam repetidamente estão mais propensos a cancelar.
- **Histórico de downgrades:** Quem já reduziu o plano está sinalizando insatisfação antes do cancelamento.
- **Padrões de uso:** Volume de dados consumido, minutos de ligação — queda de uso precede o churn.

### 4.2 Dados Externos

- **NPS (Net Promoter Score):** Pesquisas de satisfação são preditores diretos de intenção de saída.
- **Dados de concorrência:** Promoções agressivas de concorrentes no período explicariam picos de churn que variáveis internas não capturam.
- **Dados geográficos:** Qualidade de cobertura por região — churn pode ser mais alto em áreas com sinal fraco.

### 4.3 Série Temporal por Cliente

Com múltiplos snapshots mensais (o dataset tem apenas um), seria possível:

- Construir **curvas de sobrevivência** (Kaplan-Meier, Cox Proportional Hazards) para prever *quando* o churn ocorrerá, não apenas *se*.
- Detectar **trajetórias de risco**: clientes cujo score sobe consistentemente mês a mês vs aqueles com score estável.

---

## 5. O que Faria Diferente com Maior Contexto de Negócio

### 5.1 Calibração Econômica dos Tiers

Os limiares 30/70 foram definidos heuristicamente. Com dados reais de:

- **Custo médio de aquisição de cliente (CAC)**
- **Lifetime Value (LTV) por segmento**
- **Custo por ligação de retenção**

...seria possível calcular o **ponto ótimo de corte** onde `custo_de_reter < custo_de_perder`, transformando os Tiers em faixas economicamente calibradas ao invés de percentis arbitrários.

### 5.2 Prescriptive Analytics

O sistema atual é **preditivo** (quem vai cancelar?). Com contexto de negócio, evoluiria para **prescritivo**:

- *"Cliente X tem 85% de chance de churn. A causa mais provável é contrato mensal + fibra sem suporte técnico. Ação recomendada: oferecer migração para contrato anual com 3 meses grátis de TechSupport."*
- Cada ação teria um **ROI estimado** baseado no LTV preservado vs custo da oferta.

### 5.3 A/B Testing do Modelo

Antes de escalar para toda a base, rodar um teste controlado:

- **Grupo de tratamento:** Clientes de Alto Risco recebem ligação proativa.
- **Grupo de controle:** Clientes de Alto Risco não são contactados.
- Medir a **redução real de churn** atribuível ao modelo — o único número que justifica o investimento em Data Science vs a intuição do gerente.

---

## 6. Lições Aprendidas

1. **Simplicidade é uma feature, não uma limitação.** A Regressão Logística venceu porque generaliza melhor, é mais interpretável e tem probabilidades naturalmente calibradas. A complexidade do modelo não é mérito — a utilidade do output é.

2. **O teste E2E revelou bugs que o backtest não captura.** A robustez OHE (batches parciais sem todas as categorias) e o filtro de base ativa (ex-clientes na fila de retenção) só apareceram quando um CSV real foi processado na interface.

3. **A separação treino/produção é inegociável.** Notebooks sujos são ferramentas de pesquisa. O módulo de inferência precisa ser determinístico, testável e isolado.

4. **O valor do projeto não está no modelo — está na fila de trabalho.** O Score de Risco e os Tiers transformam uma massa amorfa de 7.043 clientes em ação operacional com urgência definida. Esse é o output que justifica o investimento.
