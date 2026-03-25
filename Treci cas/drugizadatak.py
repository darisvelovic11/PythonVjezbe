inventar = [
    {"ime": "Meda","tezina": 15,"vrijednost": 42},
 
    {"ime": "motika","tezina": 11,"vrijednost": 412},
    
    {"ime": "kais","tezina": 13,"vrijednost": 23},
      
    ]
def izracunaj_inventar(lista_predmeta):
    ukupna_tezina = 0
    najvrijedniji = lista_predmeta[0] 
    max_vrijednost = najvrijedniji["vrijednost"]

    for predmet in lista_predmeta:
        ukupna_tezina+=predmet["tezina"]

        if predmet["vrijednost"]> max_vrijednost:
            max_vrijednost = predmet["vrijednost"]
            najvrijedniji = predmet
    return ukupna_tezina , najvrijedniji  

print(izracunaj_inventar(inventar) )    

