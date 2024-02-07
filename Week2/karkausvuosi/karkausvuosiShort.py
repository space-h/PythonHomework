vuosi = int(input("Syötä Vuosi\n"))
if (vuosi % 400 == 0):
    karkausvuosi = True
elif (vuosi % 100 == 0):
    karkausvuosi = False
elif (vuosi % 4 == 0):
    karkausvuosi = True
else:
    karkausvuosi = False

if karkausvuosi == True:
    print(f"{vuosi} on karkausvuosi")
else:
    print(f"{vuosi} ei ole karkausvuosi")

