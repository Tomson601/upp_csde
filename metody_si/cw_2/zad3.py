# Wczytać od użytkownika 5 liczb całkowitych i wypisać na ekran największą
# oraz najmniejszą z nich.


def find_min_max(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    return print(f"Najmniejsza liczba: {min_num}, Największa liczba: {max_num}")

numbers = []

for i in range(5):
    num = int(input(f"Podaj liczbę całkowitą {i+1}: "))
    numbers.append(num)

find_min_max(numbers)
