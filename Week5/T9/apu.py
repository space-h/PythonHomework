
"""
Lukee käyttäjältä luvun ja varmistaa,
että se on annetulla välillä.
"""

def lue_kokonaisluku(kehote, pienin, suurin):



    tulos = 0
    ok = False
    while not ok:
        teksti = input(kehote + "\n") 
        tulos = int(teksti)
        if tulos >= pienin and tulos <= suurin:
            ok = True
        else:
            print(f'Luvun pitää olla välillä {pienin}-{suurin}. Yritä uudelleen!')

    return tulos

#En ihan ymmärtänyt mitä tarkoitat oletusarvolla, niin laitoin maksimiarvoiksi
def lue_desimaaliluku(kehote, pienin, suurin):
    tulos = 0
    ok = False
    while not ok:

        teksti = input(kehote + "\n") 
        tulos = float(teksti)
        if tulos >= pienin and tulos <= suurin and tulos >= 0 and tulos <= 1:
            ok = True
        else:
            print(f'Luvun pitää olla välillä {pienin}-{suurin}. Yritä uudelleen!')

    return tulos
