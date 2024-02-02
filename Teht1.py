lokakuu_kulutus = 642.934
marraskuu_kulutus = 674.345
joulukuu_kulutus = 757.599
#yksikko KWH

#senttia
perusmaksu_energia = 198 #per kuukausi
perusmaksu_siirto = 477 #per kk
energiamaksu = 7.09 #per kwh
siirtomaksu = 2.9264 #per kwh
vero = 2.79372 #kwh

perusyht = perusmaksu_energia + perusmaksu_siirto #per kk

muuttuvatKustannukset = energiamaksu + siirtomaksu + vero



lokakuu = round(muuttuvatKustannukset * lokakuu_kulutus  + perusyht)
marraskuu = round(muuttuvatKustannukset * marraskuu_kulutus  + perusyht)
joulukuu = round(muuttuvatKustannukset * joulukuu_kulutus  + perusyht)

total = lokakuu + marraskuu + joulukuu

loppusumma = total / 100
print(f'Lasku on {loppusumma} euroa')
