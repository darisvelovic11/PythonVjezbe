class Vozilo():
    def __init__(self, registracija, marka, model, godina, predjeno_km, dostupno):
        self.registracija = registracija
        self.marka = marka
        self.model = model
        self.godina = godina
        self.predjeno_km = predjeno_km
        self.dostupno = dostupno

    def iznajmi(self):
        if self.dostupno:
            self.dostupno = False
            print(f"Vozilo {self.model} {self.marka} je sada iznajmljeno.")
        else:
            print(f"Vozilo {self.model} {self.marka} nije dostupno za iznajmljivanje.")

    def vrati(self, km):
        self.predjeno_km+=km
        self.dostupno = True
        print(f"Vozilo {self.model} {self.marka} je vraćeno. Ukupno predjeno km: {self.predjeno_km}.")
    
    def status(self):
        if self.dostupno:
            print(f"Vozilo {self.model} {self.marka} je dostupno za iznajmljivanje.")
        else:
            print(f"Vozilo {self.model} {self.marka} nije dostupno za iznajmljivanje.")
    
    def __str__(self):
        return f"Vozilo: {self.marka} {self.model}, Registracija: {self.registracija}, Godina: {self.godina}, Predjeno km: {self.predjeno_km}, Dostupno: {'Da' if self.dostupno else 'Ne'}"
    
class ElektricniAutomobil(Vozilo):
    def __init__(self, registracija, marka, model, godina, predjeno_km,kapacitet_baterije, napunjenost_baterije, dostupno):
        super().__init__(registracija, marka, model, godina, predjeno_km, dostupno)
        self.kapacitet_baterije = kapacitet_baterije
        self.napunjenost_baterije = napunjenost_baterije

    def iznajmi(self):
        if self.napunjenost_baterije >= 20:
            self.dostupno = True
            print("Moguce je iznajmiti auto")
        else:
            self.dostupno = False
            print("Baterija mora biti napunjena barem 20%")

    def napuni_bateriju(self):
        self.napunjenost_baterije = 100
        print("Baterija je FULL napunjena")

    def __str__(self):
        return super().__str__() + f", Kapacitet baterije: {self.kapacitet_baterije}, Napunjenost baterije: {self.napunjenost_baterije}" 

class SportskiAutomobil(Vozilo):
    def __init__(self, registracija, marka, model, godina, predjeno_km,maksimalna_brzina, stanje_guma, dostupno):
        super().__init__(registracija, marka, model, godina, predjeno_km, dostupno)
        self.maksimalna_brzina = maksimalna_brzina
        self.stanje_guma = stanje_guma

    def iznajmi(self):
        if self.stanje_guma == "Lose":
            self.dostupno = False
            print("Nemoguce je iznajmiti auto , stanje guma je  lose")
        else:
            self.dostupno=True
            print("Gume su dobre. Mozemo iznajmiti auto")
    
    def zamijeni_gume(self):
        self.stanje_guma="Novo"
        print("Gume su nove!")

    def izvedi_drift(self):
        if self.stanje_guma == "Novo":
            self.stanje_guma="Dobro"
            print("Stanje guma je Dobro")
        elif self.stanje_guma == "DObro":
            self.stanje_guma="Lose"
            print("Stanje guma je Lose")
        elif self.stanje_guma == "Lose":
             print("Stanje guma je Lose, ne moze se izvesti drift")
    
    def __str__(self):
        return super().__str__() + f", Maksimalna brzina: {self.maksimalna_brzina}, Stanje guma: {self.stanje_guma}"
    
if __name__=="__main__":
    tesla = ElektricniAutomobil("PGCK123","Tesla","CyberTruck",2020,1000,70,100,True)
    ferari = SportskiAutomobil("BRCS903","Ferrari","Spyder",2026,500,330,"Novo",True)

    print(tesla)
    tesla.iznajmi()
    tesla.vrati(100)
    tesla.napuni_bateriju()

    print("\n")

    print(ferari)
    ferari.zamijeni_gume()
    ferari.izvedi_drift()
    ferari.izvedi_drift()

        