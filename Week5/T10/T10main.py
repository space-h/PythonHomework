from T10function import *


while True:
    checker = "pelataan"
    komento = input("\nAnna komento\n")
    komento = komento.strip()
    sanat = komento.split()

    if len(sanat) == 0:
        print("Syöte liian lyhyt\n")

    if len(sanat) == 1:
        checker = userInputOneWord(sanat[0])
        print(checker)

    if len(sanat) == 2:
        userInputTwoWords(sanat[0],sanat[1])
        
    if len(sanat) > 2:
        print("Syöte liian pitkä\n")
    if checker == "Peli ohi":
        break
