#Zadanie 3.1 - usuwanie stopwords w spacy
import spacy

# Załaduj model języka polskiego
nlp = spacy.load("pl_core_news_sm")

# Tekst wejściowy
tekst = "Firma produkuje proszki owocowe i regularnie testuje ich jakość w laboratorium."

# Przetwarzanie tekstu
doc = nlp(tekst)

# Filtracja - usuń stopwords i znaki interpunkcyjne
slowa_bez_stopwords = [token.text for token in doc if not token. is_stop and not token.is_punct]

print("słowa po usunięciu stopwords:")
print(slowa_bez_stopwords)
