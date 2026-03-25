brojevi=[1,22,22,33,33,44]
brojevi2 = set(brojevi)
print(brojevi2)

gradovi = ["Nikšić", "Budva", "Nikšić", "Kotor", "Budva"]

# Pretvaramo listu u skup da maknemo duplikate
jedinstveni_gradovi = set(gradovi)

# Ako želimo opet nazad listu, samo je "obučemo" u list()
rezultat = list(jedinstveni_gradovi)

print(f"Jedinstveni gradovi: {rezultat}")