"""
Aplicacao Streamlit para inferencia de Churn e Score de Risco.

Interface MVP para a equipe operacional de retencao:
- Upload de CSV bruto com dados de clientes
- Processamento automatico via pipeline aprovado
- KPIs executivos (total processado, % alto risco)
- Tabela de acao ordenada por score
- Seletor de cliente individual na sidebar
- Filtro por Tier de Risco + download do CSV filtrado

Uso: streamlit run app.py
"""
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import sys

# --- Configuracao de caminhos ---
REPO_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from inference_app import predict_and_score_app, validate_columns

# --- Configuracao da pagina ---
st.set_page_config(
    page_title="Synapsee Churn Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_resource
def carregar_modelo():
    """Carrega o modelo campeao uma unica vez (cache do Streamlit)."""
    return joblib.load(REPO_ROOT / "models" / "campeao.joblib")


modelo = carregar_modelo()


# ============================================================
# HEADER
# ============================================================
st.title("📊 Synapsee Churn Predictor")
st.markdown(
    "Plataforma de inferencia para predicao de **cancelamento (Churn)** "
    "e calculo do **Score de Risco** (0-100) em bases de clientes de telecom."
)
st.divider()

# ============================================================
# UPLOAD
# ============================================================
st.subheader("1. Upload do CSV de Clientes")
st.caption(
    "Envie um arquivo CSV no formato original do Kaggle "
    "(Telco Customer Churn). O sistema processara automaticamente."
)

arquivo_csv = st.file_uploader(
    "Arraste ou selecione o arquivo CSV",
    type=["csv"],
    help="O arquivo deve conter as colunas originais do dataset Telco Customer Churn.",
)

if arquivo_csv is not None:
    # --- Leitura do CSV ---
    try:
        df_upload = pd.read_csv(arquivo_csv)
    except Exception as e:
        st.error(f"Erro ao ler o CSV: {e}")
        st.stop()

    # --- Teste de Sanidade ---
    colunas_ok, colunas_faltantes = validate_columns(df_upload)

    if not colunas_ok:
        st.warning(
            f"⚠️ O arquivo enviado esta incompleto. "
            f"Faltam as seguintes colunas obrigatorias: "
            f"**{', '.join(colunas_faltantes)}**. "
            f"Verifique se o CSV esta no formato correto do Telco Customer Churn."
        )
        st.stop()

    st.success(f"✅ Arquivo carregado com sucesso! **{len(df_upload)} clientes** encontrados.")

    # --- Processamento ---
    with st.spinner("Processando pipeline de inferencia..."):
        df_resultado = predict_and_score_app(df_upload, modelo)

    # ============================================================
    # KPIs EXECUTIVOS
    # ============================================================
    st.divider()
    st.subheader("2. Visao Executiva")

    total_clientes = len(df_resultado)
    clientes_alto_risco = len(df_resultado[df_resultado["Risk_Tier"] == "Alto Risco"])
    pct_alto_risco = (clientes_alto_risco / total_clientes) * 100
    score_medio = df_resultado["Risk_Score"].mean()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Processados", f"{total_clientes:,}")
    col2.metric("Alto Risco", f"{clientes_alto_risco:,}")
    col3.metric("% Alto Risco", f"{pct_alto_risco:.1f}%")
    col4.metric("Score Medio", f"{score_medio:.0f}/100")

    # ============================================================
    # TABELA DE ACAO
    # ============================================================
    st.divider()
    st.subheader("3. Tabela de Acao (Ordenada por Risco)")

    # Colunas de exibicao para a tabela principal
    colunas_exibicao = ["customerID", "Risk_Score", "Risk_Tier", "Churn_Predicted"]
    # Adicionar Churn real se existir na base
    if "Churn" in df_resultado.columns:
        colunas_exibicao.append("Churn")

    df_tabela = df_resultado[colunas_exibicao].sort_values(
        "Risk_Score", ascending=False
    )

    st.dataframe(
        df_tabela,
        width="stretch",
        height=400,
        column_config={
            "customerID": st.column_config.TextColumn("ID do Cliente"),
            "Risk_Score": st.column_config.ProgressColumn(
                "Score de Risco",
                min_value=0,
                max_value=100,
                format="%d",
            ),
            "Risk_Tier": st.column_config.TextColumn("Tier de Risco"),
            "Churn_Predicted": st.column_config.NumberColumn(
                "Churn Previsto", format="%d"
            ),
        },
    )

    # ============================================================
    # FILTRO OPERACIONAL + DOWNLOAD
    # ============================================================
    st.divider()
    st.subheader("4. Extracao Inteligente (Filtro Operacional)")

    filtro_tier = st.radio(
        "Selecione o Tier de Risco para filtrar:",
        options=["Todos", "Alto Risco", "Risco Medio", "Baixo Risco"],
        horizontal=True,
    )

    if filtro_tier == "Todos":
        df_filtrado = df_resultado
    else:
        df_filtrado = df_resultado[df_resultado["Risk_Tier"] == filtro_tier]

    st.info(f"**{len(df_filtrado)}** clientes no filtro selecionado.")

    # Botao de download do CSV filtrado
    csv_filtrado = df_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        label=f"⬇️ Baixar CSV ({filtro_tier})",
        data=csv_filtrado,
        file_name=f"churn_predicoes_{filtro_tier.lower().replace(' ', '_')}.csv",
        mime="text/csv",
    )

    # ============================================================
    # SIDEBAR — SELETOR DE CLIENTE
    # ============================================================
    st.sidebar.header("🔍 Consulta por Cliente")
    st.sidebar.caption("Selecione um cliente para ver seus detalhes.")

    # Lista de IDs ordenada pelo score (mais arriscados primeiro)
    ids_ordenados = (
        df_resultado.sort_values("Risk_Score", ascending=False)["customerID"]
        .tolist()
    )

    cliente_selecionado = st.sidebar.selectbox(
        "Customer ID",
        options=ids_ordenados,
    )

    if cliente_selecionado:
        dados_cliente = df_resultado[
            df_resultado["customerID"] == cliente_selecionado
        ].iloc[0]

        # Exibir Score de Risco com destaque visual
        score = dados_cliente["Risk_Score"]
        tier = dados_cliente["Risk_Tier"]

        # Cor do tier
        if tier == "Alto Risco":
            cor_tier = "🔴"
        elif tier == "Risco Medio":
            cor_tier = "🟡"
        else:
            cor_tier = "🟢"

        st.sidebar.metric("Score de Risco", f"{score}/100")
        st.sidebar.markdown(f"**Tier:** {cor_tier} {tier}")
        st.sidebar.markdown(
            f"**Churn Previsto:** {'Sim' if dados_cliente['Churn_Predicted'] == 1 else 'Nao'}"
        )

        # Churn real se disponivel
        if "Churn" in dados_cliente.index:
            churn_real = dados_cliente["Churn"]
            st.sidebar.markdown(
                f"**Churn Real:** {'Sim' if churn_real == 1 else 'Nao'}"
            )

        st.sidebar.divider()
        st.sidebar.caption("Dados completos do cliente:")
        st.sidebar.json(dados_cliente.to_dict())

else:
    # Estado inicial — sem upload
    st.info(
        "👆 Envie um arquivo CSV para iniciar a analise. "
        "Voce pode usar o arquivo `data/raw/sample_upload_batch.csv` para testes."
    )
