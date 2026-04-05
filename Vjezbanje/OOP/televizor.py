class Televizor:
    def __init__(self):
        self.__broj_kanala = 0
        self.__naziv_kanala = ""
        self.__kanali = []
        self.__jacina_tona = 0


    def get_broj_kanala(self):
        return self.__broj_kanala

    def get_naziv_kanala(self):
        return self.__naziv_kanala

    def get_kanali(self):
        return self.__kanali

    def get_jacina_tona(self):
        return self.__jacina_tona



    def set_broj_kanala(self, broj):
        if 0 <= broj <= len(self.__kanali):
            self.__broj_kanala = broj
            if broj == 0:
                self.__naziv_kanala = ""
            else:
                self.__naziv_kanala = self.__kanali[broj - 1]
        else:
            print(f"Greška: broj kanala mora biti između 0 i {len(self.__kanali)}.")

    def set_naziv_kanala(self, naziv):
        self.__naziv_kanala = naziv

    def set_jacina_tona(self, jacina):
        if 0 <= jacina <= 10:
            self.__jacina_tona = jacina
        else:
            print("Greška: jačina tona mora biti između 0 i 10.")


    def dodaj_kanal(self, naziv):
        self.__kanali.append(naziv)

    def obrisi_kanal(self, naziv):
        if naziv in self.__kanali:
            self.__kanali.remove(naziv)
        else:
            print(f"Greška: kanal '{naziv}' ne postoji u listi.")

    def pojacaj_ton(self):
        if self.__jacina_tona < 10:
            self.__jacina_tona += 1
        else:
            print("Ton je već na maksimalnoj vrijednosti (10).")

    def ime_kanala(self, broj):
        if 1 <= broj <= len(self.__kanali):
            return self.__kanali[broj - 1]
        else:
            print(f"Greška: nema kanala na poziciji {broj}.")
            return None


if __name__ == "__main__":
    tv = Televizor()

    tv.dodaj_kanal("RTS 1")
    tv.dodaj_kanal("RTS 2")
    tv.dodaj_kanal("Pink")
    tv.dodaj_kanal("Prva")

    print("Kanali:", tv.get_kanali())

    tv.set_broj_kanala(2)
    print("Trenutni kanal:", tv.get_naziv_kanala())

    tv.pojacaj_ton()
    tv.pojacaj_ton()
    print("Jacina tona:", tv.get_jacina_tona())

    print("Kanal na poziciji 3:", tv.ime_kanala(3))

    tv.obrisi_kanal("Pink")
    print("Kanali nakon brisanja:", tv.get_kanali())
