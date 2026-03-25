def filtriraj_studente(lista_studenata):
    rezultat = []  
    
    for student in lista_studenata:
        ime = student["ime"]
        prisutan = student["prisutan"]
        odsutan = student["odustan"] 

        ukupan_broj_casova = prisutan + odsutan
        
        procenat = prisutan / ukupan_broj_casova
        
        
        if procenat >= 0.75:
            
            stavka = (ime, round(procenat, 2))
            rezultat.append(stavka)
            
    return rezultat


studenti = [
    {"ime": "Marko Markovic", "prisutan": 10, "odustan": 2},
    {"ime": "Milos Milosevic", "prisutan": 8, "odustan": 4},
    {"ime": "Marija Cetkovic", "prisutan": 6, "odustan": 6},
    {"ime": "Nikola Milivojevic", "prisutan": 2, "odustan": 10},
    {"ime": "Marijana Minic", "prisutan": 11, "odustan": 1}
]


izlaz = filtriraj_studente(studenti)
print(izlaz)