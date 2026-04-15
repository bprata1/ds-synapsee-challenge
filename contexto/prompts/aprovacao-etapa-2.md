# Aprovação e Execução: Pipeline de Features (Etapa 2)

A sua proposta foi de altíssimo nível. A decisão de colapsar o "No internet service", a criação da feature `NumServicos` e, principalmente, a percepção de adiar o escalonamento para evitar *Data Leakage* no modelo linear mostram grande maturidade técnica. **Proposta 100% aprovada.**

No entanto, para a implementação, preciso que você adicione uma blindagem pensando na nossa Etapa 5 (Deploy no Streamlit):

## 1. Encapsulamento para Produção

* O Streamlit receberá dados brutos no futuro. Portanto, não escreva as transformações de dados (encoding, map, drops e criação de NumServicos) soltas em dezenas de células no notebook.
* **Ação:** Crie uma função unificada e limpa chamada `preprocess_features(df_raw)` dentro do notebook `02_feature_engineering.ipynb`. Essa função deve receber o dataframe bruto, aplicar todas as regras aprovadas e retornar o dataframe pronto para a Etapa 3. Certifique-se de incluir os tratamentos da Etapa 1 (imputação de TotalCharges, criação de TicketMedio e descarte do TotalCharges original) dentro desta mesma função. Isso é vital, tanto para a fase atual, tanto porque o Streamlit injetará o CSV 100% cru, e a função precisará reproduzir todo o histórico de transformações de ponta a ponta.

## 2. Salvando o Artefato

* Após aplicar a função no dataset, não perca o dado.
* **Ação:** Salve o dataframe final resultante em um novo arquivo: `data/processed/telco_churn_features.csv` (crie a pasta `processed/` se necessário). A Etapa 3 usará este arquivo.

## 3. Governança e Transição

Após o código rodar com sucesso e o CSV ser salvo:

1. Atualize o `markdowns-ativos/dicionario-features.md` registrando as novas variáveis (ex: dummies) e o status das dropadas (Gatilho A).
2. Atualize o `markdowns-ativos/logs.md` indicando o novo shape do dataset (Gatilho A).
3. Atualize o `draft-relatorio.md` registrando a estratégia de encoding e a feature `NumServicos` que aprovamos (Gatilho B).
4. Faça o commit da Etapa 2 (Gatilho C).

**Pode iniciar a codificação do notebook `02_feature_engineering.ipynb`. Aguardo a confirmação da conclusão com a mensagem de transição de fase.**
