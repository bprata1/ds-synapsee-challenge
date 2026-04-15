# Comando de Inicialização: Etapa 4 (Score de Risco)

Temos nosso modelo campeão treinado e salvo. Agora, precisamos traduzir o output matemático (probabilidade) em uma métrica de negócios acionável para a operação: o Score de Risco.

## 1. Criação do Score de Risco

* Crie o notebook `notebooks/04_score_risco.ipynb` (use script Python para gerar o JSON com segurança, como feito nas etapas anteriores).
* Carregue a base processada (`data/processed/telco_churn_features.csv`) e o modelo campeão (`models/campeao.joblib`).
* **Ação:** Aplique o `.predict_proba()` no dataset inteiro. Multiplique a probabilidade da classe 1 (Churn) por 100 e arredonde para criar uma nova coluna inteira chamada `Risk_Score` (0 a 100).

## 2. Clusterização de Risco (Tiers)

A operação precisa de faixas de prioridade para atuar.

* **Ação:** Crie uma coluna `Risk_Tier` com as seguintes categorias baseadas no `Risk_Score`:
  * **Baixo Risco:** 0 a 30
  * **Risco Médio:** 31 a 70
  * **Alto Risco:** 71 a 100 (Estes são os clientes que precisam de ação imediata).
* *Nota Analítica:* Gere uma distribuição (Value Counts) de quantos clientes caem em cada Tier para vermos o tamanho do problema da operação.

## 3. Preparação para o Deploy (Streamlit)

Amanhã, a interface web receberá um arquivo CSV bruto do usuário. O backend precisará rodar todo o pipeline (da limpeza à predição).

* **Ação:** No notebook, além de calcular os scores, crie uma função "portátil" chamada `predict_and_score(df_raw, model)`. Essa função deve:
  1. Chamar internamente a função `preprocess_features` (que criamos na Etapa 2) para limpar o dado bruto.
  2. Aplicar o `.predict()` e o `.predict_proba()` do modelo.
  3. Gerar as colunas `Risk_Score` e `Risk_Tier`.
  4. Retornar o dataframe final pronto para exibição.
* Salve esse código limpo em um arquivo `src/inference.py` (crie a pasta `src/`), pois precisaremos importar isso amanhã no Streamlit. Você pode salvar a base final como `data/processed/telco_churn_scored.csv` apenas para fins de auditoria, mas ela não será a entrada do app.

## 4. Governança

1. Atualize o `markdowns-ativos/dicionario-features.md` registrando as novas colunas `Risk_Score` e `Risk_Tier` (Gatilho A).
2. Atualize o `markdowns-ativos/logs.md` (Gatilho A).
3. Atualize o `draft-relatorio.md` (Gatilho B), adicionando uma breve seção sobre como a probabilidade matemática foi transformada em Score de Risco e quantas pessoas caíram na faixa de "Alto Risco". Já traga a seção de storytelling também traduzindo para regra de negócio.
4. Execute o commit (Gatilho C).

**Pode iniciar a execução técnica. Aguardo um resumo de quantos clientes temos no Tier de "Alto Risco"!**
