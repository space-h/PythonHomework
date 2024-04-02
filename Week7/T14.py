sanalista = []
sana = "Null"
counter = 0


while True:
    if sana == "":
        break
    sana = input("Anna sana\n")
    if len(sana) > 1:
        sanalista.append(sana)


print(sanalista)

for x in range(0,len(sanalista)):
    for y in range(0,len(sanalista[x])):
        counter = counter + 1

max_len = -1
for testattava in sanalista:
    if len(testattava) > max_len:
        max_len = len(testattava)
        pisinSana = testattava

min_len = 3000
for testattavaLyhyt in sanalista:
    if len(testattavaLyhyt) < min_len:
        min_len = len(testattavaLyhyt)
        lyhyinSana = testattavaLyhyt        

print(f"Lyhyin sana oli {lyhyinSana}")        
print(f"Pisin sana oli {pisinSana}")
print(f"kaikkien sanojen yhteispituus: {counter} merkkiä")

#Toteutuksessa ensimmäinen sana joka on yhtä lyhyt kuin lyhyin ilmoitetaan
#Tilanteen voisi korjata tekemällä listan johon
#lisätä aina kun tulee saman mittainen sana, ja
#sitten putsamalla listan jos tulee lyhyempi
