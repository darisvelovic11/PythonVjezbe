class Student():
    def __init__(self):
        self.__ime = ""
        self.__prezime = ""
        self.__broj_indeksa = ""
        self.__lista_polozenih_ispita = []
    
    def get_ime(self):
        return self.__ime
    def get_prezime(self):
        return self.__prezime
    def get_broj_indeksa(self):
        return self.__broj_indeksa
    def get_lista_polozenih_ispita(self):
        return self.__lista_polozenih_ispita
    
    def set_ime(self, ime):
        if ime != "":
            self.__ime = ime
        else:
            print("Unesite ime")
    def set_prezime(self, prezime):
        if prezime != "":
            self.__prezime = prezime
        else:
            print("Unesite prezime")
    def set_broj_indeksa(self, indeks):
        if indeks != "" and "/" in indeks:
            self.__broj_indeksa = indeks
        else:
            print("Pogresan unos indeksa")
    

    def dodaj_ispit(self, naziv_predmeta):
        if naziv_predmeta not in self.__lista_polozenih_ispita:
            self.__lista_polozenih_ispita.append(naziv_predmeta)
        else:
            print("Predmet je vec u listi")
    
    def ukloni_ispit(self, naziv_predmeta):
        if naziv_predmeta  in self.__lista_polozenih_ispita:
            self.__lista_polozenih_ispita.remove(naziv_predmeta)
        else:
            print("Predmet nije u listi")
    
    def broj_polozenih_ispita(self):
        broj = len(self.__lista_polozenih_ispita)
        return broj
    
if __name__ =="__main__":
    s1 = Student()
    s1.set_ime("Daris")
    s1.set_prezime("Velovic")
    s1.set_broj_indeksa("24/016")
    s1.dodaj_ispit("Programiranje")
    s1.dodaj_ispit("Statistika")
    s1.dodaj_ispit("Analiza i Dizajn")

    print("Naziv:", s1.get_ime())
    print("Autor:", s1.get_prezime())
    print("Godina:", s1.get_broj_indeksa())
    print("Broj stranica:", s1.get_lista_polozenih_ispita())

    s1.dodaj_ispit("Java")
    s1.dodaj_ispit("Programiranje")
    s1.ukloni_ispit("Statistika")
    s1.ukloni_ispit("Python")
    print("Broj stranica:", s1.get_lista_polozenih_ispita())

    






    

    



    
    

    

