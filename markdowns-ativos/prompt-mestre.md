# Diretrizes Centrais do Projeto: Desafio Synapsee (Data Scientist)

## 1. Contexto e Objetivo Core
O desafio consiste em processar o "EEG Brainwave Dataset: Mental State" (Kaggle) para construir um pipeline analítico ponta a ponta. O objetivo é classificar 3 estados mentais (relaxado, neutro, concentrado) usando sinais de EEG, e derivar uma lógica matemática coerente para um "Score de Engajamento" (escala de 0 a 100).

## 2. Escopo de Entregas Obrigatórias
O projeto deve estritamente conter as seguintes entregas:
* **EDA (Notebook):** Um arquivo Jupyter (`.ipynb`) com a análise exploratória, distribuição dos sinais, correlações entre canais e diferenças entre os estados mentais.
* **Pipeline de Features:** Script focado na extração de características do sinal de EEG (ex: bandas de frequência Alpha/Beta/Theta, PSD - densidade espectral de potência, estatísticas temporais). Cada feature deve ter justificativa documentada.
* **Modelagem Preditiva:** Treinamento, validação e comparação obrigatória de pelo menos **duas abordagens diferentes** de algoritmos. Discussão explícita sobre a capacidade de generalização.
* **Métrica Contínua:** Implementação e documentação do Score de Engajamento.
* **Plataforma de Inferência:** Uma interface `Streamlit` funcional que receba um arquivo CSV de upload e retorne a predição da classe + score.
* **Relatório Final:** Documento (Draft mantido no Git) registrando o que funcionou, os trade-offs e lições aprendidas.

## 3. Restrições e Mindset (Pragmatismo)
* **Tempo Restrito:** O projeto deve ser concluído rapidamente. Foco absoluto no "básico bem feito".
* **Defesa Técnica ao Vivo:** O usuário precisará explicar o código e as escolhas de modelagem para uma banca avaliadora. Portanto, o código deve ser extremamente limpo, interpretável e com as decisões documentadas (zero "black-boxes" inexplicáveis).
* **Governança Estrita:** Todas as decisões arquiteturais (imputação, seleção de features, algoritmos) devem passar pelo crivo do usuário (co-piloto) antes de serem codificadas.

## 4. Critérios de Aceitação (SLAs)
1. **Baseline:** Acurácia / Macro F1-Score mínimo de 66% nos dados de teste.
2. **Robustez:** Queda máxima de 10 pontos percentuais de performance entre Treino e Teste (tolerância a overfitting).
3. **Score:** A nota de engajamento deve ser matematicamente coerente (ex: predição de "Concentrado" deve gerar score maior que "Relaxado").
4. **Deploy:** A interface Streamlit deve executar sem erros de compilação ou exceções durante o upload.