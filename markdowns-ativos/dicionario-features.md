# Dicionário de Features e Indicadores

Única fonte da verdade para definições técnicas e limites matemáticos das variáveis utilizadas na modelagem.

---

## customerID

* **Descrição:** ID único de identificação do cliente.
* **Origem/Fonte:** Base bruta (Kaggle - Telco Customer Churn).
* **Matemática/Transformação:** Descartada, pois não agrega poder preditivo.
* **Status:** Dropada

## gender

* **Descrição:** Gênero do cliente (Masculino ou Feminino).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mapeada para Male=1, Female=0
* **Status:** Processed

## SeniorCitizen

* **Descrição:** Indica se o cliente é idoso/aposentado (1 para sim, 0 para não).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Já contida no formato 0/1 originalmente. Manter inalterada.
* **Status:** Processed

## Partner

* **Descrição:** Indica se o cliente possui um parceiro/cônjuge (Yes, No).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mapeada para Yes=1, No=0
* **Status:** Processed

## Dependents

* **Descrição:** Indica se o cliente possui dependentes (Yes, No).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mapeada para Yes=1, No=0
* **Status:** Processed

## tenure

* **Descrição:** Número de meses que o cliente permaneceu na empresa (Tempo de vida útil).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Manter inalterada. Escalonamento ocorrerá na própria pipeline de modelagem da Etapa 3, se modelo exigir.
* **Status:** Processed

## PhoneService

* **Descrição:** Indica se o cliente possui serviço de telefonia (Yes, No).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mapeada para Yes=1, No=0
* **Status:** Processed

## MultipleLines

