# Napisać program służący do konwersji wartości temperatury podanej w
# stopniachCelsjusza na stopnie w skali Fahrenheita (stopnie Fahrenheita =
# 1.8 * stopnieCelsjusza + 32.0).


def celsius_to_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32.0
    return print(fahrenheit)

celsius_to_fahrenheit(0)  # powinno zwrócić 32.0
celsius_to_fahrenheit(100)  # powinno zwrócić 212.0

