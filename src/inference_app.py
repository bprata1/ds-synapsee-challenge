"""
Modulo de inferencia para producao (Streamlit).

Variante do inference.py que PRESERVA o customerID no output final,
pois a interface precisa dele para identificar o cliente nas tabelas
e no seletor da sidebar, mesmo que o modelo nao o use para prever.

Contem:
- preprocess_features_for_app(df_raw): Pipeline com preservacao do ID.
- predict_and_score_app(df_raw, model): Pipeline ponta-a-ponta para Streamlit.
- validate_columns(df): Teste de sanidade das colunas do CSV subido.
"""
import pandas as pd
import numpy as np


# Colunas obrigatorias que o pipeline espera encontrar no CSV bruto
COLUNAS_OBRIGATORIAS = [
    "customerID", "gender", "SeniorCitizen", "Partner", "Dependents",
    "tenure", "PhoneService", "MultipleLines", "InternetService",
    "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport",
    "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling",
    "PaymentMethod", "MonthlyCharges", "TotalCharges",
]


def validate_columns(df):
    """
    Teste de sanidade: verifica se todas as colunas obrigatorias
    estao presentes no DataFrame subido pelo usuario.

    Parametros
    ----------
    df : pd.DataFrame
        DataFrame carregado a partir do CSV do usuario.

    Retorna
    -------
    tuple (bool, list)
        (True, []) se todas as colunas estiverem presentes.
        (False, [colunas_faltantes]) caso contrario.
    """
    colunas_faltantes = [c for c in COLUNAS_OBRIGATORIAS if c not in df.columns]
    return (len(colunas_faltantes) == 0, colunas_faltantes)


def preprocess_features_for_app(df):
    """
    Pipeline de Feature Engineering identico ao inference.py,
    porem PRESERVA o customerID em uma coluna separada para
    que a interface Streamlit consiga referenciar cada cliente.

    Parametros
    ----------
    df : pd.DataFrame
        DataFrame bruto no formato original do Kaggle (21 colunas).

    Retorna
    -------
    tuple (pd.DataFrame, pd.Series)
        (df_processado, series_customer_ids)
    """
    df_proc = df.copy()

    # Guardar IDs antes de qualquer transformacao
    customer_ids = df_proc["customerID"].copy()

    # --- 1. Tratamentos da Etapa 1 ---
    df_proc["TotalCharges"] = pd.to_numeric(
        df_proc["TotalCharges"].replace(" ", "0")
    )
    df_proc["TicketMedio"] = df_proc.apply(
        lambda row: row["TotalCharges"] / row["tenure"]
        if row["tenure"] > 0
        else 0.0,
        axis=1,
    )
    df_proc.drop(columns=["TotalCharges"], inplace=True)

    # --- 2. Encoding das Variaveis (Etapa 2) ---
    if "Churn" in df_proc.columns:
        df_proc["Churn"] = df_proc["Churn"].map({"Yes": 1, "No": 0})

    df_proc["gender"] = df_proc["gender"].map({"Male": 1, "Female": 0})

    bin_cols = ["Partner", "Dependents", "PhoneService", "PaperlessBilling"]
    for col in bin_cols:
        df_proc[col] = df_proc[col].map({"Yes": 1, "No": 0})

    internet_features = [
        "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies",
    ]
    for col in internet_features:
        df_proc[col] = df_proc[col].map(
            {"Yes": 1, "No": 0, "No internet service": 0}
        )

    df_proc["MultipleLines"] = df_proc["MultipleLines"].map(
        {"Yes": 1, "No": 0, "No phone service": 0}
    )

    df_proc["Contract"] = df_proc["Contract"].map(
        {"Month-to-month": 0, "One year": 1, "Two year": 2}
    )

    df_proc = pd.get_dummies(
        df_proc,
        columns=["InternetService", "PaymentMethod"],
        drop_first=True,
        dtype=int,
    )

    # Dropar customerID das features (modelo nao usa)
    if "customerID" in df_proc.columns:
        df_proc.drop(columns=["customerID"], inplace=True)

    # --- Robustez OHE: garantir que TODAS as colunas dummy esperadas pelo
    # modelo existam, mesmo que o batch nao contenha todos os valores
    # categoricos (ex: um CSV so com clientes DSL nao gera a coluna
    # 'InternetService_Fiber optic'). Sem isso, sklearn rejeita o input.
    colunas_ohe_esperadas = [
        "InternetService_Fiber optic",
        "InternetService_No",
        "PaymentMethod_Credit card (automatic)",
        "PaymentMethod_Electronic check",
        "PaymentMethod_Mailed check",
    ]
    for coluna in colunas_ohe_esperadas:
        if coluna not in df_proc.columns:
            df_proc[coluna] = 0

    # --- 3. Engenharia de Features ---
    servicos_cols = internet_features + ["PhoneService", "MultipleLines"]
    df_proc["NumServicos"] = df_proc[servicos_cols].sum(axis=1)

    return df_proc, customer_ids


def predict_and_score_app(df_raw, model):
    """
    Pipeline ponta-a-ponta para o Streamlit.

    Diferencial em relacao ao inference.py original:
    - Preserva customerID no output final para exibicao na interface.
    - Inclui validacao de colunas embutida.

    Parametros
    ----------
    df_raw : pd.DataFrame
        DataFrame bruto no formato original do Kaggle.
    model : sklearn Pipeline
        Modelo campeao carregado via joblib.

    Retorna
    -------
    pd.DataFrame
        DataFrame com customerID + features processadas + 3 colunas de output:
        Churn_Predicted, Risk_Score, Risk_Tier.
    """
    # 1. Pre-processar preservando IDs
    df_processed, customer_ids = preprocess_features_for_app(df_raw)

    # 2. Separar features para predicao
    feature_cols = [c for c in df_processed.columns if c != "Churn"]
    X = df_processed[feature_cols]

    # 3. Predicao
    df_processed["Churn_Predicted"] = model.predict(X)

    # 4. Score de Risco
    probabilidades = model.predict_proba(X)[:, 1]
    df_processed["Risk_Score"] = np.round(probabilidades * 100).astype(int)

    # 5. Tiers de Risco
    def classificar_tier(score):
        """Atribui faixa de risco operacional com base no score 0-100."""
        if score <= 30:
            return "Baixo Risco"
        elif score <= 70:
            return "Risco Medio"
        else:
            return "Alto Risco"

    df_processed["Risk_Tier"] = df_processed["Risk_Score"].apply(classificar_tier)

    # 6. Reinserir customerID como primeira coluna
    df_processed.insert(0, "customerID", customer_ids.values)

    return df_processed
