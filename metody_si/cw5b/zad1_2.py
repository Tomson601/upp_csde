import re

opisy_nawozow = [
	"oprysk A: 2.5 l/ha",
	"oprysk B = 1 l / ha",
	"oprysk C - 0.75L/HA",
	"oprysk D: 3  l/ha",
]

# Wzorzec usuwa jednostke 'l/ha' (takze wielkie litery) z roznymi odstepami.
wzorzec = r"\s*l\s*/\s*ha\b"

oczyszczone_opisy = [re.sub(wzorzec, "", opis, flags=re.IGNORECASE) for opis in opisy_nawozow]

print("Przed:", opisy_nawozow)
print("Po:", oczyszczone_opisy)
