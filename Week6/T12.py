def tulosta_inventaario(esineet=""):  
    if not esineet:
        print("Sinulla ei ole esineitä")
        return esineet
    
    for item in esineet:
        print("- "+ item.capitalize())

    return esineet


inventaario = ("lyhty", "kirja", "Kahvipaketti")
tulosta_inventaario(inventaario)



