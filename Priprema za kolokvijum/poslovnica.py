def upis_poslovnica(jedan,dva, tri):
    with open(jedan , "w")as f:
        f.write("proizvod,kategorija,prodato_komada,cijena_po_komadu,popust_procenat\n")
        f.write("Laptop,Elektronika,10,500,10\n")
        f.write("Telefon,Elektronika,15,300,5\n")
        f.write("Kompjuter,Elektronika,5,1000,10\n")
    with open(dva , "w")as f:
        f.write("proizvod,kategorija,prodato_komada,cijena_po_komadu,popust_procenat\n")
        f.write("Laptop,Elektronika,10,500,10\n")
        f.write("Telefon,Elektronika,15,300,5\n")
        f.write("Kompjuter,Elektronika,5,1000,10\n")
    with open(tri , "w")as f:
        f.write("proizvod,kategorija,prodato_komada,cijena_po_komadu,popust_procenat\n")
        f.write("Laptop,Elektronika,10,500,10\n")
        f.write("Telefon,Elektronika,15,300,5\n")
        f.write("Kompjuter,Elektronika,5,1000,10\n")

    return True
upis_poslovnica("bar.txt","podgorica.txt","niksic.txt")

def ucitavanje(fajl):
    lista =[]
    with open(fajl,"r")as f:
        next(f)
        for red in f:
            rijeci = red.strip().split(",")
            rjecnik = {
                "proizvod":rijeci[0],
                "kategorija":rijeci[1],
                "prodato":int(rijeci[2]),
                "cijena":int(rijeci[3]),
                "popust":int(rijeci[4])
            }
            rjecnik["zarada"] = rjecnik["prodato"]*rjecnik["cijena"]*(1-rjecnik["popust"]/100)
            lista.append(rjecnik)
    return lista
print(ucitavanje("bar.txt"))

def obrada(fajl):
    def status(p):
        novo = {
            "proizvod": p["proizvod"],
            "kategorija": p["kategorija"],
            "cijena": p["cijena"],
            "prodato": p["prodato"],
            "popust": p["popust"],
            "zarada": p["zarada"],
            "status": "Bestseller" if p["prodato"] > 50 else "Regular"
        }
        return novo
    sa_statusom = list(map(status , fajl))
    filtrirani = list(filter(lambda p: p["zarada"]>=1000 ,sa_statusom ))
    sortirani = sorted(sa_statusom, key=lambda p: p["zarada"], reverse=True)

    return sa_statusom , sortirani

ucitani = ucitavanje("bar.txt")
print(obrada(ucitani))