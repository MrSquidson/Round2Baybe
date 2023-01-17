# Opgave Læg to bruger bestemte værdier sammen
#
# Beder brugeren om deres navn for en mere personlig **Experience**
navnet = input("Skriv dit navn")
print('Hej', navnet)
print('Jeg er et program der skal hjælpe dig med at lægge 2 tal sammen... Er du klar?')

while True:

    #   Indsamler tal 1
    try:
        tal1 = int(input("Skriv dit første tal"))
#       Hvis tallet ikke kan godkendes af maskinen eller
#       brugeren har indtastet et bogstav giver den en besked + fejlkode
    except Exception as e:
        print('Det virker ikke')
        exit('Ikke et Realt tal')

    print('Dit første tal er:', tal1)

#   Indsamler tal 2
    try:
        tal2 = int(input('Skriv dit andet tal'))
#       Hvis tallet ikke kan godkendes af maskinen eller
#       brugeren har indtastet et bogstav giver den en besked + fejlkode
    except Exception as e:
        print('Det virker ikke')
        exit('Ikke et Realt tal')

    print('Dit andet tal er', tal2)

    resultat = tal1 + tal2

#   Skaber en string der vil fortælle os om tallet er lige el. ulige
    ligeEllerUlige = 'ikke bestemt'
#   Tjekker om tallet er lige eller ulige
    if (resultat % 2) == 0:
        ligeEllerUlige = 'lige'
    else:
        ligeEllerUlige = 'ulige'

#   Lægger de 2 tal der er indsamlet i int strings sammen og viser om tallet er lige el. ulige på samme linje
    print('Din samlede værdi mellem de to tal er', resultat, 'resultatet er et', ligeEllerUlige, 'tal')

#   Finder ud af om resultatet er et primtal
    if resultat > 1:
        for i in range(2, resultat//2):
            if (resultat % i) == 0:
                print('Dit resultat', resultat, "er ikke et primtal")
                break
            else:
                print('Dit resultat', resultat, "er et primtal")
    else:
        print('Dit resultat', resultat, "er ikke et primtal")
