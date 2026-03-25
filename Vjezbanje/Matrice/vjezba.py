temperature = [
    [12, 15, 14], # Grad A
    [20, 22, 19], # Grad B
    [5, 8, 7]     # Grad C
]
#PROSJEK ZA SVE
def prosjek_temp(lista):
    count = 0
    ukupno = 0
    for i in lista:
        for j in i:
            ukupno+=j
            count+=1
    return round(ukupno/count,2)

#PROSJEK ZA GRAD    
def prosjek_grada(lista , index):
    red = lista[index]
    ukupno = 0
    count = 0
    for r in red:
        ukupno+=r
        count+=1
    return round(ukupno/count,2)

#PRVI ZA SVAKI GRAD
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

#NAJVECI BROJ U MATRICI
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

    


