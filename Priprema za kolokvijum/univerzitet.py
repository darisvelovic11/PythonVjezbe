def studenti_rjecnik(fajl):
    lista_studenata=[]
    with open(fajl, "r", encoding="UTF-8") as f:
        next(f)
        for r in f:
            rijeci = r.strip().split(",")
            studenti = {
                "ime":rijeci[0],
                "indeks":rijeci[1],
                "k1":int(rijeci[2]),
                "k2":int(rijeci[3]),
                "z":int(rijeci[4]),
            }
            studenti["ukupno"] = studenti["k1"] + studenti["k2"] + studenti["z"]
            lista_studenata.append(studenti)
    return  lista_studenata
rjecnik =studenti_rjecnik("matematika.txt")


def odredi_ocjenu(bodovi):
    if bodovi>= 95: return 10
    elif bodovi >= 85: return 9
    elif bodovi >= 75: return 8
    elif bodovi >= 65: return 7
    elif bodovi >= 55: return 6
    else: return 5

def obradi_studente(studenti):
    studenti_sa_ocjenom = list(map(lambda s:{
        "ime":s["ime"],
        "indeks":s["indeks"],
        "k1":s["k1"],
        "k2":s["k2"],
        "z":s["z"],
        "ukupno":s["ukupno"],
        "ocjena":odredi_ocjenu(s["ukupno"])
    },studenti))

    pali_studenti = list(filter(lambda s:s["ukupno"]<55, studenti_sa_ocjenom))
    sortirano = sorted(studenti_sa_ocjenom,key=lambda s:s["ukupno"], reverse=True)
    
    return studenti_sa_ocjenom , pali_studenti ,sortirano 

def statistika(studenti):
    ukupno_bodova = 0
    broj_polozenih = 0
    distibucija = {6:0,7:0,8:0,9:0,10:0}
    najbolji = studenti[0]
    
    for s in studenti:
        ukupno_bodova+=s["ukupno"]
        if s["ukupno"]>=55:
            broj_polozenih+=1
            if s["ocjena"] in distibucija:
                distibucija[s["ocjena"]]+=1
        if s["ukupno"] > najbolji["ukupno"]:
            najbolji = s
    prosjek = round(ukupno_bodova/len(studenti),2)
    prolaznost = round((broj_polozenih/len(studenti)*100),2)
    return {
        "prosjek":prosjek,
        "prolaznost":prolaznost,
        "najbolji":najbolji
    }



sirovi_podaci = studenti_rjecnik("matematika.txt")
obradjeni , pali , sortirani = obradi_studente(sirovi_podaci)
baza_statistike =statistika(obradjeni)

def kum_izvjestaj(matematika,programiranje,baze):
    indeksi_mat = set(s["indeks"] for s in matematika)
    indeksi_prog = set(s["indeks"] for s in programiranje)
    indeksi_baze = set(s["indeks"] for s in baze)

    zajednicki_indeksi = indeksi_mat.intersection(indeksi_prog).intersection(indeksi_baze)

    rezultati=[]
    for indeks in zajednicki_indeksi:
        ukupno_bodova = 0
        ime = ""
        for s in matematika:
            if s["indeks"] == indeks:
                ukupno_bodova += s["ukupno"]
                ime = s["ime"] # Uzimamo ime usput
        
        for s in programiranje:
            if s["indeks"] == indeks:
                ukupno_bodova += s["ukupno"]
                
        for s in baze:
            if s["indeks"] == indeks:
                ukupno_bodova += s["ukupno"]
        prosjek = round(ukupno_bodova / 3, 2)
        rezultati.append({"ime": ime, "indeks": indeks, "kumulativni_prosjek": prosjek})
        
    return rezultati
mat_lista = studenti_rjecnik("matematika.txt")
prog_lista = studenti_rjecnik("programiranje.txt")
baze_lista = studenti_rjecnik("baze.txt")

zajednicki = kum_izvjestaj(mat_lista, prog_lista, baze_lista)
print("Studenti na svim predmetima:", zajednicki)








