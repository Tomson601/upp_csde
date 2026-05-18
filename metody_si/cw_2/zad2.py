# Napisać program służący do konwersji wartości temperatury podanej w
# stopniach Celsjusza na stopnie w skali Kelwina (stopnie Celsjusza + 273.15)


def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return print(kelvin)

celsius_to_kelvin(0)  # powinno zwrócić 273.15
celsius_to_kelvin(100)  # powinno zwrócić 373.15
celsius_to_kelvin(-273.15)  # powinno zwrócić 0.0

