import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean

df = pd.read_csv('videos.txt', sep=' ', na_values='N/A')


def impute_missing(row, df, column):
    if pd.isna(row[column]):
        available_cols = [col for col in ['Time_s', 'Positive_count', 'Negative_count'] if
                          col != column and not pd.isna(row[col])]
        distances = []
        for idx, other_row in df.iterrows():
            if idx == row.name or pd.isna(other_row[column]):
                continue
            dist = 0
            count = 0
            for col in available_cols:
                dist += (row[col] - other_row[col]) ** 2
                count += 1
            if count > 0:
                dist = np.sqrt(dist / count)
            else:
                dist = np.inf
            distances.append((dist, other_row[column]))
        if distances:
            closest = min(distances, key=lambda x: x[0])
            return closest[1]
        else:
            return np.nan
    return row[column]


for col in ['Time_s', 'Positive_count', 'Negative_count']:
    df[col] = df.apply(lambda row: impute_missing(row, df, col), axis=1)
df.to_csv('videos_corrected.txt', sep=' ', index=False)
print(df)
