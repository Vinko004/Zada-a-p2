import random
imena=['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan',
'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimena=['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez',
'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith',
'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

workers=[]
for i in range(15):
    imenaa = random.choice(imena)
    prezimenaa = random.choice(prezimena)
    satnica = random.uniform(4, 6)
    zaokruzeni_s = round(satnica, 2)

    workers.append(
        {"ime": imenaa, 
         "prezime": prezimenaa, 
         "satnica": zaokruzeni_s}
        )

for tjedni_sati in(workers):
    tjedni_sati["tjedni_sati"] = random.randint(20 ,30)

print(workers)

tuple_radnika = []

obracun = 0

for radnik in workers:
    tjedna = round(radnik["satnica"] * radnik["tjedni_sati"], 2)
    tuple_radnika.append((radnik["ime"], radnik["prezime"], tjedna))
    obracun += tjedna

print(tuple_radnika)

prosjecna_isplata = obracun / len(workers)

print("Isplata za tjedan je: ", round(obracun))

print("Prosjecna isplata za tjedan je: ", round(prosjecna_isplata))



if radnik in tuple_radnika:
    if radnik[2] > prosjecna_isplata:
        print("radnik", radnik[0], "ima veću prosječnuj plaću od", radnik[2])