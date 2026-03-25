def odvoji_parne_neparne(lista):
    parni = []
    neparni = []
    
    for broj in lista:
        if broj % 2 == 0:
            parni.append(broj)
        else:
            neparni.append(broj)
            
    return parni, neparni

moji_brojevi = [1, 2, 3, 4, 5, 6, 7, 8]
p, n = odvoji_parne_neparne(moji_brojevi)

print(f"Parni: {p}")   
print(f"Neparni: {n}") 