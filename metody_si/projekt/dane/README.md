# Opis kolumn danych meteorologicznych

Poniżej znajduje się opis pól (kolumn) występujących w zbiorze danych stacji meteorologicznych.

| Kolumna | Opis |
|---|---|
| NSP | Kod stacji |
| POST | Nazwa stacji |
| ROK | Rok |
| MC | Miesiąc |
| DZ | Dzień |
| TMAX | Maksymalna dobowa temperatura powietrza [°C] |
| WTMAX | Status pomiaru TMAX |
| TMIN | Minimalna dobowa temperatura powietrza [°C] |
| WTMIN | Status pomiaru TMIN |
| STD | Średnia dobowa temperatura powietrza [°C] |
| WSTD | Status pomiaru STD |
| TMNG | Minimalna dobowa temperatura powietrza przy gruncie [°C] |
| WTMNG | Status pomiaru TMNG |
| SMDB | Suma dobowa opadów [mm] |
| WSMDB | Status pomiaru SMDB |
| ROOP | Rodzaj opadu (np. S - śnieg, W - deszcz) |
| PKSN | Wysokość pokrywy śnieżnej [cm] |
| WPKSN | Status pomiaru PKSN |

## Uwagi dotyczące statusów

- Status `8` — brak pomiaru
- Status `9` — brak zjawiska

## Przykład danych

| NSP | POST | ROK | MC | DZ | TMAX | WTMAX | TMIN | WTMIN | STD | WSTD | TMNG | WTMNG | SMDB | WSMDB | ROOP | PKSN | WPKSN |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 249180010 | PSZCZYNA | 2001 | 1 | 1 | -1.3 | NaN | -9.6 | NaN | -5.7 | NaN | -11.0 | NaN | 0.0 | 9.0 | NaN | 13.0 | NaN |
| 249180010 | PSZCZYNA | 2001 | 1 | 2 | 3.3 | NaN | -12.0 | NaN | -2.7 | NaN | -13.2 | NaN | 0.0 | 9.0 | NaN | 11.0 | NaN |

- W kolumnach `WTMAX`, `WTMIN`, `WSTD`, `WTMNG`, `WPKSN` te pola mogą zawierać kody statusu (np. `8`, `9`) lub być puste("")- `NaN`.
- `SMDB` to suma dobowych opadów w mm; `WSMDB` to status pomiaru opadów (w przykładzie `9` oznacza brak zjawiska).
