class Televizor():
    def __init__(self):
        self.__broj = 0
        self.__naziv = ""
        self.__kanali = []
        self.__jacina_tona = 0

    def get_broj(self):
        return self.__broj
    
    def get_naziv(self):
        return self.__naziv
    
    def get_kanali(self):
        return self.__kanali
    
    def get_jacina_tona(self):
        return self.__jacina_tona
    
    def set_broj(self, broj):
        if 0 <= broj <= len(self.__kanali):
            self.__broj = broj
            if broj==0:
                self.__naziv = ""
            else:
                self.__naziv =self.__kanali[broj-1]
        else:
            print(f"Greška: broj kanala mora biti između 0 i {len(self.__kanali)}.")
    
    def set_naziv(self,naziv):
        self.__naziv = naziv

    def set_jacina_tona(self, jacina):
        if jacina >= 0 and jacina <= 10:
            self.__jacina_tona = jacina
        else:
            print("Greška: jačina tona mora biti između 0 i 10.")


    def dodaj_kanal(self, kanal):
        self.__kanali.append(kanal)
    
    def obrisi_kanal(self, kanal):
        if kanal in self.__kanali:
            self.__kanali.remove(kanal)
        else:
            print("Ne mozete izbrisati kanal koji ne postoji")

    def pojacaj_ton(self):
        if self.__jacina_tona < 10:
            self.__jacina_tona+=1
        else:
            print("Dostignuta je maksimalna jacina zvuka")
    
    def ime_kanala(self, broj_kanala):
        if 1<=broj_kanala<=len(self.__kanali):
            return self.__kanali[ broj_kanala-1]
        else:
            print(f"Greška: nema kanala na poziciji { broj_kanala}.")
            return None

if __name__ == "__main__":
    tv = Televizor()

    tv.dodaj_kanal("RTCG 1")
    tv.dodaj_kanal("RTCG 2")
    tv.dodaj_kanal("Baka Prase")
    tv.dodaj_kanal("Prva")

    print("Kanali:", tv.get_kanali())

    tv.set_broj(2)
    print("Trenutni kanal:", tv.get_naziv())

    tv.pojacaj_ton()
    tv.pojacaj_ton()
    print("Jacina tona:", tv.get_jacina_tona())

    print("Kanal na poziciji 3:", tv.ime_kanala(3))

    tv.obrisi_kanal("Baka Prase")
    print("Kanali nakon brisanja:", tv.get_kanali())





        
        

        

