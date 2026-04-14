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
