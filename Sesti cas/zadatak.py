def kreiraj_upisi(mat , prog , baze):
    with open(mat,mode="w") as f:
        f.write("ime_prezime,indeks,bodovi_kol1,bodovi_kol2,bodovi_zavrsni\n")
        f.write("Marko Markovic,21-045,20,20,40\n")
        f.write("Nemanja Nikolic,21-035,10,30,40\n")
        f.write("Borislav Zivoinonic,21-015,15,15,40\n")
    with open(prog,mode="w") as f:
        f.write("ime_prezime,indeks,bodovi_kol1,bodovi_kol2,bodovi_zavrsni\n")
        f.write("Marko Markovic,21-045,20,20,40\n")
        f.write("Nemanja Nikolic,21-035,10,30,40\n")
        f.write("Borislav Zivoinonic,21-015,15,15,40\n")
    with open(baze,mode="w") as f:
        f.write("ime_prezime,indeks,bodovi_kol1,bodovi_kol2,bodovi_zavrsni\n")
        f.write("Marko Markovic,21-045,20,20,40\n")
        f.write("Nemanja Nikolic,21-035,10,30,40\n")
        f.write("Borislav Zivoinonic,21-015,15,15,40\n")
    
    return True
kreiraj_upisi("matematika.txt","programiranje.txt","baze.txt")

def rjecnik_studenata(fajl):
    lista_studenata = []
    with open(fajl, "r") as f:
        next(f)
        for red in f:
            rijeci = red.strip().split(",")
            studenti = {
                "ime_prezime" : rijeci[0], # Promijenjeno sa "ime" na "ime_prezime"
                "indeks" : rijeci[1],
                "bodovi_kol1": int(rijeci[2]),
                "bodovi_kol2": int(rijeci[3]),
                "bodovi_zavrsni": int(rijeci[4])        
            }
            studenti["ukupno"] = studenti["bodovi_kol1"] + studenti["bodovi_kol2"] + studenti["bodovi_zavrsni"]            
            lista_studenata.append(studenti)
    return lista_studenata
baze = rjecnik_studenata("baze.txt")
print(baze)

def odredi_ocjenu(bodovi):
    if bodovi>= 95: return 10
    elif bodovi >= 85: return 9
    elif bodovi >= 75: return 8
    elif bodovi >= 65: return 7
    elif bodovi >= 55: return 6
    else: return 5

def obradi_studente(studenti):
    studenti_sa_ocjenom=list(map(
        lambda s:{
            "ime_prezime":s["ime_prezime"],
            "indeks":s["indeks"],
            "bodovi_kol1":s["bodovi_kol1"],
            "bodovi_kol2":s["bodovi_kol2"],
            "bodovi_zavrsni":s["bodovi_zavrsni"],
            "ukupno":s["ukupno"],
            "ocjena":odredi_ocjenu(s["ukupno"])
        },studenti))
    pali = list(filter(lambda s:s["ukupno"]<55,studenti_sa_ocjenom))
    pali_sortirano = sorted(pali,key = lambda s : s["ukupno"], reverse=True )

    return studenti_sa_ocjenom,pali_sortirano
baze_obrada,baze_pali= obradi_studente(baze)

def statistika(studenti):
    ukupno_bodova = 0
    broj_polozenih = 0
    distribucija={6:0,7:0,8:0,9:0,10:0}
    najbolji_student = studenti[0]

    for student in studenti:
        ukupno_bodova+=student["ukupno"]
        if student["ukupno"]>=55:
            broj_polozenih+=1
            if student["ocjena"] in distribucija:
                distribucija[student["ocjena"]]+=1
        if student["ukupno"]>=najbolji_student["ukupno"]:
            najbolji_student = student
    prosjek = ukupno_bodova/len(student)
    prolaznost = (broj_polozenih/len(student))*100
    return{
        "prosjek":prosjek,
        "prolaznost":prolaznost,
        "ime_najbolje":najbolji_student,
        "distribucija":distribucija
    }
baze_statistika = statistika(baze_obrada) 



