# Revisão e Ajustes da Etapa 1 (EDA)

Sua condução da EDA teve excelentes achados estatísticos, mas precisamos ajustar o rigor em qualidade de dados e a organização do projeto antes de fecharmos a Etapa 1.

Suas recomendações estruturais (Imputar com 0, criar `TicketMedio` e usar `class_weight`) são ótimas, MAS elas pertencem às Etapas 2 e 3 do projeto. Não tomaremos decisões de feature engineering ou modelagem antes de darmos a exploração como esgotada.

## Ações Obrigatórias para Finalizar a Etapa 1

### 1. Gestão do "Ponto de Controle" Prematuro

* Acione o **Gatilho B** imediatamente: Registre as três ótimas ideias que você teve (Imputar 0, TicketMedio, e Balanceamento) no arquivo `markdowns-ativos/draft-relatorio.md` sob uma seção temporária chamada *"Ideias a Validar nas Próximas Etapas"*. Assim garantimos a memória, mas voltamos o foco para a EDA.

### 2. Organização do Workspace e Correção do Kernel

* A pasta `data/raw/` é um santuário de dados imutáveis. Mova todas as imagens (`.png`) geradas para a pasta `reports/figures/`.
* Reescreva a primeira célula do notebook `01_eda.ipynb` utilizando a biblioteca `pathlib` ou `os` para garantir que o `DATA_PATH` e os caminhos de salvamento das imagens operem com caminhos absolutos baseados na raiz do repositório. O uso de caminhos relativos quebrou a execução na minha máquina.

### 3. Rigor na Validação de Qualidade de Dados (Fim do Viés)

* Você focou apenas na coluna `TotalCharges`. Quero uma varredura sistêmica adicionada ao final do notebook:
    1. * Execute uma checagem abrangente procurando por anomalias (espaços em branco, strings vazias, '?', 'NA') em **todas** as colunas do dataset.
    2. * Avalie as estatísticas descritivas (`.describe()`) procurando por outliers ilógicos nas variáveis numéricas.

### 4. Reflexão: O que falta para esgotarmos a EDA?

* Após realizar os ajustes acima, faça uma avaliação crítica: Considerando as correlações que você já encontrou e as regras de "pragmatismo e tempo restrito (básico bem feito)" definidas no nosso Prompt Mestre, o que mais precisamos explorar visualmente ou estatisticamente para considerarmos a Etapa 1 100% concluída?
* Apresente sua avaliação de quais análises faltam (se houver alguma) para darmos o "de acordo" final antes de avançarmos para o Pipeline de Features (Fase 2).

**Ação:** Realize os ajustes de código, faça o commit (Gatilho C), atualize o relatório (Gatilho B) e aguarde minha validação da sua resposta ao item 4.
