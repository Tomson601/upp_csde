# Z zastosowaniem słowników napisać funkcje, której parametrem będzie
# zmienna zawierająca łańcuch znaków. W funkcji należy policzyć częstość
# występowania każdego znaku. Funkcja powinna zwrócić słownik
# zawierających wszystkie znaki (jako klucze) i ich wystąpienia
# (wartosc).
# Przykładowo, dla: liczZnaki(”Ala ma psa”)
# powinien powstać słownik: ’A’: 1,
# ’l’: 1,
# ’a’: 3,
# ’ ’: 2,
# ’m’: 1,
# ’p’: 1,
# ’s’: 1


def liczZnaki(text):
    character_count = {}

    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

input_text = input("Podaj łańcuch znaków: ")
result = liczZnaki(input_text)
print(result)
