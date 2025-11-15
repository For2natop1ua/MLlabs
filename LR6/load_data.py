import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

print("Перші 5 рядків:")
print(df.head())
print(f"\nРозмір: {df.shape}")