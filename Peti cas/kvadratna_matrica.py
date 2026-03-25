def is_square(matrica):
    broj_redova = len(matrica)
    for red in matrica:
        if len(red)!=broj_redova:
            return False
    return True
