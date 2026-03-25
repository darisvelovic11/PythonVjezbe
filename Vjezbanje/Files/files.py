#f = open("names.txt")

#sadrzaj = f.read() - cita cijeli fajl
#sadrzaj = f.read(5) - cita prvih pet slova fajla

# print(f.readline()) -> stampa prvi red fajla
# print(f.readline()) - stampa prva dva

"""for line in f:
    print(line)
f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("Ne postoji taj fajl!")
finally:
    f.close()"""
    
#Append - kreira fajl ako ne postoji ili dodaje stvari u postojeci fajl

# f = open("names.txt", "a")
# f.write("Tomi")
# f.close()

# f = open("names.txt")
# print(f.read())
# f.close()

#Write(Overwite)
"""f = open("context.txt","w")
f.write("I deleted all the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()"""



#1
import json

#KLASICAN UNOS I CITANJE

"""vozila = ["BMW M4", "Audi A3", "VW Eos"]



with open("auta.txt","w")as f:

    for auto in vozila:

        f.write(auto + "\n")

with open("auta.txt","r")as f:

    sadrzaj = f.read()

    print(sadrzaj)"""



podaci = {

    "firma": "EOS Rent a Car",

    "vozni_park": [

        {"model": "BMW M4", "cijena": 150},

        {"model": "Audi A3", "cijena": 70}

    ]

}

"""def json_fajl(fajl):

    with open(fajl,"w")as f:

        json.dump(podaci,f,indent=4)



    with open(fajl,"r")as f:

        ucitani_podaci = json.load(f)

        print(ucitani_podaci["vozni_park"][0]["model"])

json_fajl("podaci.json")"""



def dodaj_automobil(ime_fajla):

    try:

        with open(ime_fajla,"r") as f:

            podaci = json.load(f)

    except(FileNotFoundError,json.JSONDecodeError):

        podaci = {"firma": " EOS RENT a Car", "vozni_park" : []}

    model = input("Unesi ime modela:")

    cijena = int(input("Unesi cijenu auta: "))



    novi_auto = {"model": model,"cijena": cijena}



    podaci["vozni_park"].append(novi_auto)



    with open(ime_fajla,"w")as f:

        json.dump(podaci,f,indent=4)

    print(f"Uspjesno dodat {model} u bazu!")



dodaj_automobil("podaci.json")











#UNOS IMENA

"""def unos_imena(ime_fajla):

    ime = input("Unesi ime: ")

    try:

        with open(ime_fajla,"a") as f:

            f.write(ime + "\n")

    

    except Exception:

        print("Nesto nije u redu")



unos_imena("korisnici.txt")

"""

    

#ISPIS KORISNIKA

"""def ispis_korisnika(ime_fajla):

    try:

        with open(ime_fajla, "r") as f:

            print("--- Spisak validnih korisnika ---")

            for linija in f:

                # 1. Čistimo liniju od razmaka i prelaska u novi red (\n)

                ime = linija.strip()

                

                # 2. Proveravamo dužinu imena

                if len(ime) > 3:

                    print(f"Korisnik: {ime}")

                else:

                    print(f"Preskočen prekratak unos: '{ime}'")

                    

    except FileNotFoundError:

        print("Greška: Fajl sa korisnicima još uvek ne postoji.")

    except Exception as e:

        print(f"Desila se neočekivana greška: {e}")



# Pozivamo funkciju da testiramo

ispis_korisnika("korisnici.txt")"""



#2.
"""from functools import reduce

l = [2,3,4,5,6]

print(list(map(lambda x: x*2,l)))

#print(list(filter(lambda x:x%2==0,l)))

print(reduce(lambda acc,item:acc+item,l,0))"""



"""try:

   lista = [10,20,30]

   indeks = int(input("Unesite index za listu:"))

   print(lista[indeks])

except IndexError:

   print("Unijeli ste indeks van liste")

except ValueError:

   print("Nijetse unijeli cijeli broj")"""



"""def provjeri_godine(godine):

    if godine<18:

        raise ValueError("Morate imati bar 18 godina")

try:

    godine = int(input("Unesi broj godina: "))

    print(provjeri_godine(godine))



except Exception as e:

    print(e)"""



"""lista = [i**2 for i in range(1,101)]

print(lista)"""



lista_filmova = ["The Godfather", "Pulp Fiction", "The Beautiful Woman"]

"""nova_lista = []

for film in lista_filmova:

    if film.lower().startswith("t"):

        nova_lista.append(film)

print(nova_lista)"""



#NOVA LISTA FILMOVA

nova_lista_filmova = [film for film in lista_filmova if film.lower().startswith("t")] 

print(nova_lista_filmova) #PROVJERI KOJI JE REDOSLJED CITANJA



lista = [10,12,15,21,32]

print(list(filter(lambda x: x%5==0, lista)))





#NOVA LISTA GRADOVA SA NOVOM TEMPERATUROM

"""for element in lista:

    if element%5==0:

        print(element)"""

lista_gradova = [("Podgorica",19),("Bar",27),("Niksic", 14)]

nova_lista_gradova = list(map(lambda x:(x[0], x[1]*1.8 +32), lista_gradova)) #[0] je grad , [1] je temperatura

print(nova_lista_gradova)



l1 = [10,20,30]

l2 = [5,10,20]

c = list(map(lambda a, b: a+b,l1,l2))

print(c)

from functools import reduce

print(reduce(lambda x, y: x + y, c, 0))





#3.
'''f = open("products.txt",mode="w",encoding="utf-8")

f.write("Naxiv,Opis,Godina,Kolicina,Cijena\n")

f.close()'''





with open("products.txt",mode ="w", encoding="utf-8") as f:

    f.write("Naziv,Opis,Godina,Kolicina,Cijena\n")

proizvodi = [{"naziv":"Televizor",

              "opis":"LG TV",

              "godina":2019,

              "kolicina":5,

              "cijena":300},

              {"naziv":"Televizor",

              "opis":"Samsung TV",

              "godina":2017,

              "kolicina":5,

              "cijena":250

              }]

def append_to_file(list_of_products):

    with open("products.txt","a")as f:

        for product in list_of_products:

            f.write(f"{product['naziv']},{product['opis']},{product['godina']},{product['kolicina']},{product['cijena']}\n")

append_to_file(proizvodi)

with open("products.txt", mode = "r") as f:

    print(f.read())



def get_latest_products(year):

    latest_products=[]

    with open("products.txt", "r") as f:

        next(f)

        for line in f:

            row = [x.strip() for x in line.split(",")]

            if int(row[2])>= year:

                latest_products.append(row)

    return latest_products

#print(get_latest_products(2018))



def max_possible_revenue():

    ukupno = 0



    with open("products.txt","r") as f:

        next(f)

        for line in f:

            row = [x for x in line.split(",")]

            ukupno+=float(row[4])*int(row[3])

        return ukupno

print(max_possible_revenue())



