import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
import matplotlib
matplotlib.use('TkAgg')
iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
X = MinMaxScaler().fit_transform(df)
data = np.array(X)


def forel_clustering(data, R=0.25, min_points=15):
    n = len(data)
    labels = np.full(n, -1)
    centers = []
    cluster_id = 0
    remaining = list(range(n))

    while len(remaining) > min_points:
        idx = np.random.choice(remaining)
        center = data[idx].copy()
        prev_center = None

        while prev_center is None or np.linalg.norm(center - prev_center) > 1e-5:
            prev_center = center.copy()
            distances = np.linalg.norm(data[remaining] - center, axis=1)
            in_sphere = np.array(remaining)[distances <= R]
            if len(in_sphere) == 0:
                break
            center = data[in_sphere].mean(axis=0)

        distances = np.linalg.norm(data[remaining] - center, axis=1)
        cluster_idx = np.array(remaining)[distances <= R]

        if len(cluster_idx) >= min_points:
            labels[cluster_idx] = cluster_id
            centers.append(center)
            remaining = [i for i in remaining if i not in cluster_idx]
            cluster_id += 1
        else:
            break

    return labels, np.array(centers)


R = 0.25
labels_forel, centers_forel = forel_clustering(data, R)

print(f"Знайдено кластерів: {len(centers_forel)}")
print("Центри:")
print(pd.DataFrame(centers_forel, columns=iris.feature_names).round(4))

plt.figure(figsize=(10, 6))
valid = labels_forel != -1
unique_labels = np.unique(labels_forel[valid])
cmap = plt.colormaps.get_cmap('Set1')
colors = [cmap(i) for i in range(len(unique_labels))]

for i, cid in enumerate(unique_labels):
    mask = labels_forel == cid
    plt.scatter(data[mask, 0], data[mask, 1],
                color=colors[i], label=f'FOREL Кластер {int(cid)}',
                alpha=0.7, s=60, edgecolor='k')

for center in centers_forel:
    plt.scatter(center[0], center[1], facecolors='none', edgecolors='black',
                marker='o', s=300, linewidths=3)

plt.scatter([], [], facecolors='none', edgecolors='black', marker='o', s=300, label='Центри')
plt.xlabel('Sepal Length (норм.)')
plt.ylabel('Sepal Width (норм.)')
plt.title(f'FOREL: Iris (R={R})')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()