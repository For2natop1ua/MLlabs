import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler

iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    scaler.fit_transform(df),
    columns=iris.feature_names
)

print("Нормалізовані дані (перші 5):")
print(df_normalized.head())
print("\nMin/Max:")
print(df_normalized.agg(['min', 'max']).round(4))