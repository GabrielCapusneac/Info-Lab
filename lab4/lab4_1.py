def afisare_cuvinte_sir(sir):
    cuvinte_sir = sir.split()
    print("cuvinte sir", len(cuvinte_sir))
    for i in cuvinte_sir:
        print(i,"-",len(i),"caractere")
def inlocuire_x_y(sir):
    x=input("introduceti caracter de inlocuit: ")
    y=input("introduceti caracterul dorit: ")
    if x in sir:
        sir_nou=sir.replace(x,y)
        return sir_nou
    else:
        return sir

def majuscule_sir(sir):
    sir_nou=""
    for i in sir:
        if i.isupper:
            sir_nou=sir_nou+i
    print(sir_nou)

def afisare_vocale(sir):
    print("Numarul de vocale A,a este de ",sir.count('A')+sir.count('a')," vocale")
    print("Numarul de vocale E,e este de ", sir.count('E') + sir.count('E'), " vocale")
    print("Numarul de vocale I,i este de ", sir.count('I') + sir.count('i'), " vocale")
    print("Numarul de vocale O,o este de ", sir.count('O') + sir.count('o'), " vocale")
    print("Numarul de vocale U,u este de ", sir.count('U') + sir.count('u'), " vocale")

def caracter_special(sir):
    sir_caractere_special=" "
    for spec in sir:
        if spec.isalnum():
            sir_caractere_special+=spec
    print(sir_caractere_special)

def poz_caracter(sir):
    poz=int(input("dati pozitia: "))
    sir_poz=sir[poz:] #+sir[0:poz]
    print(sir)
    print(sir_poz)

def afisare_meniu():
    while 1:
        print("Meniu principal")
        print("[1]. Citire sir: ")
        print("[2]. Afisare sir: ")
        print("[3]. Afisarea nr total de cuvinte din sir, cuvintele si a nr. de caractere pentru fiecare cuvant:" )
        print("[4]. Inlocuire caracterului <<X>> in sirul initial cu caracterul <<Y>>: ")
        print("[5]. Construiti un sir nou format din caracterele majuscule din sirul initial: ")
        print("[6]. Afisati numarul de aparitii pentru fiecare vocala din sirul initial: ")
        print("[7]. Eliminati caracterele speciale din sirul initial")
        print("[8]. Afisati INTREG sirul de caractere pornid de la o pozitie X - data")
        print("[9]. Exit")
        print("--------------------")
        optiune = input("Introduceti optiunea dorita: ")
        print("--------------------")

        if optiune == "1":
            sir=input("Introduce un sir de caractere: ")
        elif optiune == "2":
            print(sir)
        elif optiune == "3":
            print(afisare_cuvinte_sir(sir))
        elif optiune == "4":
            print(inlocuire_x_y(sir))
        elif optiune == "5":
            print(majuscule_sir(sir))
        elif optiune == "6":
            print(afisare_vocale(sir))
        elif optiune == "7":
            print(caracter_special(sir))
        elif optiune == "8":
            print(poz_caracter(sir))
        elif optiune == "9":
            break


if __name__ == '__main__':
    afisare_meniu()