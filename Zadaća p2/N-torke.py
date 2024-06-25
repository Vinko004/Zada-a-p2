import csv

#Dodajem vrijednosti reda
red_imena  = 1
red_prezimena = 2
red_bodovi = 3

#Liste gdje će se spremat podaci
imena = []
prezimena = []
bodovi = []

#Ovo sam napravio djelomično pomoću AI. Uglavnom, čitam CSV datoteku i njene vrijednosti spremam u niz(Naravno sa određenim uvijetima)
with open('P1_23_24_1K_REZ.csv', 'r') as read_obj:
    
    csv_reader = csv.reader(read_obj)
    
    for red in csv_reader:
        prezimena.append(red[red_prezimena - 1])
        imena.append(red[red_imena - 1])
        bodovi.append(red[red_bodovi - 1])
        
#Nizove skraćujem jer cijeli stupac sadrži više od potrebnih podataka
imena = imena[4:-3]
prezimena = prezimena[4:-3]
bodovi = bodovi[4:-3]

#ZIP-am tri liste u jednu
ukupno =  list(zip(imena, prezimena, bodovi))

#Samo ispisujemo studente koji su položili(Prvi dio zadatka)
print("Studenti koji su položili ispit su: ")
for element in ukupno:
    if int(element[2]) > 49:
        print(element)

#Drugi dio zadatka
#Ovdje sortiramo ntorku pomoću drugog elementa(prezime)
ukupno2 = sorted(ukupno, key=lambda x: x[1])

print("----------------------------------")
#Ovdje samo im dodjeljujemo ocjene
print("Ocjene su: ")
for element in ukupno2:
    if int(element[2]) >= 90:
        print(element," Izvrstan")
    elif int(element[2]) >= 80:
        print(element, " Vrlo dobar")
    elif int(element[2]) >= 65:
        print(element, " Dobar")
    elif int(element[2]) >= 50:
        print(element, " Dovoljan")
    else:
        print(element, " Nije položio/la")