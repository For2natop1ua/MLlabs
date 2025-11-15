import pandas as pd
import numpy as np

df = pd.read_csv("data.txt", sep=r"\s+")
df = df.replace("N/A", np.nan)
df = df.apply(pd.to_numeric, errors='ignore')

df_median = df.copy()
for col in df_median.columns[1:]:
    df_median[col] = df_median[col].fillna(df_median[col].median())

df_median.to_csv("TabMD.txt", sep="\t", index=False)
print("Файл TabMD.txt створено (заміна пропусків медіаною).")
