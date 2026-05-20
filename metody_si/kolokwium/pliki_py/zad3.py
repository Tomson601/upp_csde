import pandas as pd

df = pd.read_csv('zadanie_3_brak.csv')

df = df.head(500)

df = df[['Date', 'Open', 'Close', 'Volume']]

df = df.dropna(subset=['Open'])

print(df.head(10))
