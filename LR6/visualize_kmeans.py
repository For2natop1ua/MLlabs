import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

matplotlib.use('TkAgg')
iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
X = MinMaxScaler().fit_transform(df)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)
centers = kmeans.cluster_centers_

plt.figure(figsize=(10, 6))
colors = ['#e74c3c', '#27ae60', '#3498db']

for i in range(3):
    mask = labels == i
    plt.scatter(X[mask, 0], X[mask, 1],
                c=colors[i], label=f'Кластер {i}', alpha=0.7, s=60, edgecolor='k')

for center in centers:
    plt.scatter(center[0], center[1], c='black', marker='X', s=300, linewidths=3)

plt.scatter([], [], c='black', marker='X', s=300, label='Центри')
plt.xlabel('Sepal Length (норм.)')
plt.ylabel('Sepal Width (норм.)')
plt.title('K-means: Iris')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
