def tulosta_inventaario(esineet):
    esineetCapped = [] #alustetaan lista
    for i in esineet:
        esineetCapped.append(i.capitalize()) #Syötetään tuplen sisältö listaan

    print(esineetCapped) #printataan listana
    esineetCapped = tuple(esineetCapped) #lista takaisin tupleksi
    return esineetCapped


inventaario = ("lyhty", "kirja", "Kahvipaketti") # Syötetään tuple
print(inventaario)
print(tulosta_inventaario(inventaario))
