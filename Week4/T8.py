import time

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
            print(f'{sanat[1].capitalize()} otettu')
        if sanat[0] == "pudota":
            print(f'{sanat[1].capitalize()} pudotettu')
    time.sleep(2)
time.sleep(1)
print("Kiitos pelaamisesta")
