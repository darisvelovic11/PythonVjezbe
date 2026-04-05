class BankovniRacun():
    def __init__(self):
        self.__broj_racuna = ""
        self.__ime_vlasnika = ""
        self.__stanje = 0

    def get_broj_racuna(self):
        return self.__broj_racuna
    def get_ime_vlasnika(self):
        return self.__ime_vlasnika
    def get_stanje(self):
        return self.__stanje
    
    def set_broj_racuna(self, broj):
        if broj != "":
            self.__broj_racuna = broj
        else:
            print("Broj racuna ne smije biti prazan")
    def set_ime_vlasnika(self, ime):
        if ime != "":
            self.__ime_vlasnika = ime
        else:
            print("Ime ne smije biti prazno")
    def set_stanje(self, stanje):
        if stanje>=0:
            self.__stanje=stanje
        else:
            print("Stanje ne moze biti negativno")
    
    def uplati(self, iznos):
        if iznos>0:
            self.__stanje+=iznos
            return self.__stanje
    
    def podigni(self, iznos):
        if iznos>0 and self.__stanje>=iznos:
             self.__stanje-=iznos
             return self.__stanje
           
    
    def prikazi_stanje(self):
        return f"Trenutno stanje je {self.__stanje} $"


if __name__ == "__main__":
        b1 = BankovniRacun()

        b1.set_ime_vlasnika("Daris")
        b1.set_broj_racuna("123ABC")
        b1.set_stanje(1000)

        print(b1.podigni(200))
        print(b1.uplati(500))
        print(b1.prikazi_stanje())
        
        
        