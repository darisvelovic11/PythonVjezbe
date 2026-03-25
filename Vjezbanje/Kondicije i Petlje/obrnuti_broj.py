broj = int(input("Unesi broj: "))
obrnuto = 0

while broj>0:
    cifra = broj%10
    obrnuto = obrnuto*10 + cifra
    broj //=10
print(obrnuto)