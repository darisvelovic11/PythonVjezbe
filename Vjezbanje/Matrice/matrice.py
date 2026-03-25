# Ovo je matrica 3x3 (3 reda, 3 kolone)
matrica = [
    [1, 2, 3],  # Red 0
    [4, 5, 6],  # Red 1
    [7, 8, 9]   # Red 2
]
for red in matrica:
    for kolona in red:
        print(kolona,end="t")
    print()


print(matrica[0][0],matrica[1][1],matrica[2][2])

m = [[1, -2, 3], [4, 5, -6], [-7, 8, 9]]
count = 0
for a in m:
    for b in a:
        if b<0:
            count+=1
print(count)

matrica = [
    [1, 2, 3],  # Red 0
    [4, 5, 6],  # Red 1
    [7, 8, 9]   # Red 2
]
lista=[]
for a in matrica:
    for b in a:
        b*=1.2
        lista.append(round(b,2))
print(lista)

tabla = [
    [0, 0, 0], 
    [0, 1, 0], 
    [0, 0, 0]
]

# Prolazimo kroz indekse redova (0, 1, 2)
for i in range(len(tabla)):
    # Prolazimo kroz indekse kolona u tom redu (0, 1, 2)
    for j in range(len(tabla[i])):
        # Provjeravamo da li je na toj poziciji naša figura (broj 1)
        if tabla[i][j] == 1:
            print(f"Figura je pronađena!")
            print(f"Red: {i}")
            print(f"Kolona: {j}")
            print(f"Koordinate su: ({i}, {j})")

#Prosjek temperature
def izracunaj_prosjek_temperatura(matrica):
    ukupna_suma = 0
    broj_mjerenja = 0
    
    for red in matrica:
        ukupna_suma += sum(red) # sum() je brza ugrađena funkcija za zbir liste
        broj_mjerenja += len(red) # len() nam daje broj elemenata u redu
        
    if broj_mjerenja == 0: # Uvijek mislite na "edge case" - šta ako je matrica prazna?
        return 0
        
    return round(ukupna_suma / broj_mjerenja, 2)

#Prosje svakog prvog dana
temperature = [
    [12, 15, 14], # Grad A
    [20, 22, 19], # Grad B
    [5, 8, 7]     # Grad C
]

def prosjek_prvog_dana(matrica):
    suma_prvog_dana = 0
    broj_gradova = len(matrica)
    
    # Prolazimo kroz svaki red (grad)
    for red in matrica:
        # Uzimamo samo element na poziciji 0 (prvi dan)
        suma_prvog_dana += red[0]
        
    prosjek = suma_prvog_dana / broj_gradova
    return round(prosjek, 2)

print(f"Prosjek za prvi dan (ponedjeljak) je: {prosjek_prvog_dana(temperature)}")

""" profi trik: # Izvlačimo sve nulte elemente u jednu novu listu
prvi_dan = [red[0] for red in temperature]
prosjek = sum(prvi_dan) / len(prvi_dan)"""

temperature = [
    [12, 15, 14], # Grad A
    [20, 22, 19], # Grad B
    [5, 8, 7]     # Grad C
]

def prosjek_kolone(matrica, indeks_kolone):
    suma_kolone = 0
    broj_redova = len(matrica)
    
    # Prolazimo kroz svaki red (grad)
    for red in matrica:
        # Uzimamo element iz specifične kolone (npr. drugi dan, indeks 1)
        suma_kolone += red[indeks_kolone]
        
    prosjek = suma_kolone / broj_redova
    return round(prosjek, 2)

# Testiramo za drugi dan (srijeda, indeks 1)
# To su vrijednosti: 15, 22, 8
srijeda_prosjek = prosjek_kolone(temperature, 1)
print(f"Prosječna temperatura za drugi dan je: {srijeda_prosjek}")

#Najveci
banka = [
    [100, 150, 200], # Klijent 1
    [50, 50, 50],    # Klijent 2
    [300, 200, 100]  # Klijent 3
]

def najveca_usteda(matrica):
    # Pretpostavimo da je prvi broj u matrici najveći
    # To nam je "startna pozicija" za poređenje
    max_iznos = matrica[0][0]
    
    # Prolazimo kroz svaki red (klijenta)
    for red in matrica:
        # Prolazimo kroz svaki iznos (mjesec) u tom redu
        for iznos in red:
            # Ako nađemo iznos koji je VEĆI od našeg trenutnog rekordera...
            if iznos > max_iznos:
                # ...taj iznos postaje novi rekorder!
                max_iznos = iznos
                
    return max_iznos

# Pozivamo funkciju i ispisujemo rezultat
rezultat = najveca_usteda(banka)
print(f"Najveća ušteda u cijeloj banci je: {rezultat} EUR")

#Skraceno profi:
maksimalni_po_redovima = [max(red) for red in matrica]
apsolutni_maksimum = max(maksimalni_po_redovima)
