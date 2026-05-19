#Zadanie 5.1 - Sentiment Analyzer do oceniania opinii rolników na podstawie słów pozytywnych i negatywnych.
# Opinie użytkownikow (surowe dane)
opinie = [
    "Ten nawoz jest rewelacyjny, efekty były widoczne od razu.",
    "To najgorszy produkt, jaki kupiłem. Strata pieniędzy.",
    "Rośliny wyrosły zdrowe i silne, jestem bardzo zadowolony.",
    "Nie działa, zupełnie bezużyteczny środek.",
    "Działa dobrze, ale mógłby być tańszy.",
    "Ziemia wyglądała gorzej niż wcześniej. Nie polecam.",
    "Super skuteczność! Plony o 30% wyższe.",
    "Efekty były przeciętne, nic specjalnego.",
    "Totalna katastrofa. Wszystko uschło.",
    "Rewelacja, działa lepiej niż się spodziewałem!"
]

# Prosty słownik emocjonalny
pozytywne = {"rewelacyjny", "zadowolony", "zdrowe", "silne", "dobrze", "super", "wyższe", "rewelacja", "skuteczność", "działa"}
negatywne = {"najgorszy", "strata", "nie", "bezużyteczny", "gorszy", "katastrofa", "uschło"}

import spacy
nlp = spacy.load("pl_core_news_sm")

def ocen_sentiment(text):
    doc = nlp(text.lower())
    pos = sum(1 for token in doc if token.lemma_ in pozytywne)
    neg = sum(1 for token in doc if token.lemma_ in negatywne)

    if pos > neg:
        return "pozytywna"
    elif neg > pos:
        return "negatywna"
    else:
        return "neutralna"

# testowanie analizatora
for opinia in opinie:
    wynik = ocen_sentiment(opinia)
    print(f"Opinia: \"{opinia}\"\n+ Ocena sentymentu: {wynik}\n")
