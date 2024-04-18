from itertools import cycle
import time
f = open('tietovisa.txt', 'r', encoding='utf-8')

oikeat = 0
kysymyksetLKM = 0
mytuple = ("A)", "B)", "C)")
myit = cycle(mytuple)

for x in range(3):
    kysymys =  (f.readline().strip())
    print(kysymys)
    vastausvaihtoehdot = (f.readline().strip(),f.readline().strip(),f.readline().strip())
    for i in vastausvaihtoehdot:
        print(next(myit) + i , sep = " " )
        time.sleep(0.2)
        
    userVastaus = input('Vastauksesi: ')[0].upper()
    oikea_kirjain = f.readline().strip()[0].upper()

    if userVastaus == oikea_kirjain:
        print('Oikein!\n')
        oikeat = oikeat + 1
        kysymyksetLKM = kysymyksetLKM + 1
        time.sleep(1)
        
    else:
        print(f'Väärin, oikea vastaus on {oikea_kirjain}.\n')
        kysymyksetLKM = kysymyksetLKM + 1
        time.sleep(1)
    
f.close()


print(f"Tuloksesi: {oikeat} / {kysymyksetLKM}")
#tekijän huomio. T17:ää tuli hiottua vähän liikaakin, niin ei ollut paukkuja tähän, niin tästä tuli vähän tämmönen kakka
