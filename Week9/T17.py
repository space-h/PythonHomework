def sekuuttiMuunnos(s):
    minutes = s // 60
    leftoverSekunnit = s % 60
    valmis = str(f"{minutes}:{leftoverSekunnit}")
    return valmis


recordSides = {"A": 0, "B": 0}

myfile = open("vinyylit.txt", "r")
myline = myfile.readline()

while myline:
    if myline[0] in recordSides:
        sekunnit = int(myline[5]+myline[6])
        recordSides[myline[0]]+=sekunnit
        minuutit = int(myline[3])
        #muutetaan minuutit sekunneiksi ja lisätään
        #ensimmäistä kirjainta vastaavaan avainpariin
        recordSides[myline[0]]+=minuutit * 60    
    myline = myfile.readline()
    
myfile.close()

for key, value in recordSides.items():
    print(f"{key} - {sekuuttiMuunnos(value)}")


print(f"Total - {sekuuttiMuunnos(sum(recordSides.values()))}")





