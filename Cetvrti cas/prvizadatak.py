matrica = [
    [10, 15, 20], # Klijent 1
    [5, 5, 5],    # Klijent 2
    [3, 2, 10]  # Klijent 3
]

for i in range(len(matrica)) :
    for j in range(len(matrica[i])):
        if matrica[i][j] %2==0:
            matrica[i][j] = matrica[i][j]**2
print(matrica)
