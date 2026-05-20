import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#a
df = pd.read_csv('Pumpkin_Seeds_Dataset.csv', sep=';', encoding='latin-1')

print("Pierwsze 5 wierszy:")
print(df.head())

x = df.iloc[:, :-1]
y = df.iloc[:, -1]

#b
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#c
# W tej petli zamieniłem przecinki na kropki w celu późniejszego przekonwertwanian na floaty
for col in X_train.columns:
    X_train[col] = X_train[col].astype(str).str.replace(',', '.', regex=False)
    X_test[col] = X_test[col].astype(str).str.replace(',', '.', regex=False)

X_train = X_train.astype(float)
X_test = X_test.astype(float)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#d
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

#e
mlp = MLPClassifier(
    hidden_layer_sizes=(100,),
    activation='relu',
    max_iter=5000,
    random_state=42,
    verbose=False
)

mlp.fit(X_train_scaled, y_train_encoded)

#f
y_pred = mlp.predict(X_test_scaled)
accuracy = accuracy_score(y_test_encoded, y_pred)

print("EWALUACJA NA ZBIORZE TESTOWYM:\n")
print(f"Dokładność (Accuracy): {accuracy:.4f} ({accuracy*100:.2f}%)")
print("\nRaport klasyfikacji:")
print(classification_report(y_test_encoded, y_pred, target_names=label_encoder.classes_))
