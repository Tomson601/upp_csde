import spacy

# Załaduj polski model językowy
nlp = spacy.load("pl_core_news_sm")

# Tekst do analizy
tekst = "Firma produkuje proszki owocowe i regularnie testuje ich jakość w laboratorium."

# Przetwarzanie tekstu przez model spacy
doc = nlp(tekst)

# Wyświetlenie lematów dla każdego tokena
for token in doc:
    print(f"Słowo: {token.text:<15} -> Lemat: {token.lemma_}")
