# Napisać program, który oblicza wartość współczynnik BMI (ang. body
# massindex) wg. wzoru: waga/wzrost^2 . Jezeli wynik jest w przedziale (18,5 -
# 24,9) to wypisuje”waga prawidłowa” , jezeli poniżej to ”niedowaga”, jeżeli powyżej ”nadwaga”.

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return print(f"BMI: {bmi:.2f} - niedowaga")
    elif 18.5 <= bmi <= 24.9:
        return print(f"BMI: {bmi:.2f} - waga prawidłowa")
    else:
        return print(f"BMI: {bmi:.2f} - nadwaga")
    
weight = float(input("Podaj swoją wagę w kilogramach: "))
height = float(input("Podaj swój wzrost w metrach: "))
calculate_bmi(weight, height)
