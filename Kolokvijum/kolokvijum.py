def ucitaj_objave(fajl):
    lista=[]
    with open(fajl, "r", encoding="UTF-8") as f:
        next(f)
        for r in f:
            if not r.strip():   # skip empty lines
                continue
            rijeci = r.strip().split(",")
            profil = {
                "korisnik":rijeci[0],
                "platforma":rijeci[1],
                "lajkovi":int(rijeci[2]),
                "komentari":int(rijeci[3]),
                "tip_sadrzaja":rijeci[4]
            }
           
            lista.append(profil)
    return  lista
rjecnik =ucitaj_objave("drustvene_mreze.csv")
print(rjecnik)

"""def dodaj_objavu(objave):
    lista = []
    try:
        korisnik = input("Unesi ime korisnika: ")
        platforma = input("Unesi platformu: ")
        lajkovi = int(input("Unesi broj lajkova: "))
        komentari = int(input("Unesi broj komentara: "))
        tip_sadrzaja = input("Unesi tip sadrzaja: ")
    except lajkovi and komentari < 0 and not int:
        print("Pogresan unos ")
    except platforma==("instagram","facebook","tiktok","linkedln"):
        print("Nepostojeca plarforma")
    except tip_sadrzaja==("reel","foto","video","reel"):
        print("Pogresan tip sadrzaja")
    rjecnik = {
        "korisnik":korisnik,
        "platforma":platforma,
        "lajkovi":lajkovi,
        "komentari":komentari,
        "tip_sadrzaja":tip_sadrzaja
    }
    lista.append(rjecnik)

    return lista

#def ukupan_angazman(objava):
    


def prosjek_lajkova(objava):
   
    ukupno = 0
    with open(objava,"r") as f:
        for i in f:
            ukupno = sum(i["lajkovi"])
            prosjek = ukupno/len(i["lajkovi"])

        return prosjek
    





    
        """