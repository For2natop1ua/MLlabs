import pandas as pd
import numpy as np

df = pd.read_csv("data.txt", sep=" ")
df = df.replace("N/A", np.nan)

for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df_manh = df.copy()
numeric_cols = df.columns[1:]


def restore_row(idx):
    row = df_manh.loc[idx]
    if not row.isna().any():
        return
    nan_cols = row[row.isna()].index
    best_dist = float("inf")
    best_row = None
    for j, r in df_manh.iterrows():
        if j == idx:
            continue
        if r[nan_cols].isna().any():
            continue
        dist = np.abs(r[numeric_cols] - row[numeric_cols]).sum()
        if dist < best_dist:
            best_dist = dist
            best_row = r
    for col in nan_cols:
        df_manh.at[idx, col] = best_row[col]


for i in range(len(df_manh)):
    restore_row(i)

df_manh = df_manh.round(2)
df_manh.to_csv("TabManhattan.txt", sep=" ", index=False)
print("Файл TabManhattan.txt створено.")
