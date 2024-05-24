# dex_meniu={
#     '1. Generare matrice',
#     '2. Afisare Matrice',
#     '3. Transpusa matricei',
#     '9. Exit',
#     '-------------'
# }
def introducere_matrice(r, c):
    # global matrice
    # r = int(input("Introduceti numarul de randuri: "))
    # c = int(input("Introduceti numarul de coloane: "))
    matrice = []

    for i in range(r):
        rand = []
        for j in range(c):
            nr = int(input(f"Introduceti nr de la pozitia ({i + 1},{j + 1}):"))
            rand.append(nr)
        matrice.append(rand)
    return matrice

# def afisare(matrice):


def meniu():
    print('1. Generare matrice')
    print('2. Afisare Matrice')
    print('3. Transpusa matrice')
    print('9. Exit')
    opt = input('introduceti optiunea dorita: ')
    while True:
        if opt == '1':
            r = int(input("Introduceti numarul de randuri: "))
            c = int(input("Introduceti numarul de coloane: "))
            # matrice = introducere_matrice(r, c)
            matrice = introducere_matrice()
        elif opt == '2':
            print(matrice)
        elif opt == '9':
            break


if __name__ == '__main__':
    meniu()
