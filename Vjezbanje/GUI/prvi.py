import customtkinter as ctk

#UVECAJ BROJAC NA KLIK
"""def uvecaj_brojac():
    trenutna_vrijednost = int(labela_broja.cget("text"))
    nova_vrijednost = trenutna_vrijednost + 1
    labela_broja.configure(text=str(nova_vrijednost))

app = ctk.CTk()
app.title("Moj Prvi GUI")
app.geometry("300x200")

naslov = ctk.CTkLabel(app, text="Brojač klikova", font=("Arial",20))
naslov.pack(pady=10)

labela_broja = ctk.CTkLabel(app, text="0", font=("Arial", 30, "bold"))
labela_broja.pack(pady=10)

dugme = ctk.CTkButton(app,text="Klikni me!", command=uvecaj_brojac)
dugme.pack(pady=10)



eur_u_usd=True

def zamjeni_smjer():
    global eur_u_usd
    eur_u_usd = not eur_u_usd

    if eur_u_usd:
        labela_eur.configure(text="Iznos je u EUR:")
        labela_rezultat.configure(text="$0.00")
        dugme_zamjena.configure(text="Prebaci na: USD -> EUR")
    else:
        labela_eur.configure(text="Iznos u USD:")
        labela_rezultat.configure(text="0.00€")
        dugme_zamjena.configure(text="Prebaci na: EUR -> USD")

def konvertuj():
    unos = polje_eur.get()

    try:
        vrijednost = float(unos)
        if eur_u_usd:
            rezultat = vrijednost*1.08
            labela_rezultat.configure(text=f"${rezultat: .2f}", text_color="darkgreen")
        else:
            rezultat = vrijednost / 1.08
            labela_rezultat.configure(text=f"{rezultat: .2f}€", text_color="darkblue")

    except ValueError:
        labela_rezultat.configure(text="Unesi broj!", text_color="red")

app.mainloop()"""


#KONVERTER VALUTA
"""app = ctk.CTk()
app.title("Koverter")
app.geometry("400x300")

app.grid_columnconfigure((0, 1), weight=1)

naslov = ctk.CTkLabel(app, text="Currency Converter", font=("Arial", 20, "bold"))
naslov.grid(row=0, column=0, columnspan=2, pady=20)

dugme_zamjena = ctk.CTkButton(app, text="Prebaci na: USD -> EUR", fg_color="gray", command=zamjeni_smjer)
dugme_zamjena.grid(row=1, column=0, columnspan=2, pady=10)

labela_eur = ctk.CTkLabel(app, text="Iznos u EUR:")
labela_eur.grid(row=2, column=0, padx=10, pady=10, sticky="e")

polje_eur = ctk.CTkEntry(app, placeholder_text="0.00")
polje_eur.grid(row=2, column=1, padx=10, pady=10, sticky="w")

labela_rezultat = ctk.CTkLabel(app, text="$0.00", font=("Arial", 18))
labela_rezultat.grid(row=3, column=0, padx=10, pady=20)

dugme_konvertuj = ctk.CTkButton(app, text = "Convert", command = konvertuj)
dugme_konvertuj.grid(row=3, column=1, padx=10, pady=20)

app.mainloop()"""



#TO DO LISTA
"""class TodoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Moja To-Do Lista")
        self.geometry("400x500")
        self.grid_columnconfigure(0, weight=1)

        # UI Elementi na vrhu
        self.naslov = ctk.CTkLabel(self, text="Danas planiram:", font=("Arial", 20))
        self.naslov.grid(row=0, column=0, pady=20)
        
        self.unos_zadatka = ctk.CTkEntry(self, placeholder_text="Unesi novi zadatak", width=300)
        self.unos_zadatka.grid(row=1, column=0, pady=10)

        self.dugme_dodaj = ctk.CTkButton(self, text="Dodaj zadatak", command=self.dodaj_na_listu)
        self.dugme_dodaj.grid(row=2, column=0, pady=10)

        # Glavni kontejner za listu zadataka
        self.lista_zadataka_okvir = ctk.CTkFrame(self)
        self.lista_zadataka_okvir.grid(row=3, column=0, pady=20, padx=20, sticky="nsew")
        self.lista_zadataka_okvir.grid_columnconfigure(0, weight=1) # Da bi redovi popunili širinu
        
        self.brojac_redova = 0

    def dodaj_na_listu(self):
        tekst = self.unos_zadatka.get()
        
        if tekst != "":
            # 1. Kreiramo poseban mali okvir za JEDAN red (zadatak + dugme)
            # Taj okvir stavljamo UNUTAR self.lista_zadataka_okvir
            red_okvir = ctk.CTkFrame(self.lista_zadataka_okvir, fg_color="transparent")
            red_okvir.grid(row=self.brojac_redova, column=0, sticky="ew", padx=5, pady=2)
            red_okvir.grid_columnconfigure(0, weight=1) # Labela će se širiti, dugme neće

            # 2. Labela sa tekstom zadatka (ide u red_okvir)
            nova_labela = ctk.CTkLabel(red_okvir, text=f"• {tekst}")
            nova_labela.grid(row=0, column=0, sticky="w", padx=10)
            
            # 3. Dugme za brisanje (ide u red_okvir)
            # Komanda destroy se poziva nad 'red_okvir' - to briše i njega i sve unutar njega
            obrisi_dugme = ctk.CTkButton(red_okvir, text="Obriši", width=60, 
                                         fg_color="#ff4444", hover_color="#cc0000",
                                         command=red_okvir.destroy)
            obrisi_dugme.grid(row=0, column=1, padx=5)

            # Pomjeramo brojač za sljedeći red i čistimo unos
            self.brojac_redova += 1
            self.unos_zadatka.delete(0, "end")

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()

"""
class Planner(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Weeding Planner")
        self.geometry("600x400")
        self.grid_columnconfigure(1, weight=1)

        self.naslov = ctk.CTkLabel(self, text="Weeding calcualtor", font=("Arial", 20))
        self.naslov.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.unos_label = ctk.CTkLabel(self, text="Unesi naziv dekoracije", width=300)
        self.unos_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.unos_naziv = ctk.CTkEntry(self, placeholder_text="npr. Cvjetni luk", width=300)
        self.unos_naziv.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.cijena_label = ctk.CTkLabel(self, text="Cijena (€):")
        self.cijena_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        
        self.unos_cijena = ctk.CTkEntry(self, placeholder_text="npr. 150", width=250)
        self.unos_cijena.grid(row=2, column=1, padx=10, pady=10, sticky="w")

if __name__ == "__main__":
    app = Planner()
    app.mainloop()


