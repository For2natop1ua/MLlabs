import pandas as pd
import numpy as np

df = pd.read_csv("data.txt", sep=" ")
df = df.replace("N/A", np.nan)

for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.fillna(df.mean(numeric_only=True))
df = df.round(2)
df.to_csv("TabSA.txt", sep=" ", index=False)

print("Файл TabSA.txt створено.")
