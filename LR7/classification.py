from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd


iris = datasets.load_iris()
X, y = iris.data, iris.target
target_names = iris.target_names

df = pd.DataFrame(X, columns=iris.feature_names)
df['species'] = y

print(f"Розмір: {X.shape}")
print(f"Класи: {target_names.tolist()}")
print(f"Перші 3 рядки:")
print(df.head(3).to_string(index=False))

scaler = MinMaxScaler()
X_norm = scaler.fit_transform(X)
df_norm = pd.DataFrame(X_norm, columns=iris.feature_names)
print(f"Дані нормалізовано:")
print(df_norm.head(3).round(4).to_string(index=False))
print(f"Мін: {df_norm.min().min():.1f}, Макс: {df_norm.max().max():.1f}")

X_train, X_test, y_train, y_test = train_test_split(
    X_norm, y, test_size=0.3, random_state=42, stratify=y
)

print(f"Train: {X_train.shape} (70%)")
print(f"Test:  {X_test.shape} (30%)")
print(f"Класи в test: {pd.Series(y_test).value_counts().sort_index().tolist()}")

models = {
    'kNN (k=5)': KNeighborsClassifier(n_neighbors=5),
    'Decision Tree (depth=3)': DecisionTreeClassifier(random_state=42, max_depth=3),
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=200)
}

predictions = {}
print("Навчання моделей:")
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    predictions[name] = y_pred
    acc = accuracy_score(y_test, y_pred)
    print(f"{name}: Accuracy = {acc:.4f}")


def show_metrics(name, y_true, y_pred):
    print(f"\n{name}")
    print(f"Accuracy: {accuracy_score(y_true, y_pred):.4f}")
    report = classification_report(y_true, y_pred, target_names=target_names, output_dict=True)
    metrics = pd.DataFrame(report).transpose().round(4)
    print(metrics.iloc[:3][['precision', 'recall', 'f1-score']].to_string())


for name, y_pred in predictions.items():
    show_metrics(name, y_test, y_pred)


results = []
for name, y_pred in predictions.items():
    acc = accuracy_score(y_test, y_pred)
    results.append({'Модель': name.split(' (')[0], 'Accuracy': round(acc, 4)})

results_df = pd.DataFrame(results)
print("\nПорівняння:")
print(results_df.to_string(index=False))