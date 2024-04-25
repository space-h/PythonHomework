import json

with open('pelaaja.json', 'r') as f:
    data = json.load(f)
    
print(f"Ennen ajoa: {data}")
data["playerInfo"][0]["pelaaja"] = "J"
data["playerInfo"][0]["pisteet"] = data["playerInfo"][0]["pisteet"] + 10
data["playerInfo"][0]["esineet"] = ["piano", "rumpu", "kukka"]

with open('pelaaja.json', 'w') as f:
     json.dump(data, f, indent=4)
    

print(f"Ajon jälkeen {data}")
f.close()
