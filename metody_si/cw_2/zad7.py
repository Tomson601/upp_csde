# Napisać program, który wczytuje liczby podawane przez użytkownika
# dotąd, do-póki nie podana zostanie liczba 0. Następnie wyświetlić sumę
# wszystkich poda-nych liczb.


def sum_of_numbers():
    total_sum = 0
    
    while True:
        num = int(input("Podaj liczbę (0 kończy wprowadzanie): "))
        if num == 0:
            break
        total_sum += num
    
    return print(f"Suma wszystkich podanych liczb: {total_sum}")

sum_of_numbers()

