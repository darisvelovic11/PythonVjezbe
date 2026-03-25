data = [5, 12, 7, 18, 3, 25, 10, 6]
nova = []

for x in data:
    if x>10 and x%2==0:
        nova.append(x)

print(nova)

#NAJVECI BROJ I INDEX
najveci = data[0]
index = 0
for i  in range(1,len(data)):
    if data[i]>najveci:
        najveci=data[i]
        index = i
print(f"Najveci broj je {najveci} ,njegov index je: {index}")

#PARNI I NEPARNI
parni = []
neparni = []
for br in data:
    if br%2==0:
        parni.append(br)
    else:
        neparni.append(br)
print("Parni brojevi: ", parni)
print("Neparni brojevi: ", neparni)  
    
#PALINDROM BEZ SLICING primjer: Ana voli Milovana
def is_palindrome(lst):
    lijevo = 0
    desno = len(lst) - 1
    
    while lijevo < desno:
        if lst[lijevo] != lst[desno]:
            return False
        lijevo += 1
        desno -= 1
    
    return True

#NAJVECA RAZLIKA
def max_difference(lst):
    if not lst:
        return 0
    
    maksimum = lst[0]
    minimum = lst[0]
    
    for broj in lst:
        if broj > maksimum:
            maksimum = broj
        if broj < minimum:
            minimum = broj
    
    return maksimum - minimum

