def on_karkaus(vuosi):
    karkausvuosi = False
    
    if (vuosi % 400 == 0):
        karkausvuosi = True
    elif (vuosi % 100 == 0):
        karkausvuosi = False
    elif (vuosi % 4 == 0):
        karkausvuosi = True
    else:
        karkausvuosi = False

    return karkausvuosi


for y in range(1896, 2025):
    if on_karkaus(y):
        print(f"{y} On karkausvuosi")
    else:
        print(f"{y} Ei ole karkausvuosi")
