# Wygeneruj dane klasyfikacyjne za pomocą make_classification (np. 2
# cechy wejściowe, 2 klasy). Następnie utwórz i naucz model MLPClassifier z
# biblioteki scikit-learn. Podziel dane na zbiór treningowy i testowy, wykonaj
# predykcję dla danych testowych. Na końcu oceń skuteczność modelu.
from sklearn.datasets import make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

dane = make_classification(n_samples=100, n_features=5, n_classes=2, n_informative=2, n_redundant=0, n_repeated=0, random_state=42)
x, y = dane[0], dane[1]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Dokładność modelu: {accuracy:.4f}")
print("\nRaport klasyfikacji:")
print(classification_report(y_test, y_pred))
