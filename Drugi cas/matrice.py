matrica = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma = 0

# Prolazimo kroz svaki red
for red in matrica:
    # Prolazimo kroz svaki broj u tom redu
    for broj in red:
        suma = suma + broj  # Dodajemo broj na ukupnu sumu

print(f"Zbroj svih brojeva u matrici je: {suma}")