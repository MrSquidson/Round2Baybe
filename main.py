#Opgave Læg to bruger bestemte værdier sammen

#Beder brugeren om deres navn for en mere personlig **Experience**
navnet = input("Skriv dit navn")
print('Hej', navnet)
print('Jeg er et program der skal hjælpe dig med at lægge 2 tal sammen... Er du klar?')

#Indsamler tal 1
try:
    tal1 = int(input("Skriv dit første tal"))
#       Hvis tallet ikke kan godkendes af maskinen eller
#       brugeren har indtastet et bogstav giver den en besked + fejlkode
except:
    print('Det virker ikke')
    exit('Ikke et Realt tal')

print('Dit første tal er:', tal1)

#Indsamler tal 2
try:
    tal2 = int(input('Skriv dit andet tal'))
#Se linje 11
except:
    print('Det virker ikke')
    exit('Ikke et Realt tal')

print('Dit andet tal er', tal2)

#Lægger de 2 tal der er indsamlet i int strings sammen
print('Din samlede værdi mellem de to tal er', tal1 + tal2)
