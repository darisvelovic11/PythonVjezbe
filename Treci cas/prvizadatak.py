pravouugaonici = [(15,2),(11,8),(9,17)]

def najveca_povrsina(lista_pravougonika):
    najveci = lista_pravougonika[0]
    max_povrsina = najveci[0]* najveci[1]
    for pravougaonik in pravouugaonici:
        povrsina =pravougaonik[0] * pravougaonik[1]
        if povrsina > max_povrsina:
            max_povrsina = povrsina
            najveci = pravougaonik

    return najveci,max_povrsina

#print(najveca_povrsina(pravouugaonici))
pravougaonik1,povrsina1 = najveca_povrsina(pravouugaonici)
print(f"Pravougaonik sa dimenzijama{pravougaonik1} ima najvece dimenzije: {povrsina1}")


# for a, b in pravouugaonici:
#     povrsina = a*b
#     if povrsina>max_povrsina:
#         max_povrsina=povrsina
#         max_dimenzije=(a,b)
# print(max_dimenzije)
