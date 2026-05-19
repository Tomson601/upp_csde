#Zadanie 6.1 - Stemming
import spacy

# Załaduj model spaCy dla języka polskiego
nlp = spacy.load("pl_core_news_sm")

tekst = ("Proszki owocowe są popularnym składnikiem w przemyśle spożywczym. "
"Firma używa owocow do produkcji naturalnych proszków, ktore zachowują smak i aromat świeżych owoców.")

doc = nlp(tekst)

# Usuwamy stopwords i interpunkcję
slowa = [token. text. lower() for token in doc if not token.is_stop and not token.is_punct]

# Symulowany stemming - obcinamy do 5 pierwszych liter
stemy = [slowo[:5] for slowo in slowa]

# Wyświetlenie
print("Symulowany stemming (obcięcie do 5 znaków):")
for slowo, stem in zip(slowa, stemy):
    print(f"{slowo:<20} + {stem}")
