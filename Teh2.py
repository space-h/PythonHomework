


print("Titteli, isolla")
titteli = input()
print("Opettajan nimi, isolla")
opettaja = input()
print("mikä katosi")
kadonnutJuttu =  input()
print("mikä eläin")
elain =  input()
print("Lemmikin nimi")
lemmikin_Nimi = input()

if kadonnutJuttu[-1] == 't':
    seVAIne = 'ne'
else:
    seVAIne = 'se'

if seVAIne == 'se':
    toinen_seVAIne = "sen"
else:
    toinen_seVAIne = "ne"


print(f'Pahoitteluni, {titteli} {opettaja}, ei aavistustakaan mihin {seVAIne} {kadonnutJuttu} oikein joutui. Lemmikki{elain}ni {lemmikin_Nimi} varmaankin söi {toinen_seVAIne}.')
