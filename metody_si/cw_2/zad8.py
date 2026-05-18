# Napisać program, który pobiera od użytkownika liczbę całkowitą, a następnie:
#   * oblicza sumę cyfr tej liczby
#   * oblicza stosunek średniej arytmetycznej cyfr parzystych do średniej arytmetycznej cyfr nieparzystych.


def sum_of_digits(n):
    digits = []
    for digit in str(n):
        digits.append(int(digit))

    return sum(digits)

def ratio_of_means(n):
    digits = []
    for digit in str(n):
        digits.append(int(digit))

    even_digits = []
    for d in digits:
        if d % 2 == 0:
            even_digits.append(d)

    odd_digits = []
    for d in digits:
        if d % 2 != 0:
            odd_digits.append(d)

    if not even_digits:
        return "Brak cyfr parzystych"
    if not odd_digits:
        return "Brak cyfr nieparzystych"

    mean_even = sum(even_digits) / len(even_digits)
    mean_odd = sum(odd_digits) / len(odd_digits)

    return mean_even / mean_odd

number = int(input("Podaj liczbę całkowitą: "))

print(f"Suma cyfr: {sum_of_digits(number)}")
print(f"Stosunek średnich: {ratio_of_means(number)}")


