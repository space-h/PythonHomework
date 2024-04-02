def lauseOnPalidromi(lause):
    lauseValmis = []
    lause = lause.replace(" ", "")
    lause = lause.lower()
    
    for l in lause:
        if l.isalpha() == True:
            lauseValmis.append(l)

    lause = "".join(lauseValmis)
    reversedWord = ''.join(list(reversed(lause)))
    return lause == reversedWord


lause = input("Anna lause\n")
print(lauseOnPalidromi(lause))
