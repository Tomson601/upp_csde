# Wyświetl dataframe ze zbiorami danych. Określ atrybuty zbioru i podaj klasę decyzyjną. 
# Następnie:
# Zaprojektuj Multi-Layer Perceptron przy użyciu dataset Diabetes (regresja) i Iris (klasyfikacja).
# Porównaj wyniki.
from sklearn.datasets import load_diabetes, load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor, MLPClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report
import pandas as pd
import numpy as np

print("="*80)
print("ZBIÓR DANYCH DIABETES (REGRESJA)")
print("="*80)

# Załaduj zbiór danych Diabetes
diabetes = load_diabetes()
X_diabetes = diabetes.data
y_diabetes = diabetes.target

# Wyświetl informacje o zbiorze Diabetes
print(f"\nLiczba próbek: {X_diabetes.shape[0]}")
print(f"Liczba atrybutów: {X_diabetes.shape[1]}")
print(f"Atrybuty: {diabetes.feature_names}")
print(f"Cel predykcji (zmienną zależną): Progresja cukrzycy (wartość ciągła - regresja)")

# Utwórz DataFrame dla Diabetes
df_diabetes = pd.DataFrame(X_diabetes, columns=diabetes.feature_names)
df_diabetes['Target'] = y_diabetes
print(f"\nPierwsze 5 wierszy zbioru Diabetes:")
print(df_diabetes.head())
print(f"\nStatystyki zbioru Diabetes:")
print(df_diabetes.describe())

print("\n" + "="*80)
print("ZBIÓR DANYCH IRIS (KLASYFIKACJA)")
print("="*80)

# Załaduj zbiór danych Iris
iris = load_iris()
X_iris = iris.data
y_iris = iris.target

# Wyświetl informacje o zbiorze Iris
print(f"\nLiczba próbek: {X_iris.shape[0]}")
print(f"Liczba atrybutów: {X_iris.shape[1]}")
print(f"Atrybuty: {iris.feature_names}")
print(f"Klasy decyzyjne: {iris.target_names}")
print(f"Cel predykcji: Rodzaj kwiatu (klasyfikacja na 3 klasy)")

# Utwórz DataFrame dla Iris
df_iris = pd.DataFrame(X_iris, columns=iris.feature_names)
df_iris['Target'] = y_iris
df_iris['Target_Name'] = df_iris['Target'].map({0: iris.target_names[0], 1: iris.target_names[1], 2: iris.target_names[2]})
print(f"\nPierwsze 5 wierszy zbioru Iris:")
print(df_iris.head())
print(f"\nStatystyki zbioru Iris:")
print(df_iris.describe())

print("\n" + "="*80)
print("TRENOWANIE MODELI")
print("="*80)

# ===== DIABETES (REGRESJA) =====
print("\n1. DIABETES - REGRESJA (MLPRegressor)")
print("-" * 80)

# Podziel dane Diabetes
X_train_diab, X_test_diab, y_train_diab, y_test_diab = train_test_split(
    X_diabetes, y_diabetes, test_size=0.2, random_state=42
)

# Trenuj model regresji
model_diabetes = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
model_diabetes.fit(X_train_diab, y_train_diab)

# Predykcja
y_pred_diab_train = model_diabetes.predict(X_train_diab)
y_pred_diab_test = model_diabetes.predict(X_test_diab)

# Metryki dla regresji
mse_train_diab = mean_squared_error(y_train_diab, y_pred_diab_train)
mse_test_diab = mean_squared_error(y_test_diab, y_pred_diab_test)
r2_train_diab = r2_score(y_train_diab, y_pred_diab_train)
r2_test_diab = r2_score(y_test_diab, y_pred_diab_test)

print(f"Typ zadania: Regresja (predykcja wartości ciągłej)")
print(f"Model: MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000)")
print(f"\nWyniki na zbiorze treningowym:")
print(f"  - MSE (Mean Squared Error): {mse_train_diab:.4f}")
print(f"  - R² Score: {r2_train_diab:.4f}")
print(f"\nWyniki na zbiorze testowym:")
print(f"  - MSE (Mean Squared Error): {mse_test_diab:.4f}")
print(f"  - R² Score: {r2_test_diab:.4f}")

