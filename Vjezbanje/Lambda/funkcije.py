#MAP
brojevi = [1, 2, 3, 4]
kvadrati = list(map(lambda x: x**2, brojevi)) # [1, 4, 9, 16]

str_brojevi = ["1", "5", "10"]
ints = list(map(int, str_brojevi)) # [1, 5, 10]

cijene = [100, 200, 300]
nove_cijene = list(map(lambda x: x * 1.1, cijene)) # [110.0, 220.0, 330.0]

korisnici = [{'ime': 'Ana'}, {'ime': 'Marko'}]
imena = list(map(lambda x: x['ime'], korisnici)) # ['Ana', 'Marko']

#FILTER
brojevi = [1, 2, 3, 4, 5, 6]
parni = list(filter(lambda x: x % 2 == 0, brojevi)) # [2, 4, 6]

rijeci = ["Python", "kod", "programiranje", "AI"]
duge = list(filter(lambda x: len(x) > 5, rijeci)) # ['Python', 'programiranje']

podaci = [0, "test", None, False, "ok", ""]
cisti = list(filter(None, podaci)) # ['test', 'ok'] (zadržava samo "truthy" vrijednosti)

#SORTED
voce = ["jabuka", "banana", "kiwi", "narandža"]
sortirano = sorted(voce, key=len) # ['kiwi', 'jabuka', 'banana', 'narandža']

studenti = [
    {'ime': 'Ana', 'ocjena': 9},
    {'ime': 'Bojan', 'ocjena': 7},
    {'ime': 'Ceca', 'ocjena': 10}
]
# Sortiranje od najveće ka najmanjoj ocjeni
top_studenti = sorted(studenti, key=lambda x: x['ocjena'], reverse=True)

brojevi = [10, -50, 20, -1]
po_velicini = sorted(brojevi, key=abs) # [-1, 10, 20, -50]
