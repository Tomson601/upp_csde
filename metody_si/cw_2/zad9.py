# Napisać program, dla podanej liczby całkowitej wyświetla jej dzielniki.
# Przykła-dowo, dla liczby 21 dzielniki to: 1, 3, 7, 21.

def print_divisors(n):
    if n == 0:
        return print("Liczba 0 ma nieskończenie wiele dzielników.")
    
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(str(i))

    return print(", ".join(divisors))

number = int(input("Podaj liczbę całkowitą: "))
print_divisors(number)
