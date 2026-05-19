#6.2 Steeming dla słownika ang
from nltk.stem import PorterStemmer

# Inicjalizacja stemmera Portera
stemmer = PorterStemmer()

#o proszkach porzeczkowych
tekst = "The company produces blackcurrant powders and uses them in various food supplements and beverages."

# Ręczna tokenizacja - usunięcie kropek i przecinków, podział po spacji
tekst_clean = tekst.replace(".", "").replace(",", "").lower()
tokeny = tekst_clean.split()

# Zastosowanie stemmingu
stemy = [stemmer.stem(token) for token in tokeny]

# Wyświetlenie wyników
print("Stemming (PorterStemmer) - ręczna tokenizacja:")
for slowo, stem in zip(tokeny, stemy):
    print(f"{slowo:<15} + {stem}")
