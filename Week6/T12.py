def tulosta_inventaario(esineet=""):  
    if not esineet:
        print("Sinulla ei ole mukana mitään.")
        return esineet
    print("Sinulla on mukana: ")
    for item in esineet:
        print("- "+ item.capitalize())

    return esineet


inventaario = ("lyhty", "kirja", "Kahvipaketti")
tulosta_inventaario(inventaario)



