def rjecnik_studenata(fajl):
    lista_studenata=[]
    try:    
        with open(fajl, 'r')as f:
            for red in f:
                rijeci = red.strip().split(",")
                ukupno = int(rijeci[2]+rijeci[3]+rijeci[4])
                student = {
                    "ime": rijeci[0].strip(),
                    "indeks": rijeci[1].strip(),
                    "ukupno": ukupno
                }
                lista_studenata.append(student)
    except FileNotFoundError:
        print(f"Fajl {fajl} nije pronađen.")
    return lista_studenata

def odredi_ocjenu(bodovi):
    if bodovi>= 95: return 10
    elif bodovi >= 85: return 9
    elif bodovi >= 75: return 8
    elif bodovi >= 65: return 7
    elif bodovi >= 55: return 6
    else: return 5

def odredi_podatke(lista):
    polozili = list(filter(lambda s: s['ukupno']>=55, lista))
    sortitani = sorted(polozili, key = lambda s: s['ukupno'], reverse= True)
    obradjeni = list(map(lambda s: {**s, "ocjena": odredi_ocjenu(s['ukupno'])}))

    return obradjeni

def generisi_statistiku(lista_svih , lista_polozenih):
    ukupni_bodovi = sum(s['ukupno'] for s in lista_svih)
    prosjek_bodova = ukupni_bodovi/ len(lista_svih)
    prolaznost = (len(lista_polozenih) / len(lista_svih)) * 100

    najbolji = max(lista_svih, key=lambda s: s['ukupno'])['ime']

    distribucija = {6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for s in lista_polozenih:
        ocjena = s['ocjena']
        distribucija[ocjena] = distribucija.get(ocjena, 0) + 1
    