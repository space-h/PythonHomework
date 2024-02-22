nuottiarray = [0] * 128

for i in range (127):
    nuottiarray[i] = i


z = int(input("Aloituspiste\n"))
y = int(input("Lopetuspiste\n"))
x = int(input("Askellusväli\n"))
print (nuottiarray[z:y:x])


#Alla itselle paremmin ymmarrettavassa muodossa


nuottiarray = [0] * 128

i = 0
while i < 128:
    nuottiarray[i] = i
    i = i + 1


z = int(input("Aloituspiste\n"))
y = int(input("Lopetuspiste\n"))
x = int(input("Askellusväli\n"))
print (nuottiarray[z:y:x])
