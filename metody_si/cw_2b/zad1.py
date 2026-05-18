import pandas
import numpy
import random
import math

#LISTY
lista = []
liczba = []
kolo1 = []
kolo2 = []
kolo3 = []
lista_grupa = []
lista_imie = []
nr = []

listab = []
liczbab = []
kolo1b = []
kolo2b = []
kolo3b = []
lista_grupab = []
lista_imieb = []
nrb = []

for i in range(30):
    #lista.append('30')
    liczba.append(random.randint(1,100000))
    kolo1.append(random.randint(2,5))
    kolo2.append(random.randint(2,5))
    kolo3.append(random.randint(2,5))
    lista_grupa.append(random.choice(['I']))
    lista_imie.append(random.choice(['Andrzej', 'Jarek', 'Monika', 'Michal', 'Tomek', 'Cezary', 'Damian']))
    nr.append(i+1)

for i2 in range(30):
    #lista.append(31,60)
    kolo1b.append(random.randint(2,5))
    liczbab.append(random.randint(1,100000))
    kolo2b.append(random.randint(2,5))
    kolo3b.append(random.randint(2,5))
    lista_grupab.append(random.choice(['II']))
    lista_imieb.append(random.choice(['Andrzej', 'Jarek', 'Monika', 'Michał', 'Tomek', 'Cezary']))
    nrb.append(i2+1)

data = pandas.DataFrame({
    'Imie': lista_imie,
    'Nr_albumu': liczba,
    'Kolokwium_I': kolo1,
    'Kolokwium_II': kolo2,
    'Projekt': kolo3,
    'Nr_grupy': lista_grupa,
    'nr': nr,
})
data = data.set_index('nr')
data_g1 = data.head(30)
data_g2 = data.tail(30)

data2 = pandas.DataFrame({
    'Imie': lista_imieb,
    'Nr_albumu': liczbab,
    'Kolokwium_I': kolo1b,
    'Kolokwium_II': kolo2b,
    'Projekt': kolo3b,
    'Nr_grupy': lista_grupab,
    'nr': nrb,
})
data2 = data2.set_index('nr')
#data_g1 = data.head(30)
#data_g2 = data.tail(30)

print('ZESTAWIENIE WYNIKÓW')
print('\n')
#------------------------------------------------------------------#
print('1. Liczba osob, które otrzymały najwyższą ocenę z kolokwium I, kolokium II i projektu włącznie')
df = pandas.DataFrame(data)
dfa2 = pandas.DataFrame(data2)
print(df.query('Projekt== 5 and Kolokwium_I==5 and Kolokwium_II==5'))
print(dfa2.query('Projekt== 5 and Kolokwium_I==5 and Kolokwium_II==5'))
# kod działa nie może być spacji przy kolumnach
print(len(df.query('Projekt== 5 and Kolokwium_I==5 and Kolokwium_II==5')))
print(len(dfa2.query('Projekt== 5 and Kolokwium_I==5 and Kolokwium_II==5')))
print('\n')
#------------------------------------------------------------------#
print('2. Osoby, ktore nie zaliczyły kolokium II')
df = pandas.DataFrame(data)
dfa2 = pandas.DataFrame(data2)
print(df.query('Kolokwium_II==2'))
print(dfa2.query('Kolokwium_II==2'))
print('\n')
#------------------------------------------------------------------#
srednia_g1_a = pandas.Series.mean(data['Kolokwium_II'])
srednia_g1_b = pandas.Series.mean(data['Kolokwium_I'])
srednia_g1_c = pandas.Series.mean(data['Projekt'])
srednia_g1 = ((srednia_g1_a + srednia_g1_b + srednia_g1_c)/3)
print('3a. Srednia dla ocen z grupy 1 dla kolokwium I:', srednia_g1_b )
print('Średnia z wszystkich ocen dla grupy I:', srednia_g1 )

srednia_g2_d = pandas.Series.mean(data2['Kolokwium_I'])
srednia_g2_e = pandas.Series.mean(data2['Projekt'])
srednia_g2_f = pandas.Series.mean(data2['Kolokwium_II'])
srednia_g2 = ((srednia_g2_d + srednia_g2_e + srednia_g2_f)/3)

print('3b. Srednia dla ocen z grupy 2 dla kolokwium I:', srednia_g2_d )
print('Średnia z wszystkich ocen dla grupy II:', srednia_g2 )
print('\n')

mediana_grupy2 = pandas.Series.median(data2['Kolokwium_I'])
mediana_grupy3 = pandas.Series.median(data2['Kolokwium_II']) #ukazuje mi mediane dla drugiej grupy znacznie szybciej!
mediana_grupy4 = pandas.Series.median(data2['Projekt'])

print('5.Mediana ocen dla grupy 2:', mediana_grupy2, mediana_grupy3, mediana_grupy4)
