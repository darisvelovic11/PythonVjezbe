lista = [[1,0,1,3],
           [0,2,0,-1],
           [2,5,4,-1]]


def sum_diagonal(matrica):
    suma = 0
    for i in range(len(matrica)):
        suma+=matrica[i][i]
        
        
    return suma


print(sum_diagonal(lista))

    
