boje = [[0,0,255],[255,0,0]]
def invertuj_boje(slika):
    for i in range(len(slika)):
        for j in range(len(slika[i])):
            slika[i][j] = 255-slika[i][j]
    return slika
print(invertuj_boje(boje))




