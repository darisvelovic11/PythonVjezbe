import csv

#ZADATAK 1
"""f = open("pjesme.csv")
sadrzaj = csv.DictReader(f)
pjesme = []

for red in sadrzaj:
    pjesme.append(red)
f.close()

pjesme.sort(key = lambda x:x['Length'], reverse = True)
top10 = pjesme[:10]

f2 = open("Zadatak1.csv", mode="w", newline = "")
pisanje = csv.DictWriter(f2,fieldnames=sadrzaj.fieldnames)
pisanje.writeheader()
for pjesma in top10:
    pisanje.writerow(pjesma)
f.close()"""


#ZADATAK 2
"""f = open("pjesme.csv")
sadrzaj = csv.DictReader(f)
pjesme = []

for red in sadrzaj:
    pjesme.append(red)
f.close()

pjesme.sort(key = lambda x:x['Danceability'], reverse = True)
top10 = pjesme[:10]

f3 = open("Zadatak2.csv", mode="w", newline = "")
pisanje = csv.DictWriter(f3,fieldnames=sadrzaj.fieldnames)
pisanje.writeheader()
for pjesma in top10:
    pisanje.writerow(pjesma)
f.close()"""

#ZADATAK 3
"""f = open("pjesme.csv")
sadrzaj = csv.DictReader(f)
pjesme = []

for red in sadrzaj:
    if len(red["Track.Name"])>0 and red["Track.Name"][0].isupper():
           pjesme.append(red)
f.close()

pjesme.sort(key = lambda x:x['Popularity'], reverse = True)
top10 = pjesme[:10]

top10.sort(key = lambda x:x["Energy"], reverse = True)

f4 = open("Zadatak3.csv", mode="w", newline = "")
pisanje = csv.DictWriter(f4,fieldnames=sadrzaj.fieldnames)
pisanje.writeheader()
for pjesma in top10:
    pisanje.writerow(pjesma)
    print(pjesma["Track.Name"], pjesma["Energy"], pjesma["Popularity"])
f4.close()
"""

#ZADATAK 4
"""f = open("pjesme.csv")
sadrzaj = csv.DictReader(f)
pjesme = []

f.close()

zanrovi = {}

for pjesma in sadrzaj:
    zanr = pjesma["Genre"]
    if pjesma["zanr"] not in zanrovi:
        zanrovi[pjesma["zanr"]] = 1
    else:
        zanrovi[pjesma["zanr"]]+=1

print(zanrovi)"""

#ZADATAK 5
f = open("cars.csv", newline="")
sadrzaj = csv.DictReader(f)
cars = []

godina = int(input("Unesite godinu"))

for red in sadrzaj:
    if int(red["year"])>=godina:
        cars.append(red)

f.close()
print(cars)

f2 = open("filter.csv", mode="w", newline="")

pisanje = csv.DictWriter(f2,fieldnames=sadrzaj.fieldnames)
pisanje.writeheader()
for car in cars:
    pisanje.writerow(car)
f2.close()