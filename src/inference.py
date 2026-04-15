"""
Modulo de inferencia para producao (Streamlit e scoring).

Contem:
- preprocess_features(df_raw): Pipeline completo de limpeza e encoding.
- predict_and_score(df_raw, model): Pipeline ponta-a-ponta de limpeza + predicao + score.

IMPORTANTE: Este modulo NAO depende de nenhum arquivo CSV ou modelo carregado
previamente. Ele recebe o dataframe bruto e o modelo como parametros.
"""
import pandas as pd
import numpy as np


def preprocess_features(df):
    """
    Aplica todas as regras de Feature Engineering aprovadas nas Etapas 1 e 2.

    Recebe o dataframe bruto (formato original do Kaggle) e retorna o
    dataframe processado, 100% numerico e pronto para predicao pelo modelo.

    Parametros
    ----------
    df : pd.DataFrame
        DataFrame com as 21 colunas originais da base Telco Customer Churn.

    Retorna
    -------
    pd.DataFrame
        DataFrame processado com 23 features numericas (sem a coluna Churn
        caso ela exista, que tambem eh mapeada).
    """
    df_proc = df.copy()

    # --- 1. Tratamentos da Etapa 1 ---
    # Imputar TotalCharges (11 registros com espaco em branco onde tenure=0)
    df_proc["TotalCharges"] = pd.to_numeric(
        df_proc["TotalCharges"].replace(" ", "0")
    )

    # Criar TicketMedio: gasto medio mensal real do cliente
    df_proc["TicketMedio"] = df_proc.apply(
        lambda row: row["TotalCharges"] / row["tenure"]
        if row["tenure"] > 0
        else 0.0,
        axis=1,
    )

    # Dropar TotalCharges original (multicolinearidade com tenure ~0.83)
    df_proc.drop(columns=["TotalCharges"], inplace=True)

    # --- 2. Encoding das Variaveis (Etapa 2) ---
    # Target (se presente na base)
    if "Churn" in df_proc.columns:
        df_proc["Churn"] = df_proc["Churn"].map({"Yes": 1, "No": 0})

    # Binarias Simples
    df_proc["gender"] = df_proc["gender"].map({"Male": 1, "Female": 0})

    bin_cols = ["Partner", "Dependents", "PhoneService", "PaperlessBilling"]
    for col in bin_cols:
        df_proc[col] = df_proc[col].map({"Yes": 1, "No": 0})

    # Binarias com "No internet service" / "No phone service" colapsadas para 0
    internet_features = [
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
    ]
    for col in internet_features:
        df_proc[col] = df_proc[col].map(
            {"Yes": 1, "No": 0, "No internet service": 0}
        )

    df_proc["MultipleLines"] = df_proc["MultipleLines"].map(
        {"Yes": 1, "No": 0, "No phone service": 0}
    )

    # Ordinal Encoding para Contract (queda monotonica de churn)
    df_proc["Contract"] = df_proc["Contract"].map(
        {"Month-to-month": 0, "One year": 1, "Two year": 2}
    )

    # One-Hot Encoding para InternetService e PaymentMethod
    df_proc = pd.get_dummies(
        df_proc,
        columns=["InternetService", "PaymentMethod"],
        drop_first=True,
        dtype=int,
    )

    # Dropar customerID (sem poder preditivo)
    if "customerID" in df_proc.columns:
        df_proc.drop(columns=["customerID"], inplace=True)

    # --- 3. Engenharia de Features ---
    # NumServicos: indice de ancoragem (soma das 8 flags de servicos)
    servicos_cols = internet_features + ["PhoneService", "MultipleLines"]
    df_proc["NumServicos"] = df_proc[servicos_cols].sum(axis=1)

    return df_proc


def predict_and_score(df_raw, model):
    """
    Pipeline ponta-a-ponta: limpeza + predicao + Score de Risco.

    Orquestra todo o fluxo de inferencia para producao (Streamlit).
    Recebe a base bruta do usuario e o modelo treinado, retornando
    o dataframe com classe prevista, probabilidade e Score de Risco.

    Parametros
    ----------
    df_raw : pd.DataFrame
        DataFrame bruto no formato original do Kaggle (21 colunas).
    model : sklearn Pipeline
        Modelo treinado (carregado via joblib) com .predict() e .predict_proba().

    Retorna
    -------
    pd.DataFrame
        DataFrame com as colunas originais processadas + 3 novas colunas:
        - Churn_Predicted: classe binaria prevista (0 ou 1)
        - Risk_Score: score de risco de 0 a 100 (inteiro)
        - Risk_Tier: faixa de risco ('Baixo Risco', 'Risco Medio', 'Alto Risco')
    """
    # 1. Pre-processar a base bruta com as regras das Etapas 1 e 2
    df_processed = preprocess_features(df_raw)

    # 2. Separar features (dropar Churn se existir, pois eh a variavel alvo)
    feature_cols = [c for c in df_processed.columns if c != "Churn"]
    X = df_processed[feature_cols]

    # 3. Predicao
    df_processed["Churn_Predicted"] = model.predict(X)

    # 4. Score de Risco: probabilidade da classe 1 (Churn) * 100
    probabilidades = model.predict_proba(X)[:, 1]
    df_processed["Risk_Score"] = np.round(probabilidades * 100).astype(int)

    # 5. Clusterizacao em Tiers de Risco
    def classificar_tier(score):
        """Atribui faixa de risco com base no score 0-100."""
        if score <= 30:
            return "Baixo Risco"
        elif score <= 70:
            return "Risco Medio"
        else:
            return "Alto Risco"

    df_processed["Risk_Tier"] = df_processed["Risk_Score"].apply(classificar_tier)

    return df_processed
