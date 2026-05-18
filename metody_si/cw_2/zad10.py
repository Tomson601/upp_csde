# Napisać program, który sprawdza, czy podana liczba całkowita n, n > 1, jest liczbą pierwszą.

def is_prime(n):
    if n <= 1:
        return print("Podaj liczbę całkowitą większą niż 1.")
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return print(f"{n} nie jest liczbą pierwszą.")
    
    return print(f"{n} jest liczbą pierwszą.")

number = int(input("Podaj liczbę całkowitą większą niż 1: "))
is_prime(number)
