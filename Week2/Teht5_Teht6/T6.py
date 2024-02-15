state = True

while state == True:
    komento = input("Anna komento\n")

    sanat = komento.split()


    sanatLKM = len(sanat)

    firstWord=sanat[0].strip()
    if firstWord == "lopeta":
        print("OK, kiitos pelistä! Nähdään taas!")
        state = False

    elif sanatLKM == 1:
        print(f'"{sanat[0]}" mitä? En ymmärtänyt')

    elif sanatLKM == 2:
        print(f'Ahaa, siis "{sanat[0]} {sanat[1]}".')

    print("\n")

