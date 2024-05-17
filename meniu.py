# match optiune :
#     instructiune
# case opt 1:
#     inst
# case opt 2:
# if ....:


def citire_numere():
    nr1 = int(input("Introduceti primul numar: "))
    nr2 = int(input("Introduceti al doilea numar: "))
    return nr1, nr2


def adunare_numere(nr1, nr2):
    return nr1 + nr2


def scadere_numere(nr1, nr2):
    return nr1 - nr2


def inmultire_numere(nr1, nr2):
    return nr1 * nr2


def impartire_numere(nr1, nr2):
    return nr1 / nr2


def afisare_meniu():
    while 1:
        print("Meniu principal")
        print("[C]. Introduceti 2 numere intregi: ")
        print("[+]. Adunarea numerelor: ")
        print("[-]. Scaderea numerelor: ")
        print("[*]. Inmultirea numerelor: ")
        print("[/]. Impartirea numerelor: ")
        print("[x]. Exit")
        print("--------------------")
        optiune = input("Introduceti optiunea dorita: ")
        print("--------------------")
        if optiune == 'C':
            nr1, nr2 = citire_numere()
            print(nr1, nr2)
        elif optiune == '+':
            print(adunare_numere(nr1, nr2))
        elif optiune == '-':
            print(scadere_numere(nr1, nr2))
        elif optiune == '*':
            print(inmultire_numere(nr1, nr2))
        elif optiune == '/':
            print(scadere_numere(nr1, nr2))
        elif optiune == 'x':
            break


if __name__ == '__main__':
    afisare_meniu()
