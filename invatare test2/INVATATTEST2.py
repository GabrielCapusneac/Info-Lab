def citire_matrice():
    # global nume, mat, n, m
    # # nume = input("Nume matrice: ")
    # n = int(input("Nr de linii: "))
    # m = int(input("Nr de coloane: "))
    # mat = [[0 for j in range(m)] for i in range(n)]
    # for i in range(n):
    #     for j in range(m):
    #         mat[i][j] = int(input(f'Dati elem pozitiei [{i}] [{j}]: '))
    #
    global coloane, randuri, matrice
    coloane=int(input("Numarul de coloane: "))
    randuri=int(input("Numarul de randuri: "))
    matrice=[]

    for i in range(randuri):
        rand=[]
        for j in range(coloane):
            rand.append(int(input()))
def afisare_matrice():
    # global mat
    # for linie in mat:
    #     print(linie)
    global coloane, randuri
    for i in range(randuri):
        for j in range(coloane):
            print(matrice[i][j],end=" ")


def meniu():
    while 1:
        print("[1]. citire matrice")
        print("[2]. Afisare matrice")
        print("[3]. Afisare lungimii sirului")
        print("[9]. exit")
        optiune = input("introduceti optiunea: ")
        if optiune == 1:
            citire_matrice()

        elif optiune == 2:
            afisare_matrice()
        elif optiune == 3:
            pass
        elif optiune == 4:
            pass

        elif optiune == 9:
            break


if __name__ == '__main__':
    meniu()
