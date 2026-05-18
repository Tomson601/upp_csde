# NSP — kod stacji.
# POST — nazwa stacji.
# ROK — rok.
# MC — miesiąc.
# DZ — dzień.
# TMAX — maksymalna dobowa temperatura powietrza.
# WTMAX — status pomiaru TMAX.
# TMIN — minimalna dobowa temperatura powietrza.
# WTMIN — status pomiaru TMIN.
# STD — średnia dobowa temperatura powietrza.
# WSTD — status pomiaru STD.
# TMNG — minimalna dobowa temperatura przy gruncie.
# WTMNG — status pomiaru TMNG.
# SMDB — suma dobowa opadów.
# WSMDB — status pomiaru SMDB.
# ROOP — rodzaj opadu.
# PKSN — wysokość pokrywy śnieżnej.
# WPKSN — status pomiaru PKSN.
import pandas as pd


cols = [
    "NSP", "POST", "ROK", "MC", "DZ",
    "TMAX", "WTMAX", "TMIN", "WTMIN",
    "STD", "WSTD", "TMNG", "WTMNG",
    "SMDB", "WSMDB", "ROOP", "PKSN", "WPKSN"
]

df = pd.read_csv(r'cw_2b\k_d_01_2001.csv', sep=',', decimal='.', encoding='cp1250', header=None, names=cols)

print('Liczba brakujących wartości w każdej kolumnie:')
print(df.isna().sum())

# Uzupełnianie TMAX i TMIN interpolacją liniową (w tym na krawędziach)
df['TMAX'] = df['TMAX'].interpolate(method='linear', limit_direction='both')
df['TMIN'] = df['TMIN'].interpolate(method='linear', limit_direction='both')

# Wypełnianie braków: numeryczne kolumny zerami, nienumeryczne kolumny stringiem '0'
num_cols = df.select_dtypes(include=['number']).columns
other_cols = df.columns.difference(num_cols)
if len(num_cols) > 0:
	df[num_cols] = df[num_cols].fillna(0)
if len(other_cols) > 0:
	df[other_cols] = df[other_cols].fillna('0')

print('\nLiczba brakujących wartości po wypełnieniu zerami:')
print(df.isna().sum())

print(df.describe())
