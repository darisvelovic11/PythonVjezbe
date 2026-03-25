def kreiraj_fajl(prva,druga,treca):
    with open(prva,"w")as f:
        f.write("prozivod,id_proizvoda,cijena,kolicina,popust\n")
        f.write("Laptop,L101,1000,5,10\n")
        f.write("Mis,M202,20,50,0\n")
    with open(druga,"w")as f:
        f.write("prozivod,id_proizvoda,cijena,kolicina,popust\n")
        f.write("Laptop,L101,1000,5,10\n")
        f.write("Mis,M202,20,50,0\n")
    with open(treca,"w")as f:
        f.write("prozivod,id_proizvoda,cijena,kolicina,popust\n")
        f.write("Laptop,L101,1000,5,10\n")
        f.write("Mis,M202,20,50,0\n")
    return True

kreiraj_fajl("poslovnica_centar.txt","poslovnica_city.txt","poslovnica_delta.txt")

def rjecnik_prodavnica(fajl):
    lista_prodavnica = []
    with open(fajl,"r",encoding="UTF-8") as f:
        next(f)
        for red in f:
        
            rijeci = red.strip().split(",")
            prodavnice = {
                "proizvod":rijeci[0],
                "id_proizvoda":rijeci[1],
                "cijena":int(rijeci[2]),
                "kolicina":int(rijeci[3]),
                "popust":int(rijeci[4])
            }
            prodavnice["zarada"] = prodavnice["cijena"]*prodavnice["kolicina"]*(1-prodavnice["popust"]/100)
            lista_prodavnica.append(prodavnice)
    return lista_prodavnica
print(rjecnik_prodavnica("poslovnica_city.txt"))

def obrada(lista_proizvoda):
    def dodaj_kategoriju(p):
        novi_p = {
            "proizvod": p["proizvod"],
            "id_proizvoda": p["id_proizvoda"],
            "cijena": p["cijena"],
            "kolicina": p["kolicina"],
            "popust": p["popust"],
            "zarada": p["zarada"],
            "kategorija": "Premium" if p["cijena"] > 500 else "Standard"
        }
        return novi_p
    proizvodi_sa_kategorijom = list(map(dodaj_kategoriju, lista_proizvoda))
    proizvodi_sa_popustom = list(filter(lambda p:p["popust"]>0, proizvodi_sa_kategorijom))
    proizvodi_po_zaradi = sorted(proizvodi_sa_kategorijom,key=lambda p:p["zarada"] , reverse=True)

    return proizvodi_sa_kategorijom, proizvodi_po_zaradi
podaci_city = rjecnik_prodavnica("poslovnica_city.txt")
svi, sa_popustom = obrada(podaci_city)

def statistika(lista):
    ukupna_zarada = 0
    broj_prodatih = 0
    naj = lista[0]

    for l in lista:
        ukupna_zarada+=l["zarada"]
        broj_prodatih+=l["kolicina"]
        if l["kolicina"]>=naj["kolicina"]:
            naj = l
        return{
            "ukupno":ukupna_zarada,
            "broj prodatih":broj_prodatih,
            "najbolji":naj
        }
print(statistika(svi))

def pronadji_zajednicke(centar, city, delta):
    set_centar = set(p["id_proizvoda"] for p in centar)
    set_city = set(p["id_proizvoda"] for p in city)
    set_delta = set(p["id_proizvoda"] for p in delta)

    
    zajednicki = set_centar.intersection(set_city).intersection(set_delta)
    konacna_lista = []

    for id_artikla in zajednicki:
        ukupna_kolicina = 0
        naziv_proizvoda = ""

        # Prolazimo kroz sve tri poslovnice
        for poslovnica in [centar, city, delta]:
            for p in poslovnica:
                if p["id_proizvoda"] == id_artikla:
                    ukupna_kolicina += p["kolicina"]
                    naziv_proizvoda = p["proizvod"]
        
        konacna_lista.append({
            "proizvod": naziv_proizvoda,
            "id": id_artikla,
            "ukupna_kolicina": ukupna_kolicina
        })
    return konacna_lista


        