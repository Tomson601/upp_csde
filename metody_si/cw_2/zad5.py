# Napisać program, który pobiera od użytkownika liczbę całkowitą
# dodatnią, a następnie wyświetla na ekranie kolejno wszystkie liczby
# nieparzyste nie większe od podanej liczby. Przykład, dla 15 program
# powinien wyświetlić: 1, 3, 5, 7, 9, 11, 13,15


def print_odd_numbers(n):
    if n < 1:
        return print("Podaj liczbę całkowitą dodatnią.")
    
    odd_numbers = []

    for i in range(1, n + 1):
        if i % 2 != 0:
            odd_numbers.append(str(i))

    return print(", ".join(odd_numbers))

number = int(input("Podaj liczbę całkowitą dodatnią: "))
print_odd_numbers(number)
