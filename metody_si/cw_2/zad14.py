# Napisać program, w którym pobierane są liczby od użytkownika dopóty,
# dopóki nie poda liczby 0. Następnie wyświetlana jest mediana podanych
# liczb i w kolejnym kroku wszystkie podane liczby w odwrotnej kolejności.

def get_numbers():
    numbers = []
    
    while True:
        num = int(input("Podaj liczbę (0 kończy wprowadzanie): "))
        if num == 0:
            break
        numbers.append(num)
    
    return numbers

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    
    return median

def reverse_numbers(numbers):
    return numbers[::-1]

numbers = get_numbers()
print(f"Mediana podanych liczb: {calculate_median(numbers)}")

print("Podane liczby w odwrotnej kolejności:")
print(reverse_numbers(numbers))

