import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
scaler = MinMaxScaler()
X = scaler.fit_transform(df)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)
centers = kmeans.cluster_centers_

print("Мітки (перші 10):", labels[:10].tolist())
print(f"Розподіл: {pd.Series(labels).value_counts().sort_index().tolist()}")
print("\nЦентри кластерів:")
print(pd.DataFrame(centers, columns=iris.feature_names).round(4))