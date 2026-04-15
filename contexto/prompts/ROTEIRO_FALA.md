# Roteiro do Apresentador — Cola da Banca

> **Instruções de uso:** Cada seção corresponde a um passo da apresentação. Leia o "O que falar" em voz alta. As "Defesas" são respostas prontas para perguntas da banca.

---

## Passo 1 — O Desafio (30 segundos)

### O que falar:

*"Antes de abrir o Jupyter, defini três metas objetivas para o projeto. Recall acima de 70% — porque o custo de deixar escapar um churner é maior do que o de incomodar um cliente satisfeito. Macro F1 acima de 70% — para garantir que o modelo funcione para ambas as classes, não só para a majoritária. E Gap entre treino e teste menor que 10 pontos — para ter certeza de que o modelo não está decorando os dados. Os três foram atingidos."*

### Defesa Técnica:

- **"Por que Recall e não Accuracy?"** → *"Accuracy em dados desbalanceados é enganosa. Um modelo que diz 'ninguém vai cancelar' teria 73.5% de acurácia. Recall mede o que importa: dos churners reais, quantos o modelo detecta."*
- **"Por que definir SLAs antes?"** → *"Sem critério de parada, o projeto vira iteração infinita buscando +0.5pp de AUC. Os SLAs são o contrato comigo mesmo."*

---

## Passo 2 — A História dos Dados (1 minuto)

### O que falar:

*"A EDA revelou um perfil de risco muito claro. O que eu chamo de 'Combo Tóxico': cliente com contrato mensal, fibra óptica, sem suporte técnico e pagando por boleto eletrônico. Cada uma dessas características individualmente já eleva o churn acima da média de 26.5% — combinadas, são praticamente uma sentença."*

*"Segundo achado: a 'UTI dos 6 Meses'. A mediana de permanência de quem cancela é de apenas 10 meses. Metade dos churners sai antes de completar 1 ano. Isso significa que o programa de retenção precisa ser agressivo nos primeiros meses — depois de 24 meses, o risco cai para quase zero."*

### Defesa Técnica:

- **"Por que imputar TotalCharges com 0?"** → *"São 11 registros com tenure=0 — clientes recém-cadastrados que ainda não receberam a primeira cobrança. TotalCharges em branco não é erro de dados, é semântica: sem tempo de casa, sem cobrança acumulada. Imputar com 0 é a tradução correta dessa realidade. Dropar as 11 linhas seria descartar informação valiosa sobre o perfil de entrada dos clientes."*
- **"O Paradoxo da Fibra Óptica?"** → *"O serviço mais caro tem o maior churn — 41.9%. Mas o churn não é do serviço em si, é da falta de 'ecossistema de valor'. Clientes com fibra óptica E suporte técnico têm churn de apenas 15.2%. O problema é vender fibra sem vender o pacote completo."*

---

## Passo 3 — A Cozinha Técnica (1 minuto)

### O que falar:

*"Treinei dois modelos: Regressão Logística e Random Forest. A Random Forest teve nota ligeiramente melhor no 'exercício de casa' — Macro F1 de 0.72 contra 0.71 da LR. Mas quando testamos com dados que o modelo nunca viu, a verdade apareceu."*

*"A Random Forest decorou: gap de 18 pontos percentuais entre treino e teste. Em Data Science, decorar não é aprender — é overfitting. A LR manteve performance quase idêntica entre treino e teste, com gap de apenas 1.5 pontos. E mais: capturou 78% dos churners, contra 65% da RF. Para cada 100 clientes que vão cancelar, a LR identifica 78 a tempo de agir."*

### Defesa Técnica:

