#Zadanie 4 Wykrywanie częstotliwości słów
import spacy
from collections import Counter

# Załaduj model języka polskiego
nlp = spacy.load("pl_core_news_sm")

# Tekst wejściowy
tekst = ("Wlazł kotek na płotek i mruga. Łapa mała, łapka mała, łyżeczka mała, bo kotek jest mały."
"Kotek mały, łapka mała, łyżeczka mała, a płotek jest wysoki. ")

# Przetwórz tekst przez spacy
doc = nlp(tekst)

# Usuń stopwords i interpunkcję, a następnie zamień na małe litery
slowa = [token.text. lower() for token in doc if not token. is_stop and not token.is_punct]

# Użyj Counter do zliczenia wystąpień
czestosc = Counter(slowa)

# Wyświetl 5 najczęstszych słów
print("Najczęściej występujące słowa:")
for slowo, liczba in czestosc.most_common(5):
    print(f"{slowo} + {liczba} razy")
