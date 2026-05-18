import pandas

data = pandas.read_csv('cw_2b\\EURUSD_15m_BID_wyczyszczony.csv', nrows=1200)
data = data.drop('Volume', axis=1)

# Liczba pustych wartości w kolumnie Close
empty_count = data['Close'].isna().sum()
print(f"Liczba pustych wartości w kolumnie Close: {empty_count}")

# Naprawa danych - interpolacja liniowa dla wypełnienia brakujących wartości
data['Close'] = data['Close'].interpolate(method='linear')

# Liczba pustych wartości po naprawie
after_fix_empty_count = data['Close'].isna().sum()
print(f"Liczba pustych wartości w kolumnie Close po naprawie: {after_fix_empty_count}")

# Przed wypełnieniem pustych wartości zerami
print("Data przed wypełnieniem pustych wartości zerami:")
print(data.isna().sum())

# Wypełnianie pustych wartości w pozostałych kolumnach zerami
data = data.fillna(0)

print("Data po wypełnieniu pustych wartości zerami:")
print(data.isna().sum())

# Wartości maksymalne i minimalne dla każdego atrybutu
print("\nWartości minimalne i maksymalne dla każdego atrybutu:")
print(data.describe().loc[['min', 'max']])

print("\nWartości średnie dla każdego atrybutu:")
print(data.describe().loc[['mean']])
