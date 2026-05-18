# Napisać program, który:
# • utworzy listę 10 liczb całkowitych i wypełni ja wartościami losowymi z przedziału [−10, . . . , 10],
# • wypisze na ekranie zawartość listy,
# • wyznaczy najmniejszy oraz największy element w liście (za pomocą min/max),
# • wyznaczy średnią arytmetyczną elementów listy,
# • wyznaczy ile elementów jest mniejszych, ile większych od średniej,
# • wypisze na ekranie zawartość listy w odwrotnej kolejności, tj. od ostatniego do pierwszego (wypisze, ale nie odwróci listy).
# • Wszystkie wyznaczone wartości powinny zostać wyświetlone na ekranie.
##################################################################################################################################
# Wylosowane liczby:-3 9 2 -10 -3 -4 -1 -5 -10 8, Min: -10, max: 9, Średnia: -1,00,
# Mniejszych od sr.: 6, Większych od sr.: 3, Liczby w odwrotnej kolejności: 8 -10 -5 -1 -4 -3 -10 2 9 -3

import random

random_list = []

for i in range(10):
    random_list.append(random.randint(-10, 10))
    
print("Wylosowane liczby: ", random_list)

min_value = min(random_list)
max_value = max(random_list)
average = sum(random_list) / len(random_list)

higher_than_average = 0
lower_than_average = 0
    
for num in random_list:
    if num > average:
        higher_than_average += 1
    elif num < average:
        lower_than_average += 1

print(f"Min: {min_value}, max: {max_value}, Średnia: {average:.2f},")
print(f"Mniejszych od sr.: {lower_than_average}, Większych od sr.: {higher_than_average},")

reversed_list = random_list[::-1]
print("Liczby w odwrotnej kolejności: ", reversed_list)
