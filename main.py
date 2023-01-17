# Opgave Læg to bruger bestemte værdier sammen
# Importere textwrap
import textwrap

# Beder brugeren om deres navn for en mere personlig **Experience**
navnet = input("Skriv dit navn: ")
print('Hej', navnet)
print('Jeg er et program der skal hjælpe dig med at lægge 2 tal sammen... Er du klar?')

# Laver strings til wrapper så hvis man inputer et meget stort tal kommer det tilbage på linjen
preferredWidth = 70

# Looper det hele
while True:
    # Importere colorama og tillader farvede outputs i console
    from colorama import Fore, Back, Style

    # Laver Prefixes med custom farve ved hjælp af colorama
    prefix = Fore.GREEN + navnet + ": "
    prog = Fore.BLUE + "NumZ: "

    # Laver en wrapper til hvis der er meget store tal
    wrapper = textwrap.TextWrapper(initial_indent=prog, width=preferredWidth, subsequent_indent=' ' * len(prog))
    #   Indsamler tal 1
    try:

        print(wrapper.fill(Fore.BLUE + "Skriv dit første tal"))
        tal1 = int(input(prefix))
#       Hvis tallet ikke kan godkendes af maskinen eller
#       brugeren har indtastet et bogstav giver den en besked + fejlkode
    except Exception as e:
        print(wrapper.fill(Fore.RED + '\tDet virker ikke'))
        exit(wrapper.fill(Fore.RED + '\tIkke et Realt tal'))

    print(Fore.LIGHTCYAN_EX + '\t\tDit første tal er:', tal1)

#   Indsamler tal 2
    try:
        print(wrapper.fill('Skriv dit andet tal'))
        tal2 = int(input(prefix))
#       Hvis tallet ikke kan godkendes af maskinen eller
#       brugeren har indtastet et bogstav giver den en besked + fejlkode
    except Exception as e:
        print(wrapper.fill(Fore.RED + '\tDet virker ikke'))
        exit(wrapper.fill(Fore.RED + '\tIkke et Realt tal'))

    print(Fore.LIGHTCYAN_EX + '\t\tDit andet tal er', tal2)

    resultat = tal1 + tal2

#   Skaber en string der vil fortælle os om tallet er lige el. ulige
    ligeEllerUlige = 'ikke bestemt'
#   Tjekker om tallet er lige eller ulige
    if (resultat % 2) == 0:
        ligeEllerUlige = Fore.GREEN + 'lige'
    else:
        ligeEllerUlige = Fore.RED + 'ulige'

#   Lægger de 2 tal der er indsamlet i int strings sammen og viser om tallet er lige el. ulige på samme linje
    print(Fore.LIGHTBLUE_EX + '\t\tDin samlede værdi mellem de to tal er', resultat, 'resultatet er et', ligeEllerUlige, 'tal')

#   Finder ud af om resultatet er et primtal
    if resultat > 1:
        for i in range(2, resultat//2):
            if (resultat % i) == 0:
                print(Fore.LIGHTBLUE_EX + '\t\tDit resultat', resultat, Fore.RED + "er ikke et primtal")
                break
            else:
                print(Fore.LIGHTBLUE_EX + '\t\tDit resultat', resultat, Fore.GREEN + "er et primtal")
    else:
        print(Fore.LIGHTBLUE_EX + '\t\tDit resultat', resultat, Fore.RED + "er ikke et primtal")
