def on_ananasta(ainekset = ""):
    ananasSpotted = False
    for aines in ainekset:
        print(aines)
        if aines == "ananas":
            ananasSpotted = True

    return ananasSpotted


    


if on_ananasta(['tonnikala', 'punasipuli', 'ananas', 'herkkusieni', 'paprika']):
    print('Tässä pizzassa on ananasta.')
    vastaus = input('Kuuluuko ananas pizzaan (k/e)? ')
    print(f'OK, kunnioitan mielipidettäsi.')
else:
    print('Tässä pizzassa ei ole ananasta.')
