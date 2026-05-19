import re

opisy = [
    "azot 20kg/ha",
    "fosfor: 15 kg/ha",
    "potas = 30 kg / ha",
    "wapń - 10kg / ha"
]

# Wzorzec do usunięcia jednostek 'kg/ha' z ewentualnymi spacjami
pattern = r'\s*kg\s*/\s*ha'

# Zastosowanie re.sub do każdego opisu
oczyszczone = [re.sub(pattern, '', opis) for opis in opisy]

print(oczyszczone)