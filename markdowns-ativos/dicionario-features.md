# Dicionário de Features e Indicadores

Única fonte da verdade para definições técnicas e limites matemáticos das variáveis utilizadas na modelagem.

---

## customerID

* **Descrição:** ID único de identificação do cliente.
* **Origem/Fonte:** Base bruta (Kaggle - Telco Customer Churn).
* **Matemática/Transformação:** Nenhuma. Geralmente descartada na modelagem por não ter poder preditivo.
* **Status:** Raw

## gender

* **Descrição:** Gênero do cliente (Masculino ou Feminino).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## SeniorCitizen

* **Descrição:** Indica se o cliente é idoso/aposentado (1 para sim, 0 para não).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## Partner

* **Descrição:** Indica se o cliente possui um parceiro/cônjuge (Yes, No).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## Dependents

* **Descrição:** Indica se o cliente possui dependentes (Yes, No).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## tenure

* **Descrição:** Número de meses que o cliente permaneceu na empresa (Tempo de vida útil).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## PhoneService

* **Descrição:** Indica se o cliente possui serviço de telefonia (Yes, No).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## MultipleLines

* **Descrição:** Indica se o cliente possui múltiplas linhas telefônicas (Yes, No, No phone service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## InternetService

* **Descrição:** Provedor de serviço de internet do cliente (DSL, Fiber optic, No).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## OnlineSecurity

* **Descrição:** Indica se o cliente possui segurança online adicional contratada (Yes, No, No internet service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## OnlineBackup

* **Descrição:** Indica se o cliente possui serviço de backup online contratado (Yes, No, No internet service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## DeviceProtection

* **Descrição:** Indica se o cliente possui plano de proteção para dispositivos (Yes, No, No internet service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## TechSupport

* **Descrição:** Indica se o cliente possui suporte técnico (Yes, No, No internet service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## StreamingTV

* **Descrição:** Indica se o cliente utiliza serviço de streaming de TV da operadora (Yes, No, No internet service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## StreamingMovies

* **Descrição:** Indica se o cliente utiliza serviço de streaming de filmes da operadora (Yes, No, No internet service).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## Contract

* **Descrição:** Tipo de termo de contrato do cliente (Month-to-month, One year, Two year).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## PaperlessBilling

* **Descrição:** Indica se o cliente optou por faturamento sem papel/digital (Yes, No).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## PaymentMethod

* **Descrição:** Método de pagamento escolhido pelo cliente (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)).
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## MonthlyCharges

* **Descrição:** O valor cobrado mensalmente do cliente.
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## TotalCharges

* **Descrição:** O valor total acumulado cobrado do cliente ao longo de todo o contrato.
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw

## Churn (TARGET)

* **Descrição:** Indica se o cliente cancelou o serviço / deu churn no último mês (Yes or No). Variável alvo preditiva.
* **Origem/Fonte:** Base bruta.
* **Matemática/Transformação:** [A definir na etapa de features]
* **Status:** Raw
