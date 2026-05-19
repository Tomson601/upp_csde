# Wygeneruj dane regresyjne za pomocą make_regression (np. 1 cecha
# wejściowa, 1 cecha wyjściowa).
# Załaduj model MLPRegressor z scikit-learn.
# Naucz model na zbiorze danych i porównaj wyniki na zbiorze
# testowym.
# Wykreśl porównanie między przewidywanymi a rzeczywistymi
# wartościami (np. wykres punktowy).
from sklearn.datasets import make_regression
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

dane = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)
model = MLPRegressor(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)


model.fit(dane[0], dane[1])
predictions = model.predict(dane[0])

plt.scatter(dane[0], dane[1], color='blue', label='Rzeczywiste wartości')
plt.scatter(dane[0], predictions, color='red', label='Przewidywane wartości')
plt.xlabel('Cecha wejściowa')
plt.ylabel('Cecha wyjściowa')
plt.title('Porównanie przewidywanych i rzeczywistych wartości')
plt.legend()
plt.show()
