try:
    from sklearn import datasets
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import MinMaxScaler
    print("scikit-learn імпортовано")
except ImportError:
    print("помилка")
    raise

import sklearn
print(f"Версія: {sklearn.__version__}")