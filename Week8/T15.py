playerInfo = {
    "name": "",
    "pisteet": 0,
    "esineet": [],
}

print(playerInfo)

while True:
    name = input("Hei, anna nimesi aloittaaksesi\n")
    name = name.strip()
    name = name.capitalize()
    if name:
        break


playerInfo["name"] = name
print("Olet syöttänyt nimesi, sait 5 pistettä")
playerInfo["pisteet"] = playerInfo["pisteet"] + 5
print("Pelaaja löytää ja sytyttää lyhdyn")
playerInfo["esineet"].append("Lyhty")
print(f'Pelaajalla {playerInfo["name"]} on nyt {"".join(playerInfo["esineet"])} ja {playerInfo["pisteet"]} pistettä')
