# Comando de Ignição: Início do Projeto

Nossa infraestrutura de governança está 100% configurada e pronta para operar. A partir de agora, você está ativo no modo de desenvolvimento.

## Instruções de Execução Imediata

1. **Leia as Regras:** Revise silenciosamente o arquivo `markdowns-ativos/prompt-mestre.md` para carregar em sua memória as suas restrições e SLAs.
2. **Inicie o Plano:** Siga para a Etapa 1 definida no nosso arquivo `contexto/PLANO.md`.
3. **Setup do Ambiente de Análise:**
   * Crie um notebook chamado `notebooks/01_eda.ipynb`.
   * Carregue os dados que estão localizados em `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv`.
4. **Objetivos da Análise Exploratória (EDA):**
   * Avalie a existência de nulos ocultos (ex: espaços em branco na variável de cobrança total, conforme mapeado no Plano).
   * Analise o desbalanceamento da variável target (`Churn`).
   * Demonstre visualmente quais *features* (numéricas ou categóricas) apresentam maior peso/correlação com o cancelamento do serviço.

## Lembretes de Governança

* Pause a execução e solicite minha validação (Ponto de Controle) antes de tomar decisões de alto impacto sobre o tratamento dos dados.
* Acione imediatamente suas regras autônomas de Logs e Dicionário (Gatilho A) assim que executarmos transformações consolidadas nos DataFrames.
