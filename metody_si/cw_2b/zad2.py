import pandas
import numpy
import random
import math
#wczytanie danych z katalogu w chmurze
data = pandas.read_csv('cw_2b\EURUSD_15m_BID_wyczyszczony.csv')
print(data)

#Wybieramy atrybuty do normalizacji
atrybuty=['Open', 'Close'] # wybieramy atrybuty do normalizacji, NAZWY KOLUMN
for atrybut in atrybuty:
    max = data[atrybut ].max() # znajdujemy wartosci max i min
    min = data[atrybut].min()
    data[atrybut] = (data[atrybut]- min) / (max - min)
print(data[atrybut])

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data['Open' ].hist() #RYSOWANIE HISTOGRAMU DLA DANYCH

#4. Na wykresie liniowym przedstaw przebieg zmienności atrybutu Close;
plt.plot(data['Close' ])
plt.show()

