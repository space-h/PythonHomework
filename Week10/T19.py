print('Avataan tiedosto rivit.txt, ja syötetään tekstiä \nkunnes annetaan "lopeta" käsky')

f = open("rivit.txt", "a")
f.write("-" * 10 + "\n")
while True:
    rivi = input()
    if rivi == "lopeta":
        break
    else:
        f.write(rivi + "\n")
f.close()
