rijec = (input("Unesi a: "))
samoglasnici = "aeiouAEIOU" 
rezultat=""

for slovo in rijec:
    if slovo in samoglasnici:
        rezultat+=slovo

print("Samoglasnici su: ", rezultat)


