import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# Pobierz zasób "vader_lexicon"
nltk.download('vader_lexicon')

# Zadanie: Określ sentyment poniższego zdania
sentence = "To jest najlepszy film, jaki kiedykolwiek widziałem!"

# Analizuj sentyment zdania
sentiment_scores = SentimentIntensityAnalyzer().polarity_scores(sentence)

# Określ wynik na podstawie wartości sentymentu
if sentiment_scores['compound'] >= 0.05:
    sentiment = "Pozytywny"
elif sentiment_scores['compound'] <= -0.05:
    sentiment = "Negatywny"
else:
    sentiment = "Neutralny"

# Wyświetl wynik
print(f"Zadanie: Okresl sentyment zdania '{sentence}'")
print(f"Wynik: {sentiment} - Analiza sentymentu: {sentiment_scores}")

# Zadanie: Określ sentyment zdania 'To jest najlepszy film, jaki kiedykolwiek widziałem!'
# Wynik: Neutralny - Analiza sentymentu: {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
# [nltk_data] Downloading package vader_lexicon to /root/nltk_data ...