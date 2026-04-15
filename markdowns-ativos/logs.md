# Log de Execução e Memória de Projeto

* **[2026-04-12 10:25] - Configuração Inicial**
  * **Dataframe(s) Ativo(s):** Nenhum carregado.
  * **Alteração:** Governança concluída. Arquitetura de agentes, logs e dicionários implementada com sucesso. Aguardando comando de ignição para carregamento da base de dados.

* **[2026-04-15 13:02] - Configuração de Ambiente**
  * **Dataframe(s) Ativo(s):** Nenhum carregado.
  * **Alteração:** Instalação de dependências concluída. Ambiente virtual ativado e pacotes instalados conforme `requirements.txt`. Aguardando comando de ignição para carregamento da base de dados.

* **[2026-04-14 17:48] - Etapa 1: EDA Completa**
  * **Dataframe(s) Ativo(s):** `df_raw` | Shape: `(7043, 21)` · `df_eda` | Shape: `(7043, 21)` (cópia com TotalCharges numérica)
  * **Alteração:** Criado notebook `notebooks/01_eda.ipynb`. Carregamento da base bruta, detecção de 11 nulos ocultos em TotalCharges (tenure=0), análise de desbalanceamento (73.5% No / 26.5% Yes, ratio 2.77:1), boxplots e KDE das numéricas, taxa de churn por categórica, ranking Cramér's V + correlação ponto-bisserial, heatmap de correlação.
  * **Descrição:** Execução completa da Etapa 1 (EDA). Dados carregados sem transformações permanentes — TotalCharges convertida apenas em cópia temporária. Achados documentados no resumo executivo do notebook.

* **[2026-04-14 20:05] - Etapa 1: Revisão e Correções da EDA**
  * **Dataframe(s) Ativo(s):** `df_raw` | Shape: `(7043, 21)` · `df_eda` | Shape: `(7043, 21)`
  * **Alteração:** (1) PNGs movidos de `data/` para `reports/figures/`. (2) Caminhos reescritos com `pathlib` (absolutos a partir da raiz do repo). (3) Adicionada seção 9: varredura sistêmica de qualidade — scan de anomalias de texto (espaços, ?, NA) em todas as colunas + validação de integridade numérica (negativos, domínio lógico). (4) Ideias de tratamento registradas no `draft-relatorio.md` (Gatilho B).
  * **Descrição:** Revisão solicitada pelo usuário para fechar a Etapa 1 com rigor. Varredura confirmou: zero anomalias adicionais além dos 11 nulos semânticos em TotalCharges. Sem duplicatas de ID, sem valores negativos, sem outliers ilógicos.

* **[2026-04-14 21:00] - Etapa 1: Consolidação Final e Transformações Aprovadas**
  * **Dataframe(s) Ativo(s):** `df_eda` | Shape: `(7043, 21)` → `(7043, 21)` (TotalCharges dropada, TicketMedio adicionada)
  * **Alteração:** (1) Notebook reconstruído via `nbformat` (integridade JSON garantida). (2) TotalCharges: 11 espaços em branco imputados com 0. (3) Criada feature `TicketMedio = TotalCharges / tenure` (0 quando tenure=0). (4) Dropada `TotalCharges` original. (5) Decisões registradas no `draft-relatorio.md`.
  * **Descrição:** Consolidação final da Etapa 1. Transformações aprovadas pelo usuário no Ponto de Controle. Estratégia de balanceamento (`class_weight='balanced'`) registrada para uso na Etapa 3.

* **[2026-04-15 06:55] - Etapa 2: Pipeline de Features e Pré-processamento**
  * **Dataframe(s) Ativo(s):** `df_raw` | Shape: `(7043, 21)` → `df_processed` | Shape: `(7043, 24)`
  * **Alteração:** (1) Criada e executada função `preprocess_features` no notebook 02. (2) Imputação e TicketMedio reaplicados. (3) Features binárias mapeadas para 0/1, colapsando 'No internet service'/'No phone service' para 0. (4) `InternetService` e `PaymentMethod` convertidas via One-Hot Encoding (`drop_first=True`). (5) `Contract` convertida ordinalmente (0-2). (6) `customerID` dropada. (7) Criada feature `NumServicos` (soma das 8 binárias de serviço). (8) Dataset final salvo em `data/processed/telco_churn_features.csv`.
  * **Descrição:** Pipeline consolidado em função única pensando no deploy (Streamlit consumirá a base crua futuramente). DataFrame exportado pronto para a Etapa 3 (sem escalonamento, que será delegado aos pipelines do scikit-learn).

* **[2026-04-15 08:02] - Etapa 3: Modelagem Preditiva (LR vs RF)**
  * **Dataframe(s) Ativo(s):** `df` (loaded from CSV) | Shape: `(7043, 24)` → X_train `(5634, 23)` / X_test `(1409, 23)`
  * **Alteração:** (1) Split estratificado 80/20. (2) Logistic Regression tunada (C=0.01, solver=lbfgs) com StandardScaler no Pipeline. (3) Random Forest tunada (200 arvores, max_depth=15). (4) LR selecionada como campeã — única a atender todos os 3 SLAs simultaneamente. (5) RF descartada por overfitting severo (gap=18pp, SLA<=10pp). (6) Modelo LR salvo em `models/campeao.joblib`. (7) Figuras: confusion matrix, ROC curve, calibration curve, feature importance.
  * **Descrição:** Resultados no holdout: LR Recall=0.78, Macro F1=0.71, ROC-AUC=0.84, Gap=1.5pp. Todos os SLAs PASS. RF teve Macro F1 ligeiramente superior (0.72) mas gap inaceitável (18pp) e Recall insuficiente (0.65).
