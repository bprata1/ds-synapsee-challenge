# Comando de Finalização: Etapa 5 (Interface de Inferência Streamlit)

Chegamos à última etapa. O objetivo é criar uma plataforma onde o usuário final possa subir um CSV e receber as predições de churn e o Score de Risco.

## 1. Preparação para Produção (MLOps)

* **Script de Produção:** Crie uma cópia isolada chamada `src/inference_app.py`. Modifique esta cópia para garantir que a coluna `customerID` **nunca seja descartada** no output final. O modelo não usa o ID para prever, mas a interface precisa dele para identificar o cliente.
* **Arquivo de Teste (Sample Batch):** Crie um script rápido que extraia 50 linhas aleatórias do CSV original bruto e salve como `data/raw/sample_upload_batch.csv`. Use ele para fazer testes de upload na interface.

## 2. Desenvolvimento da Interface MVP (`app.py`)

* Crie o arquivo `app.py` na raiz utilizando Streamlit. Carregue o modelo congelado `models/campeao.joblib`. *O modelo não pode ser alterado*.
* **Escopo Funcional (Strict MVP):**
    1. **Upload:** Componente `st.file_uploader` aceitando CSV.
    2. **Teste de Sanidade (Robustez):** Ao subir o arquivo, o sistema deve verificar se as colunas esperadas estão presentes antes de processar. Se faltar algo, emita um `st.warning` amigável em vez de quebrar a tela.
    3. **Processamento:** Ao subir o arquivo, passe os dados pela função unificada do `src/inference_app.py`.
    4. **KPIs (Visão Executiva):** Mostre `st.metric` com o total de clientes processados e o percentual em "Alto Risco".
    5. **Tabela de Ação:** Exiba um dataframe ordenado do maior score para o menor.
    6. **Seletor de Cliente (UX Melhorada):** Uma barra lateral (`st.sidebar`) com um `st.selectbox` listando os `customerID`s processados. Ao selecionar, mostre o Score e Tier daquele cliente.
    7. **Extração Inteligente (Filtro Operacional):** Adicione um filtro (ex: `st.radio` ou `st.selectbox`) para o usuário escolher o Tier de Risco (Alto, Médio, Baixo ou Todos). Conecte esse filtro a um `st.download_button` para baixar o CSV filtrado.

## 3. Autorreflexão Final

Após concluir o código, faça uma autorreflexão final aqui no chat:

* O pipeline no `inference_app.py` está robusto o suficiente para tratar o CSV?
* O Teste de Sanidade que você implementou evita que a tela quebre caso o usuário suba o arquivo errado?
* Há algo mais que possa ser feito para garantir que a apresentação de amanhã seja impecável? Pensando nesta etapa.

## 4. Documentação e Storytelling (Gatilho B)

* Atualize o `markdowns-ativos/draft-relatorio.md`. Crie a seção "Etapa 5 - Interface de Decisão (Deploy)".
* **Ação Obrigatória:** Escreva uma seção de *Storytelling* de negócio desta etapa. Explique:
  * Como o uso do Score de Risco prioriza o orçamento da equipe de retenção.
  * A funcionalidade de extração filtrada para a equipe de discagem.
  * A decisão arquitetural de separar o `inference_app.py` (MLOps).

## 5. Governança e Transição Final

1. Atualize os `logs.md` indicando a criação do app (Gatilho A).
2. Após criar os arquivos e a documentação, execute o commit final (Gatilho C): `feat(deploy): implementa interface Streamlit com filtros operacionais e encerra o projeto`.

**Ação:** Desenvolva o código, gere o arquivo de teste, atualize a documentação e me apresente o resumo da sua autorreflexão.