# ===== IRIS (KLASYFIKACJA) =====
print("\n\n2. IRIS - KLASYFIKACJA (MLPClassifier)")
print("-" * 80)

# Podziel dane Iris
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(
    X_iris, y_iris, test_size=0.2, random_state=42
)

# Trenuj model klasyfikacji
model_iris = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
model_iris.fit(X_train_iris, y_train_iris)

# Predykcja
y_pred_iris_train = model_iris.predict(X_train_iris)
y_pred_iris_test = model_iris.predict(X_test_iris)

# Metryki dla klasyfikacji
acc_train_iris = accuracy_score(y_train_iris, y_pred_iris_train)
acc_test_iris = accuracy_score(y_test_iris, y_pred_iris_test)

print(f"Typ zadania: Klasyfikacja (predykcja klasy)")
print(f"Model: MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000)")
print(f"\nWyniki na zbiorze treningowym:")
print(f"  - Dokładność: {acc_train_iris:.4f}")
print(f"\nWyniki na zbiorze testowym:")
print(f"  - Dokładność: {acc_test_iris:.4f}")
print(f"\nRaport klasyfikacji:")
print(classification_report(y_test_iris, y_pred_iris_test, target_names=iris.target_names))

# ===== PORÓWNANIE =====
print("\n" + "="*80)
print("PORÓWNANIE WYNIKÓW")
print("="*80)

comparison_df = pd.DataFrame({
    "Zbiór danych": ["Diabetes", "Iris"],
    "Typ zadania": ["Regresja", "Klasyfikacja"],
    "Liczba próbek": [X_diabetes.shape[0], X_iris.shape[0]],
    "Liczba atrybutów": [X_diabetes.shape[1], X_iris.shape[1]],
    "Liczba klas/Output": ["Ciągła", "3 klasy"],
    "Model": ["MLPRegressor", "MLPClassifier"],
    "Metryka testowa": [f"MSE: {mse_test_diab:.4f}", f"Dokładność: {acc_test_iris:.4f}"]
})

print("\n" + comparison_df.to_string(index=False))

print("\n" + "-"*80)
print("WNIOSKI:")
print("-"*80)
print("""
1. DIABETES (REGRESJA):
   - Zadanie: Predykcja wartości ciągłej (progresja cukrzycy)
   - Metryka: MSE (błąd średniokwadratowy) i R² (współczynnik determinacji)
   - R² Score wskazuje, jak dobrze model wyjaśnia wariancję w danych
   - Im wyższy R² (maksymalnie 1.0), tym lepsze dopasowanie modelu
   
2. IRIS (KLASYFIKACJA):
   - Zadanie: Predykcja kategorii (rodzaj kwiatu)
   - Metryka: Dokładność, Precision, Recall, F1-Score
   - Dokładność pokazuje procent prawidłowo zaklasyfikowanych próbek
   - Zbiór Iris jest mniejszy, ale problem jest bardziej jednorodny
   
3. RÓŻNICE:
   - Diabetes: problem regresji (wyjście ciągłe), trudniejszy do przewidzenia
   - Iris: problem klasyfikacji (wyjście dyskretne), zwykle łatwiejszy
   - Diabetes ma mniej próbek (442) niż Iris (150), ale struktura jest inna
   - Dla regresji używamy MLPRegressor, dla klasyfikacji MLPClassifier
   
4. OGÓLNE OBSERWACJE:
   - Oba modele używają tej samej architekury (2 warstwy ukryte: 100, 50 neuronów)
   - Iris zwykle osiąga wyższą dokładność ze względu na naturalnie wyodrębnialne klasy
   - Diabetes może mieć gorszą wydajność ze względu na szum w danych i większą złożoność
   - Oba zadania wymagają odpowiednich metryk ewaluacji (MSE dla regresji, dokładność dla klasyfikacji)
""")

