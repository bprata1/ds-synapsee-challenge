# Comando de Inicialização: Etapa 2 (Pipeline de Features)

A Etapa 1 foi concluída e documentada com sucesso. A partir de agora, o foco é a preparação dos dados para a modelagem preditiva.

## 1. Setup Seguro do Ambiente

* Crie o notebook `notebooks/02_feature_engineering.ipynb`.
* **Atenção:** Para evitar a corrupção do arquivo que ocorreu na fase anterior, garanta que a geração do `.ipynb` seja feita de forma estruturalmente segura (ex: via script com `nbformat` ou gerando células limpas e testadas).
* Importe os pacotes necessários e carregue o dataset (lembre-se de que já validamos a imputação de 0 em `TotalCharges` e a criação de `TicketMedio`).

## 2. Ponto de Controle de Pre-processamento (Estratégia)

Antes de aplicar qualquer transformação matemática definitiva no dataset, analise as variáveis disponíveis e me apresente uma proposta clara de pipeline contendo:

* **Estratégia de Encoding:** Como você tratará as variáveis categóricas binárias e multiclasse? (Justifique suas escolhas, como Label Encoding vs. One-Hot Encoding).
* **Estratégia de Escalonamento:** Qual método numérico será utilizado? (Justifique considerando a distribuição dos dados e os algoritmos que testaremos na Etapa 3).
* **Feature Engineering:** Proponha a criação de novas variáveis derivadas que façam sentido para o negócio (além do `TicketMedio` que já consolidamos).

## 3. Autorreflexão e Pragmatismo

Após desenhar sua proposta, faça uma avaliação crítica dela com base nas nossas regras de negócio:

* A estratégia proposta respeita a diretriz de "pragmatismo e básico bem feito" do nosso `prompt-mestre.md`?
* Estamos introduzindo alguma complexidade desnecessária ou o pipeline proposto esgota de forma eficiente o que precisamos para treinar bons modelos de baseline?

**Ação:** Me apresente a proposta estruturada no chat e sua autorreflexão. Não aplique as transformações finais, não altere o dicionário de features e não faça o commit até que eu aprove a sua estratégia neste Ponto de Controle.
