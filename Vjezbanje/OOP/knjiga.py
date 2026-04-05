class Knjiga():
    def __init__(self):
        self.__naziv =""
        self.__autor = ""
        self.__godina_izdavanja = 200
        self.__broj_stranica = 200
        self.__trenutna_stranica = 1

    def get_naziv(self):
        return self.__naziv
    def set_naziv(self,naziv):
        self.__naziv = naziv
    def get_autor(self):
        return self.__autor
    def set_autor(self, autor):
         self.__autor= autor
    def get_godina_izdavanja(self):
        return self.__godina_izdavanja
    def set_godina_izdavanja(self, godina):
        if 0<godina<2026:
            self.__godina_izdavanja = godina
        else:
            print("Pogresna godina")
    def get_broj_stranica(self):
        return self.__broj_stranica
    def set_broj_stranica(self, broj):
        if broj>0:
            self.__broj_stranica = broj
        else:
            print("Pogresan broj")
    def get_trenutna_stranica(self):
        return self.__trenutna_stranica
    def set_trenutna_stranica(self, stranica):
        if stranica>0:
            self.__trenutna_stranica = stranica
        else:
            print("Ne postoji stranica 0")

    def idi_na_stranicu(self, broj):
        if broj <= self.__broj_stranica and broj>0:
            self.__trenutna_stranica=broj
    
    def sledeca_stranica(self):
        if self.__trenutna_stranica<self.__broj_stranica:
            self.__trenutna_stranica +=1
    
    def prethodna_stranica(self):
        if self.__trenutna_stranica>1:
            self.__trenutna_stranica -=1
    
if __name__ == "__main__":
    k1 = Knjiga()

    # Postavljanje osnovnih podataka
    k1.set_naziv("Zločin i kazna")
    k1.set_autor("Dostojevski")
    k1.set_godina_izdavanja(1866)
    k1.set_broj_stranica(500)

    # Provjera gettera
    print("Naziv:", k1.get_naziv())
    print("Autor:", k1.get_autor())
    print("Godina:", k1.get_godina_izdavanja())
    print("Broj stranica:", k1.get_broj_stranica())
    print("Trenutna stranica:", k1.get_trenutna_stranica())

    # Testiranje idi_na_stranicu
    k1.idi_na_stranicu(100)
    print("Nakon idi_na_stranicu(100):", k1.get_trenutna_stranica())  # očekivano: 100

    # Testiranje sledeca_stranica
    k1.sledeca_stranica()
    print("Nakon sledeca_stranica:", k1.get_trenutna_stranica())  # očekivano: 101

    # Testiranje prethodna_stranica
    k1.prethodna_stranica()
    print("Nakon prethodna_stranica:", k1.get_trenutna_stranica())  # očekivano: 100

    # Testiranje graničnih slučajeva (edge cases)
    k1.set_godina_izdavanja(3000)   # očekivano: "Pogresna godina"
    k1.set_broj_stranica(-5)        # očekivano: "Pogresan broj"
    k1.idi_na_stranicu(0)           # ne smije proći
    k1.idi_na_stranicu(9999)        # ne smije proći, van opsega


    


        



        