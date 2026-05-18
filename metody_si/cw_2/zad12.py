# Utwórz mini kalkulator w zakresie liczb całkowitych.

def add(a, b):
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Nie można dzielić przez zero!"
    return a // b

RUN_FLAG = True


while RUN_FLAG:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")

    choice = input("Podaj numer operacji (1-5): ")

    if choice == '5':
        RUN_FLAG = False
        print("Koniec programu.")
        break

    num1 = int(input("Podaj pierwszą liczbę całkowitą: "))
    num2 = int(input("Podaj drugą liczbę całkowitą: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"Wynik dodawania: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Wynik odejmowania: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Wynik mnożenia: {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"Wynik dzielenia: {result}")
    else:
        print("Nieprawidłowy wybór. Proszę wybrać numer od 1 do 5.")
