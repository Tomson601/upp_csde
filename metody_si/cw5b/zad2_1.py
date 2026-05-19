#Zadanie 2.1
import nltk


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

tekst = "These farms produce tomatoes, potatoes, and berries."
tokeny = tekst.replace(",", "").replace(".", "").split() # ręczna tokenizacja

lematy = [lemmatizer. lemmatize(token, pos='n') for token in tokeny]
print(" ".join(lematy))
