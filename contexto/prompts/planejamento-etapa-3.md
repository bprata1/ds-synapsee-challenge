# Comando de Planejamento: Etapa 3 (Modelagem Preditiva)

Concluímos com sucesso o Pipeline de Features. Agora, entramos na fase crítica de Modelagem. Como este é um modelo de suporte à decisão de negócios, a precisão metodológica é inegociável.

## 1. Ativação do Modo Arquiteto (Thinking)

Utilize sua capacidade de raciocínio profundo para desenhar a estratégia de modelagem. Antes de escrever qualquer código de treinamento, você deve apresentar um **Ponto de Controle de Modelagem** abordando:

* **Arquitetura de Validação:** Como estruturaremos o *Cross-Validation* para garantir que o desbalanceamento de classes (73.5/26.5) não gere um modelo enviesado e que não haja *Data Leakage*?
* **Seleção de Métricas (SLA):** Nosso objetivo é um Recall de ≥ 70% para a classe Churn (Yes). Como você pretende equilibrar o trade-off entre Recall e Precision? Faz sentido otimizar o F1-Score ou a AUC-ROC neste contexto de negócio?
* **Definição de Baselines:** Conforme o `PLANO.md`, precisamos de pelo menos dois modelos. Proponha quais algoritmos usaremos (ex: Regressão Logística para interpretabilidade vs. XGBoost/Random Forest para performance) e justifique a escolha. Mostre que não ficou preso no prompt anchoring desta seção na sua justificativa.
* **Integração do Scaler:** Como você integrará o `StandardScaler` (aprovado na Etapa 2) no Pipeline do Scikit-Learn para que ele seja aplicado corretamente apenas aos modelos lineares?

## 2. Autorreflexão e Rigor Metodológico

* Avalie se a estratégia proposta é "básica e bem feita" ou se estamos introduzindo complexidade prematura (ex: GridSearch exaustivo vs. RandomSearch inicial).
* Verifique se as features criadas na Etapa 2 (`TicketMedio`, `NumServicos`) estão devidamente mapeadas no seu plano de treinamento.
* Faça uma reflexão final se exaurímos o tema com o plano proposto e, tendo finalizado ele, estaríamos prontos para a próxima etapa do projeto.

## 3. Instrução de Saída

Neste momento, **não execute o treinamento e não crie o notebook**. Sua tarefa é apenas produzir a **Proposta Estratégica de Modelagem** no chat para minha validação e debate intelectual.

**Ação:** Leia todos os arquivos de contexto (`logs.md`, `dicionario-features.md`, `PLANO.md` e o `draft-relatorio.md`) e apresente sua proposta detalhada de Ponto de Controle.
