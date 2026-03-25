npcs = [
    {
        "ime": "Stari Magičnjak",
        "uloga": "Čuvač Knjižnice",
        "pozicija": {"x": 10, "y": 20},
        "zadaci": ["Čuvati knjige", "Darovati znanje"]
    },
    {
        "ime": "Trgovac Ivan",
        "uloga": "Kupac/Prodavač",
        "pozicija": {"x": 35, "y": 15},
        "zadaci": ["Prodavati predmete", "Kupovati robu"]
    },
    {
        "ime": "Vitez Marko",
        "uloga": "Zaštitnik",
        "pozicija": {"x": 5, "y": 5},
        "zadaci": ["Čuvati grad", "Boriti se sa neprijateljima"]
    }
]

def dodaj_zadatak(ime_npc, novi_zadatak):
    
    for npc in npcs:
        if npc["ime"] == ime_npc:
            npc["zadaci"].append(novi_zadatak)
            print(f"Zadatak '{novi_zadatak}' dodan NPC-u {ime_npc}")
            return True
    print(f" NPC '{ime_npc}' nije pronađen")
    return False

def pronadi_najblizi_npc(x, y):
    if not npcs:
        return None
    
    najblizi = npcs[0]
    najkraca_udaljenost = float('inf')
    
    for npc in npcs:
        udaljenost = ((npc["pozicija"]["x"] - x) ** 2 + 
                      (npc["pozicija"]["y"] - y) ** 2) ** 0.5
        
        if udaljenost < najkraca_udaljenost:
            najkraca_udaljenost = udaljenost
            najblizi = npc
    
    return {
        "npc": najblizi,
        "udaljenost": round(najkraca_udaljenost, 2)
    }

if __name__ == "__main__":
    dodaj_zadatak("Stari Magičnjak", "Učiti čarolije")
    dodaj_zadatak("Trgovac Ivan", "Prihvatiti nove zalihe")
    
    # Pronalaženje najbližeg NPC-a
    rezultat = pronadi_najblizi_npc(8, 12)
    print(f"\nNajbliži NPC: {rezultat['npc']['ime']}")
    print(f"Udaljenost: {rezultat['udaljenost']} jedinica")
    print(f"Uloga: {rezultat['npc']['uloga']}")
    print(f"Zadaci: {', '.join(rezultat['npc']['zadaci'])}")