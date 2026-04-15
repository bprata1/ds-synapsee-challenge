# Aprovação de Arquitetura: Modelagem Preditiva (Etapa 3)

Seu planejamento é irreparável. A escolha de otimizar o Macro F1-Score para proteger o limite de falsos positivos, a recusa pragmática do XGBoost e a blindagem contra o *Data Leakage* através de um Pipeline unificado demonstram maturidade sênior. O plano está **100% aprovado**.

Adiciono apenas uma única exigência técnica antes de você iniciar o código:

## 1. Preparação para o Score de Risco (Etapa 4)

* O objetivo final não é apenas a classificação binária, mas fornecer uma probabilidade confiável que será transformada em um Score de Risco (Etapa 4).
* **Ação:** Certifique-se de que, na avaliação final e na exportação do modelo campeão, as probabilidades emitidas pelo `.predict_proba()` estejam bem calibradas. Se o Random Forest vencer, considere encapsulá-lo em um `CalibratedClassifierCV` (se o tempo de execução permitir) ou gere a Curva de Calibração (Calibration Curve) para avaliarmos a confiabilidade da probabilidade emitida.

## 2. Execução

* Crie e codifique o notebook `03_modelagem.ipynb` aplicando exatamente a arquitetura que você desenhou.
* Treine a Regressão Logística e a Random Forest.
* Me apresente no chat a tabela comparativa das métricas de ambos no Test Holdout (Recall, Precision, Macro F1, ROC-AUC) e a verificação do limite de Overfitting (<10pp de gap).

## 3. Governança

* Após a conclusão, salve o modelo vencedor em `models/campeao.joblib` (crie a pasta se não existir).
* Atualize o `logs.md` (Gatilho A) com os resultados.
* Atualize o `draft-relatorio.md` (Gatilho B) com a comparação de desempenho e os motivos de escolha do campeão. Faça também uma seção dedicada ao storytelling, igual fizemos nas etapas anteriores.
* Execute o commit (Gatilho C).

**Pode iniciar a execução técnica. Aguardo a tabela comparativa dos modelos!**
