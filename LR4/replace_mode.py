import pandas as pd
import numpy as np

df = pd.read_csv("data.txt", sep=" ")
df = df.replace("N/A", np.nan)

for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df_moda = df.copy()

for col in df_moda.columns[1:]:
    mode_val = df_moda[col].mode()
    if len(mode_val) > 0:
        df_moda[col] = df_moda[col].fillna(mode_val.iloc[0])

df_moda = df_moda.round(2)
df_moda.to_csv("TabMODA.txt", sep=" ", index=False)
print("Файл TabMODA.txt створено.")
