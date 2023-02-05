# Opgave Læg to bruger bestemte værdier sammen
# Importere textwrap
import textwrap
# Importere colorama og tillader farvede outputs i console
from colorama import Fore
import math

# Beder brugeren om deres navn for en mere personlig **Experience**
navnet = input(Fore.BLUE + "NumZ: Skriv dit navn: ")
print(Fore.BLUE + 'NumZ: Hej', navnet)
print(Fore.BLUE + 'NumZ: Jeg er et program der skal hjælpe dig med at lægge 2 tal sammen... Er du klar?')

# Laver strings til wrapper så hvis man inputer et meget stort tal kommer det tilbage på linjen
preferredWidth = 70

# Looper det hele
while True:
    # Laver Prefixes med custom farve ved hjælp af colorama
    prefix = Fore.GREEN + navnet + ": "
    prog = Fore.BLUE + "NumZ: "

    # Indsamler tal 1
    def talNummerEt():
        # Laver en wrapper til hvis der er meget store tal
        global wrapper
        wrapper = textwrap.TextWrapper(initial_indent=prog, width=preferredWidth, subsequent_indent=' ' * len(prog))

        try:
            print(wrapper.fill(Fore.BLUE + "Skriv dit første tal"))
            # int sørger for at string'en der er indtastet er et tal/integer
            global tal1
            tal1 = int(input(prefix))
            print(Fore.LIGHTCYAN_EX + '\t\t\tDit første tal er:', tal1)
            talNummerTo()

        #       Hvis tallet ikke kan godkendes af maskinen eller
        #       brugeren har indtastet et bogstav giver den en besked + fejlkode
        except ValueError:
            print(wrapper.fill(Fore.RED + '\tDet virker ikke'))
            print(wrapper.fill(Fore.RED + '\tIkke et Realt tal'))
            talNummerEt()


    def talNummerTo():
        #   Indsamler tal 2
        try:
            print(wrapper.fill('Skriv dit andet tal'))
            global tal2
            tal2 = int(input(prefix))
            print(Fore.LIGHTCYAN_EX + '\t\t\tDit andet tal er', tal2)
            mat()

        #       Hvis tallet ikke kan godkendes af maskinen eller
        #       brugeren har indtastet et bogstav giver den en besked + fejlkode
        except ValueError:
            print(wrapper.fill(Fore.RED + '\tDet virker ikke'))
            print(wrapper.fill(Fore.RED + '\tIkke et Realt tal'))
            talNummerTo()


    def mat():
        global resultat
        resultat = tal1 + tal2

        #   Tjekker om tallet er lige eller ulige
        if (resultat % 2) == 0:
            ligeEllerUlige = Fore.GREEN + 'lige'
        else:
            ligeEllerUlige = Fore.RED + 'ulige'

        #   Lægger de 2 tal der er indsamlet i int strings sammen og viser om tallet er lige el. ulige på samme linje
        print(Fore.LIGHTBLUE_EX + '\t\t\tDin samlede værdi mellem de to tal er', resultat, 'resultatet er et',
              ligeEllerUlige, 'tal')
        er_primtal()

        #   Finder ud af om resultatet er et primtal


    def er_primtal(resultat):
        if resultat % 2 == 0 and resultat > 2:
            return False
        for i in range(3, int(math.sqrt(resultat)) + 1, 2):
            if resultat % i == 0:
                return False
        return True

        print(wrapper.fill(Fore.BLUE + "\t  Hvis du vil lægge flere tal sammen så prøver vi en gang til"))

    talNummerEt()
