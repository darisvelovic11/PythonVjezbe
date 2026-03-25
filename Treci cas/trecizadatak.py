zadaci = [
    {"naziv": "matematika","status": "zapoceto","nagrada": 10},
 
    {"naziv": "maternji","zavrseno": "do pola","nagrada": 20},
    
    {"naziv": "englesko","status":"nije zapoceto","nagrada": 30},
      
    ]
def mjenjanje_statusa(lista_zadataka,naziv_zadatka):
    for l in lista_zadataka():
        if l["naziv"]=="naziv_zadatka":
            l["status"]="zavrseno"
            return True
            return False
def ukupna_nagrada(lista):
    ukupna_nagrada=0
    for zadatak in lista:
        if zadatak["status"]=="zavrseno":
            ukupna_nagrada+=zadatak["nagrada"]
    return ukupna_nagrada

mjenjanje_statusa(zadaci,"matematika")

print(ukupna_nagrada(zadaci))
    

    
    
    
    
    
 
