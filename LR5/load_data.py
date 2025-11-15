import pandas as pd

df = pd.read_csv('videos.txt', sep=' ', na_values='N/A')
print(df)