import pandas as pd
import numpy as np

df = pd.read_csv("data.txt", sep=" ", engine="python")
df = df.replace("N/A", np.nan)

for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df_norm = df.copy()

for col in df_norm.columns[1:]:
    mn = df_norm[col].min()
    mx = df_norm[col].max()
    df_norm[col] = (df_norm[col] - mn) / (mx - mn)

df_norm = df_norm.round(4)
df_norm.to_csv("TabNorm.txt", sep=" ", index=False)
print("Файл TabNorm.txt створено.")
