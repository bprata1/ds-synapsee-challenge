"""
Gera um sample batch de 50 linhas aleatorias do CSV bruto original
para testes de upload na interface Streamlit.
"""
import pandas as pd
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
raw_path = REPO_ROOT / "data" / "raw" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
output_path = REPO_ROOT / "data" / "raw" / "sample_upload_batch.csv"

df = pd.read_csv(raw_path)
sample = df.sample(n=50, random_state=42)
sample.to_csv(output_path, index=False)

print(f"Sample batch gerado: {output_path}")
print(f"Shape: {sample.shape}")
