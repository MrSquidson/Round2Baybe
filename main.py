#Læg to bruger bestemte værdier sammen
navnet = input("Skriv dit navn")
print('Hej', navnet)
print('Jeg er et program der skal hjælpe dig med at lægge 2 tal sammen... Er du klar?')

try:
    tal1 = int(input("Skriv dit første tal"))
except:
    print('Det virker ikke')
    exit('Ikke et Realt tal')

print('Dit første tal er:', tal1)

try:
    tal2 = int(input('Skriv dit andet tal'))
except:
    print('Det virker ikke')
    exit('Ikke et Realt tal')

print('Dit andet tal er', tal2)

print('Din samlede værdi mellem de to tal er', tal1 + tal2)
