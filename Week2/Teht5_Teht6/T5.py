vuosi = int(input("Anna vuosiluku: \n"))
if (vuosi % 400 == 0):
    karkausvuosi = True
elif (vuosi % 100 == 0):
    karkausvuosi = False
elif (vuosi % 4 == 0):
    karkausvuosi = True
else:
    karkausvuosi = False



kuukausi = int(input("Anna kuukauden numero (1-12): \n"))

if kuukausi == 1:
    monthToText = "tammikuussa"
elif kuukausi == 2:
    monthToText = "helmikuussa"
elif kuukausi == 3:
    monthToText = "maaliskuussa"
elif kuukausi == 4:
    monthToText = "huhtikuussa"
elif kuukausi == 5:
    monthToText = "toukokuussa"
elif kuukausi == 6:
    monthToText = "kesakuussa"
elif kuukausi == 7:
    monthToText = "heinakuussa"
elif kuukausi == 8:
    monthToText = "elokuussa"
elif kuukausi == 9:
    monthToText = "syyskuussa"
elif kuukausi == 10:
    monthToText = "lokakuussa"
elif kuukausi == 11:
    monthToText = "marraskuussa"
elif kuukausi == 12:
    monthToText = "joulukuussa"
else:
    monthToText = "invalidInput"
    
if kuukausi == 1:
    paivienLKM = 31
elif kuukausi == 2:
    paivienLKM = 28
elif kuukausi == 3:
    paivienLKM = 31
elif kuukausi == 4:
    paivienLKM = 30
elif kuukausi == 5:
    paivienLKM = 31
elif kuukausi == 6:
   paivienLKM = 30
elif kuukausi == 7:
    paivienLKM = 31
elif kuukausi == 8:
    paivienLKM = 31
elif kuukausi == 9:
    paivienLKM = 30
elif kuukausi == 10:
    paivienLKM = 31
elif kuukausi == 11:
    paivienLKM = 30
elif kuukausi == 12:
    paivienLKM = 31
else:
    paivienLKM = "invalidInput"

if kuukausi == 2:
    if karkausvuosi == True:
        paivienLKM = 29
   

print(f'Vuonna {vuosi} {monthToText} on {paivienLKM} päivää.')


