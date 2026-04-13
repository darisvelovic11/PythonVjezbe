import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")
app.grid_columnconfigure(0, weight=1) # Pravimo kolonu koja se širi

# Dugme 1: Samo stoji u sredini (default)
d1 = ctk.CTkButton(app, text="Ja sam u sredini")
d1.grid(row=0, column=0, pady=10)

# Dugme 2: Rastegnuto od ivice do ivice (sticky="ew")
d2 = ctk.CTkButton(app, text="Ja popunjavam sve", fg_color="darkgreen")
d2.grid(row=1, column=0, pady=10, sticky="ew", padx=20) 

# Dugme 3: Zalijepljeno samo lijevo (sticky="w")
d3 = ctk.CTkButton(app, text="Ja sam lijevo", fg_color="darkblue")
d3.grid(row=2, column=0, pady=10, sticky="w", padx=20)

app.mainloop()