- **"Por que não XGBoost?"** → *"Margem teórica de ganho de 1-3pp de Macro F1, mas com 9+ hiperparâmetros para tunar. O custo-benefício não se justificava no tempo disponível, e a explicação na banca seria 'boosting com gradiente + regularização L1/L2'. A LR se explica em uma frase: 'cada feature tem um peso que traduz diretamente o impacto no risco de churn'."*
- **"Por que `class_weight='balanced'` e não SMOTE?"** → *"SMOTE cria exemplos sintéticos da classe minoritária — funciona, mas introduz risco de data leakage se mal implementado e pode gerar overfitting em amostras artificiais. O `class_weight` faz o mesmo efeito por dentro do modelo, penalizando erros na classe minoritária via pesos internos. É mais simples, mais seguro e não altera o dataset original."*
- **"Por que adiar o Scaler?"** → *"Se eu escalonasse os dados antes do split treino/teste, a média e o desvio padrão usados para normalizar incluiriam informação do teste — é data leakage. A solução correta é colocar o StandardScaler dentro do Pipeline do scikit-learn, que garante que o fit do scaler acontece APENAS no treino e o transform é aplicado no teste."*
- **"A Precision de 51% não é baixa?"** → *"É o preço consciente da vigilância. O custo de ligar para um cliente satisfeito oferecendo um desconto é R$5 de tempo do operador. O custo de perder um cliente insatisfeito que cancelou sem ninguém tentar reter é o LTV inteiro — centenas de reais. A 51% de Precision é economicamente racional."*

---

## Passo 4 — A Entrega de Valor (1 minuto)

### O que falar:

*"O modelo não entrega probabilidades — entrega filas de trabalho. Transformei o output do predict_proba em um Score de Risco de 0 a 100 e dividi em três Tiers. 1.640 clientes — 23% da base — caíram no Alto Risco. Uma equipe de 10 operadores fazendo 20 ligações por dia cobre essa fila em 8 dias úteis. Os 2.927 de Baixo Risco recebem um e-mail automático — custo marginal próximo de zero."*

*"Além disso, duas features que criamos carregam narrativa de negócio. O TicketMedio responde 'quanto o cliente realmente gasta por mês desde que entrou'. E o NumServicos mede o quanto o cliente está 'ancorado' no ecossistema. Cancelar um serviço é fácil; cancelar oito ao mesmo tempo gera atrito."*

### Defesa Técnica:

- **"Por que não calibrar o score?"** → *"A Regressão Logística já é naturalmente bem calibrada — confirmamos pela curva de calibração na Etapa 3. Aplicar Platt Scaling ou Isotonic Regression seria adicionar complexidade sem ganho mensurável."*
- **"Os limiares 30/70 são arbitrários?"** → *"São heurísticos, sim. Com dados reais de CAC (custo de aquisição) e LTV (lifetime value), eu calibraria os cortes para o ponto onde custo_de_reter < custo_de_perder. Mas para o MVP, eles criam segmentos gerenciáveis e operacionalmente distintos."*

---

## Passo 5 — Arquitetura de Produção (1 minuto)

### O que falar:

*"Um modelo que vive no Jupyter é uma curiosidade acadêmica. O valor surge quando ele traduz dados em ação. O Synapsee Churn Predictor funciona assim: o gerente arrasta o CSV do mês, e em segundos tem três respostas — quantos clientes estão em risco, quem são eles, e um CSV filtrado pronto para importar no sistema de discagem do call center."*

*"Na arquitetura, separei o módulo analítico do módulo de produção. Se amanhã o modelo for substituído por um XGBoost, apenas o inference.py muda — o app continua funcionando. E durante os testes, capturei um bug de regra de negócio: a tabela estava exibindo ex-clientes na fila de ligação. Estatisticamente correto, mas operacionalmente absurdo — você não liga para quem já cancelou."*

### Defesa Técnica:

- **"Por que dois inference.py?"** → *"O original não preserva o customerID — o modelo não precisa dele. Mas a interface precisa para identificar o cliente na tabela. Criar um módulo separado (inference_app.py) isola essa responsabilidade: mudanças na UI não quebram o pipeline analítico, e vice-versa."*
- **"Por que filtrar ex-clientes?"** → *"É uma questão de OPEX. Cada ligação para um ex-cliente é dinheiro jogado fora — o operador gasta tempo, o ex-cliente se irrita, e o orçamento de retenção é desperdiçado. O filtro garante que 100% do esforço seja direcionado à base ativa."*
- **"O que faria com mais tempo?"** → *"Três coisas: validação temporal (walk-forward ao invés de split aleatório), threshold otimizado via curva Precision-Recall e, com dados de custo real, calibração econômica dos Tiers."*

---

## Frase de Fechamento

> *"O sucesso deste projeto não é o F1-Score. É que o gerente de retenção consegue, em 30 segundos, sair de um CSV bruto para uma fila de ligação priorizada. Isso é produtizar Ciência de Dados."*
