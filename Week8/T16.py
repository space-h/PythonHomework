import time

#Käytetty viikon 4, tehtävää 8 pohjana

esineet = []


while True:
    komento = input("\nAnna komento\n")
    komento = komento.strip()
    sanat = komento.split()

    if not komento:
        print("Komento oli tyhjä")


    if len(sanat) == 1:
        if sanat[0] == "lopeta":
            print("Lopetetaan peli")
            break
        elif sanat[0] == "katso":
            print("Täällä ei ole mitään erityistä nähtävää.")
        elif sanat[0] == "mukana":
            print("Sinulla ei ole mukana mitään.")
    
    if len(sanat) == 2:
        if sanat[0] == "ota":
            if len(esineet) < 5:
                print(f'{sanat[1].capitalize()} otettu')
                esineet.append(sanat[1].capitalize())
                #tähän voisi lisätä vertailun että samaa esinettä ei voi ottaa useasti
            else:
                print("Inventaario täynnä, tee tilaa jos haluat ottaa lisää mukaan")
        if sanat[0] == "pudota":
            if sanat[1].capitalize() in esineet:
                esineet.remove(sanat[1].capitalize())
                print(f'{sanat[1].capitalize()} pudotettu')
            else:
                print("Ei sinulla ole sellaista")
                
    time.sleep(1)
time.sleep(1)
print("Kiitos pelaamisesta")
