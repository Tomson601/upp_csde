from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

# Zadanie: Usuń stop words z poniższego zdania
sentence = "This is an example sentence with some stop words"

# Pobierz listę stop words dla języka polskiego
stop_words = set(stopwords.words('english'))

# Usuń stop words z zdania
filtered_sentence = [word for word in sentence.split() if word.lower() not in stop_words]

# Wyświetl wynik
print(f"Zadanie: Usun stop words z zdania '{sentence}'")
print(f"Wynik: {filtered_sentence}")

# Zadanie: Usun stop words z zdania 'This is an example sentence with some stop words'
# Wynik: ['example', 'sentence', 'stop', 'words']
# [nltk_data] Downloading package stopwords to /root/nltk_data ...
# [nltk_data] Package stopwords is already up-to-date!