* **Descrição:** Indica se o cliente possui múltiplas linhas telefônicas (Yes, No, No phone service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mapeada para Yes=1, No=0, No phone service=0. (A ausência de serviço é semanticamente igual a não ter múltiplas linhas).
* **Status:** Processed

## InternetService

* **Descrição:** Provedor de serviço de internet do cliente (DSL, Fiber optic, No).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** One-Hot Encoding com `drop_first=True`. Original é dropada.
* **Status:** Dropada

## InternetService_Fiber optic

* **Descrição:** Dummy para clientes que têm serviço de internet por fibra óptica.
* **Origem/Fonte:** Derivada de InternetService, gerada via OHE.
* **Matemática/Transformação:** Dummy. O baseline oculto é InternetService_DSL.
* **Status:** Ativa

## InternetService_No

* **Descrição:** Dummy para clientes sem serviço de internet.
* **Origem/Fonte:** Derivada de InternetService, gerada via OHE.
* **Matemática/Transformação:** Dummy. O baseline oculto é InternetService_DSL.
* **Status:** Ativa

## OnlineSecurity

* **Descrição:** Indica se o cliente possui segurança online adicional contratada (Yes, No, No internet service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mapeada para Yes=1, No=0, No internet service=0.
* **Status:** Processed

## OnlineBackup

* **Descrição:** Indica se o cliente possui serviço de backup online contratado (Yes, No, No internet service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mapeada para Yes=1, No=0, No internet service=0.
* **Status:** Processed

## DeviceProtection

* **Descrição:** Indica se o cliente possui plano de proteção para dispositivos (Yes, No, No internet service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mapeada para Yes=1, No=0, No internet service=0.
* **Status:** Processed

## TechSupport

* **Descrição:** Indica se o cliente possui suporte técnico (Yes, No, No internet service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mapeada para Yes=1, No=0, No internet service=0.
* **Status:** Processed

## StreamingTV

* **Descrição:** Indica se o cliente utiliza serviço de streaming de TV da operadora (Yes, No, No internet service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mapeada para Yes=1, No=0, No internet service=0.
* **Status:** Processed

## StreamingMovies

* **Descrição:** Indica se o cliente utiliza serviço de streaming de filmes da operadora (Yes, No, No internet service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mapeada para Yes=1, No=0, No internet service=0.
* **Status:** Processed

## Contract

* **Descrição:** Tipo de termo de contrato do cliente (Month-to-month, One year, Two year).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Tratamento Ordinal. Mapeado para Month-to-month=0, One year=1, Two year=2 em virtude da queda monotônica observada no churn.
* **Status:** Processed

## PaperlessBilling

* **Descrição:** Indica se o cliente optou por faturamento sem papel/digital (Yes, No).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mapeada para Yes=1, No=0
* **Status:** Processed

## PaymentMethod

* **Descrição:** Método de pagamento escolhido pelo cliente.
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** One-Hot Encoding com `drop_first=True`. Variável original dropada.
* **Status:** Dropada

## PaymentMethod_Credit card (automatic)

* **Descrição:** Dummy de pagamento via cartão de crédito.
* **Origem/Fonte:** Derivada de PaymentMethod via OHE.
* **Matemática/Transformação:** Dummy. O baseline oculto é Bank transfer (automatic).
* **Status:** Ativa

## PaymentMethod_Electronic check

* **Descrição:** Dummy de pagamento via electronic check (perfil com maior risco de churn da ED A).
* **Origem/Fonte:** Derivada de PaymentMethod via OHE.
* **Matemática/Transformação:** Dummy. O baseline oculto é Bank transfer (automatic).
* **Status:** Ativa

## PaymentMethod_Mailed check

* **Descrição:** Dummy de pagamento via mailed check.
* **Origem/Fonte:** Derivada de PaymentMethod via OHE.
* **Matemática/Transformação:** Dummy. O baseline oculto é Bank transfer (automatic).
* **Status:** Ativa

## MonthlyCharges

* **Descrição:** O valor cobrado mensalmente do cliente.
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mantida inalterada. O escalonamento acontecerá internamente na modelagem via pipeline scikit-learn.
* **Status:** Processed

## TotalCharges

* **Descrição:** O valor total acumulado cobrado do cliente ao longo de todo o contrato.
* **Origem/Fonte:** Base bruta.
* **Fórmula/Filtro:** 11 registros com espaço em branco (tenure=0) imputados com 0 antes do drop.
* **Status:** Dropada — Substituída pela feature derivada `TicketMedio` para mitigar multicolinearidade com `tenure` (correlação ~0.83).

## TicketMedio

* **Descrição:** Gasto médio mensal real do cliente ao longo de sua permanência. Representa o valor médio por mês de contrato efetivamente cobrado.
* **Origem/Fonte:** Feature derivada (Etapa 1 — EDA).
* **Fórmula/Filtro:** `TicketMedio = TotalCharges / tenure` quando `tenure > 0`; `0` quando `tenure == 0` (clientes recém-chegados sem histórico de gasto).
* **Status:** Ativa

## NumServicos

* **Descrição:** Quantificador de 'ancoragem' à provedora de internet. É a soma de todos os serviços ativados para aquele cliente.
* **Origem/Fonte:** Feature derivada (Etapa 2 - Pipeline de Features).
* **Fórmula/Filtro:** Soma das colunas binárias já mapeadas para 0 e 1: `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`, `MultipleLines` e `PhoneService`.
* **Status:** Ativa

## Churn (TARGET)

* **Descrição:** Indica se o cliente cancelou o serviço / deu churn no último mês (Yes or No). Variável alvo preditiva.
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** Mapeada para Yes=1, No=0.
* **Status:** Processed

## Risk_Score

* **Descrição:** Score de Risco de churn do cliente, em escala contínua de 0 a 100. Quanto maior, maior a probabilidade estimada de cancelamento.
* **Origem/Fonte:** Feature derivada (Etapa 4 — Score de Risco).
* **Fórmula/Filtro:** `Risk_Score = round(predict_proba(X)[:, 1] * 100)`. Transformação monotônica direta da probabilidade da classe Churn emitida pelo modelo campeão (Logistic Regression).
* **Limites:** Mínimo observado: 2 | Máximo observado: 94. Média Churn=Sim: 67.4 | Média Churn=Não: 32.6 (separação de 34.8 pontos).
* **Status:** Ativa (output de inferência, não input de treino)

## Risk_Tier

* **Descrição:** Faixa de prioridade operacional derivada do Risk_Score para direcionar ações de retenção.
* **Origem/Fonte:** Feature derivada (Etapa 4 — Score de Risco).
* **Fórmula/Filtro:** Baixo Risco (0-30) | Risco Médio (31-70) | Alto Risco (71-100).
* **Distribuição:** Baixo Risco: 2.927 clientes (41.6%) | Risco Médio: 2.476 (35.2%) | Alto Risco: 1.640 (23.3%).
* **Status:** Ativa (output de inferência, não input de treino)
