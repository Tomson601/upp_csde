# Załaduj zbiór danych wine z biblioteki scikit-learn.
# Podziel dane na zbiór treningowy oraz testowy.
# Wybierz model klasyfikacyjny MLPClassifier.
# Zdefiniuj kilka konfiguracji hiperparametrów modelu (np. liczba warstw ukrytych, liczba neuronów w warstwie ukrytej, liczba iteracji.
# Naucz model dla różnych konfiguracji hiperparametrów.
# Wykonaj ewaluację modelu i porównaj wyniki.
# Wskaż konfigurację hiperparametrów, która daje najlepszy wynik na zbiorze testowym.
# Krótko opisz wpływ wybranych hiperparametrów na jakość klasyfikacji.

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# 1. Załaduj zbiór danych wine
wine = load_wine()
X, y = wine.data, wine.target

# 2. Podziel dane na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Zdefiniuj kilka konfiguracji hiperparametrów
configurations = [
    {"hidden_layer_sizes": (50,), "max_iter": 500, "name": "1 warstwa (50 neuronów), 500 iteracji"},
    {"hidden_layer_sizes": (100,), "max_iter": 500, "name": "1 warstwa (100 neuronów), 500 iteracji"},
    {"hidden_layer_sizes": (50, 25), "max_iter": 500, "name": "2 warstwy (50, 25 neuronów), 500 iteracji"},
    {"hidden_layer_sizes": (100, 50), "max_iter": 500, "name": "2 warstwy (100, 50 neuronów), 500 iteracji"},
    {"hidden_layer_sizes": (100, 50, 25), "max_iter": 500, "name": "3 warstwy (100, 50, 25 neuronów), 500 iteracji"},
    {"hidden_layer_sizes": (50,), "max_iter": 1000, "name": "1 warstwa (50 neuronów), 1000 iteracji"},
    {"hidden_layer_sizes": (100, 50), "max_iter": 1000, "name": "2 warstwy (100, 50 neuronów), 1000 iteracji"},
]

# 4. Trenuj model dla różnych konfiguracji
results = []

for config in configurations:
    # Wyodrębnij parametry
    name = config.pop("name")
    
    # Utwórz i naucz model
    model = MLPClassifier(random_state=42, **config)
    model.fit(X_train, y_train)
    
    # Wykonaj predykcję
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    # Oblicz dokładność
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    
    # Zapisz wyniki
    results.append({
        "Konfiguracja": name,
        "Dokładność treningowa": f"{train_accuracy:.4f}",
        "Dokładność testowa": f"{test_accuracy:.4f}",
        "Model": model
    })
    
    print(f"\n{'='*70}")
    print(f"Konfiguracja: {name}")
    print(f"{'='*70}")
    print(f"Dokładność treningowa: {train_accuracy:.4f}")
    print(f"Dokładność testowa: {test_accuracy:.4f}")

# 5. Porównaj wyniki
print(f"\n\n{'='*70}")
print("PODSUMOWANIE WYNIKÓW")
print(f"{'='*70}\n")

results_df = pd.DataFrame(results)
print(results_df[["Konfiguracja", "Dokładność treningowa", "Dokładność testowa"]].to_string())

# 6. Znajdź najlepszą konfigurację
best_idx = max(range(len(results)), key=lambda i: float(results[i]["Dokładność testowa"]))
best_config = results[best_idx]

print(f"\n\n{'='*70}")
print("NAJLEPSZA KONFIGURACJA")
print(f"{'='*70}")
print(f"Konfiguracja: {best_config['Konfiguracja']}")
print(f"Dokładność testowa: {best_config['Dokładność testowa']}")

# 7. Szczegółowa ewaluacja najlepszego modelu
print(f"\n\nRaport klasyfikacji dla najlepszej konfiguracji:")
print(classification_report(y_test, best_config['Model'].predict(X_test), target_names=wine.target_names))

# 8. Opis wpływu hiperparametrów
print(f"\n\n{'='*70}")
print("OPIS WPŁYWU HIPERPARAMETRÓW NA JAKOŚĆ KLASYFIKACJI")
print(f"{'='*70}\n")

print("""
1. LICZBA WARSTW UKRYTYCH (Architecture Depth):
   - Model z 1 warstwą jest najprostszy, szybszy w treningu, ale może mieć ograniczoną zdolność
     do uczenia się złożonych wzorców.
   - Dodanie kolejnych warstw umożliwia model na uczenie się bardziej abstrakcyjnych reprezentacji,
     co może poprawić dokładność na skomplikowanych zbiorach danych.
   - Zbyt wiele warstw może prowadzić do przeuczenia się (overfitting).

2. LICZBA NEURONÓW W WARSTWIE UKRYTEJ (Hidden Layer Size):
   - Więcej neuronów pozwala modelowi na przechowywanie więcej informacji o danych treningowych.
   - Za mało neuronów → model może być za prosty, niedouczony (underfitting).
   - Za dużo neuronów → model może się przeuczyć i źle generalizować na nowych danych.
   - Dla danego zbioru danych istnieje optymalna liczba neuronów.

3. LICZBA ITERACJI (max_iter):
   - Więcej iteracji pozwala algorytmowi na lepszą zbieżność do lokalnego minimum.
   - Zwiększenie iteracji zwykle poprawia dokładność, ale do pewnego punktu (convergence).
   - Zbyt mało iteracji → model niedouczony, niezbyt dobre wyniki.
   - Zbyt wiele iteracji → bez dodatkowych korzyści, większy czas obliczeń.

WNIOSKI Z EKSPERYMENTU:
   - Zwiększenie liczby warstw i neuronów generalnie poprawia zdolność uczenia się modelu.
   - Zwększenie liczby iteracji również pomaga w konwergencji modelu.
   - Najlepsza konfiguracja balansuje złożoność modelu z generalizacją na danych testowych.
   - Ważne jest unikanie przeuczenia się - model dobry na zbiorze treningowym, ale słaby na testowym.
""")

