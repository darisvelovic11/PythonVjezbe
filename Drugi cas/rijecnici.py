# 1. Inicijalizacija rječnika
rjecnik = {
    "ime": "Marko",
    "index": "17",
    "prezime": "Markovic"
}

# 2. Ispis vrijednosti pomoću ključa
print(f"Index studenta je: {rjecnik['index']}")

# 3. DODAVANJE novog para ključ:vrijednost
# Ispravno: rjecnik["kljuc"] = vrijednost
rjecnik["godina_studija"] = 4
print("Nakon dodavanja godine studija:", rjecnik)

# 4. IZMJENA postojeće vrijednosti
# Ispravno: rjecnik["postojeci_kljuc"] = nova_vrijednost
rjecnik["ime"] = "Nemanja"
print("Nakon promjene imena:", rjecnik)


artikl = {
    "naziv": "Laptop",
    "cijena": 850.50,
    "kolicina": 3
}

# Uzimamo vrijednosti preko ključeva
ukupno = artikl["cijena"] * artikl["kolicina"]

print(f"Artikl: {artikl['naziv']}")
print(f"Ukupna vrijednost na skladištu: {ukupno} EUR")