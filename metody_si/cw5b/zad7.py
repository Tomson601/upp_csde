import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction. text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Przykładowe dane - 50 opinii (rozszerz je później)
data =[
    {'opinia': 'Słaba jakość, produkt nie spełnił oczekiwań. Szkoda pieniędzy.', 'etykieta': 0},
    {'opinia': 'Nie widzę żadnych efektow, to strata pieniędzy. Szkoda pieniędzy.', 'etykieta': 0},
    {'opinia': 'Nie widzę żadnych efektow, to strata pieniędzy.', 'etykieta': 0},
    {'opinia': 'Słaba jakość, produkt nie spełnił oczekiwań. Szkoda pieniędzy.', 'etykieta': 0},
    {'opinia': 'Słaba jakość, produkt nie spełnił oczekiwań.', 'etykieta': 0},
    {'opinia': 'Plony były rekordowe w tym sezonie, świetny produkt!', 'etykieta': 1},
    {'opinia': 'Nie widzę żadnych efektow, to strata pieniędzy. Szkoda pieniędzy.', 'etykieta': 0},
    {'opinia': 'Ziemia zrobiła się twarda, nie polecam tego nawozu. Szkoda pieniędzy.', 'etykieta': 0},
    {'opinia': 'Nie widzę żadnych efektow, to strata pieniędzy.', 'etykieta': 0},
    {'opinia': 'Ten nawoz bardzo pomogł moim roślinom, plony były większe. Działało zgodnie z oczekiwaniami.', 'etykieta': 1},
    {'opinia': 'Nie widzę żadnych efektów, to strata pieniędzy. Szkoda pieniędzy.', 'etykieta': 0},
    {'opinia': 'Ten nawoz bardzo pomog moim roślinom, plony były większe. Działało zgodnie z oczekiwaniami.', 'etykieta': 1},
    {'opinia': 'Niestety nawoz nie zadziałał, jak obiecywano.', 'etykieta': 0},
    {'opinia': 'Niestety nawoz nie zadziałał, jak obiecywano.', 'etykieta': 0},
    {'opinia': 'Nie widzę żadnych efektow, to strata pieniędzy.', 'etykieta': 0}
]

# Podział na dane treningowe i testowe
X_train, X_test, y_train, y_test = train_test_split(
    df["opinia"], df["etykieta"], test_size=0.3, random_state=42
)

vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer. transform(x_test)

y_pred = model.predict(x_test_tfidf)
print("Raport klasyfikacji:\n", classification_report(y_test, y_pred))
print("Macierz pomytek:\n", confusion_matrix(y_test, y_pred))
