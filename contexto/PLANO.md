# PLANO.md - Desafio Data Scientist (Synapsee)

1. O que entendi do problema e o que vou resolver

A empresa precisa saber se um usuário está relaxado, neutro ou focado ao receber um estímulo, usando para isso os dados das ondas cerebrais dele (EEG).

Meu objetivo aqui é traduzir esses sinais brutos em informação útil. Vou construir um pipeline que pega esses dados, extrai as características matemáticas importantes (como a energia de certas frequências cerebrais) e passa isso por um modelo de Machine Learning para classificar o estado mental. Além disso, vou criar um "Score de Engajamento" (uma nota de 0 a 100) para facilitar a interpretação do estado do usuário. O usuário final consumirá tudo isso através de uma interface simples na web (Streamlit).

2. Etapas de execução e estimativa de tempo (Total planejado: 16 horas)

    Etapa 1: Entendimento e Limpeza (3h) - Olhar os dados, entender como os sinais se comportam e limpar ruídos óbvios.

    Etapa 2: Criação de Variáveis / Features (4h) - Transformar o sinal bruto de EEG em variáveis que o modelo consiga entender (ex: bandas Alpha/Beta).

    Etapa 3: Treinamento dos Modelos (4h) - Treinar dois modelos preditivos diferentes, compará-los e diagnosticar se estão decorando os dados (overfitting).

    Etapa 4: Lógica do Score de Engajamento (2h) - Criar a regra matemática que calcula a nota de engajamento baseada nas features e na classe prevista.

    Etapa 5: Interface e Documentação (3h) - Subir a tela no Streamlit para testar o modelo e escrever o relatório final de trade-offs.

3. Critérios de Sucesso (Testes de Aceitação)

O projeto será considerado entregue com qualidade se passar estritamente nestes quatro testes práticos:

    Teste de Performance Mínima (Baseline): O modelo escolhido deve atingir uma métrica de avaliação geral (Accuracy / Macro F1-Score) de, no mínimo, 66% nos dados de teste, garantindo uma performance com o dobro de precisão de um chute aleatório (33%).

    Teste de Robustez (Tolerância a Overfitting): A queda de performance do modelo entre os dados de Treinamento e os dados de Teste não pode ser superior a 10 pontos percentuais. (Exemplo: se o modelo atinge 80% no treino, deve atingir no mínimo 70% no teste).

    Teste de Coerência do Score: A lógica matemática implementada deve garantir que 100% dos registros classificados como "Concentrado" resultem em um Score de Engajamento numericamente superior aos registros classificados como "Relaxado".

    Teste de Usabilidade (Pipeline Funcional): A interface no Streamlit deve conseguir receber o upload do arquivo mental-state.csv bruto e exibir as predições (Classe + Score) na tela sem apresentar exceções de código ou quebras de execução (runtime errors).