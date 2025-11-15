import pandas as pd

df = pd.read_csv('videos_corrected.txt', sep=' ')


def min_max_normalize(series):
    return (series - series.min()) / (series.max() - series.min())


for col in ['Time_s', 'Positive_count', 'Negative_count']:
    df[col] = min_max_normalize(df[col])
df.to_csv('videos_normalized.txt', sep=' ', index=False)
print(df)
