# Comando de Preparação: Material da Banca (Urgente)

Tenho poucos minutos para a minha apresentação final para a banca técnica. Preciso que você atue como meu *Speechwriter* e consolide todo o nosso trabalho em dois materiais de apoio, baseados no `RELATORIO_FINAL.md` e no `draft-relatorio.md`.
**Importante:** Escreva de forma didática, direta e confiante, pois usarei isso como minha cola principal para defender o projeto.

## 1. Arquivo de Projeção (`APRESENTACAO.md`)

Este arquivo será projetado na tela. Ele deve ser extremamente visual, com pouco texto, usando bullets curtos e referenciando os caminhos das imagens que geramos.

* **Estrutura (5 passos):**
  1. **O Desafio:** Os 3 SLAs estabelecidos.
  2. **A História dos Dados (EDA):** Destaque para o "Combo Tóxico" e a "UTI dos 6 Meses". (Inclua o link para a imagem `reports/figures/eda_categoricas_vs_churn.png`).
  3. **A Cozinha Técnica:** LR vs RF. A vitória do "Básico Bem Feito" (Gap de 1.47pp vs 18pp).
  4. **A Entrega de Valor:** A criação do `TicketMedio` e do `NumServicos` (Índice de Ancoragem), e a divisão em Tiers de Risco.
  5. **Arquitetura de Produção:** O deploy no Streamlit e MLOps básico.

## 2. Roteiro do Apresentador (`ROTEIRO_FALA.md`)

Este é o meu documento pessoal (a "cola").

* Para cada passo acima, inclua:
  * **O que falar:** Um parágrafo curto e de impacto para eu ler.
  * **Defesa Técnica (O Porquê):** As respostas prontas e fáceis de explicar para as decisões.
    * *EDA:* Por que imputei 0 no TotalCharges?
    * *Modelo:* Por que adiei o Scaler (Data Leakage)? Por que LR e não RF? Por que `class_weight` e não SMOTE?
    * *Deploy:* Por que filtrei ex-clientes da interface (Miopia Operacional)?

**Ação:** Gere imediatamente os dois arquivos.
