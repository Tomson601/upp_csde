# Napisać program, który wczytuje od użytkownika liczbę całkowitą dodatnią
# n, a następnie wyświetla na ekranie wszystkie potęgi liczby 2 nie większe, niż
# podana liczba. Przykładowo, dla liczby 71 program powinien wyświetlić:
# 1
# 2
# 4
# 8
# 16
# 32
# 64

def print_powers_of_two(n):
    if n < 1:
        return print("Podaj liczbę całkowitą dodatnią.")
    
    power = 1
    while power <= n:
        print(power)
        power *= 2

number = int(input("Podaj liczbę całkowitą dodatnią: "))

print_powers_of_two(number)
