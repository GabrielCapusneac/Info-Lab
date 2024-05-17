def cit_mat():
    global nume, mat, n, m
    nume = input("Nume matrice: ")
    n = int(input("Nr de linii: "))
    m = int(input("Nr de coloane: "))
    mat = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            mat[i][j] = int(input(f'Dati elem pozitiei [{i}] [{j}]: '))


def afisare_mat():
    global mat
    for linie in mat:
        print(linie)


def max_lin():
    global mat
    maxim = []
    for linie in mat:
        # for i in linie:
        # maxim.append(i)
        maxim.append(max(linie))
        print(f'Maximul liniei este {maxim}')


def flip_mat():
    global mat, m, n
    max_col = [0] * m
    coloana = [0] * n
    for j in range(m):
        for i in range(n):
            coloana[i] = mat[i][j]
        max_col[j] = max(coloana)
        # print(coloana)
    print(f'max de coloana:{max_col}')


def transpusa():
    global mat
    m = len(mat)
    n = len(mat[0])

    mat_tras = [[0 for j in range(m)] for i in range(n)]
    for i in range(m):
        for j in range(n):
            mat_tras[j][i] = mat[i][j]

    print(f'Matrice tras: ')
    for linie in mat_tras:
        print(linie)


def meniu():
    while True:
        print('[1]. Citire matrice de la tastatura (pe linii)')
        print('[2]. Afisare matrice')
        print('[3]. Creare si afisare lista de elemente maxime de pe linii')
        print('[4]. Creare si afisare lista de elemente maxime de pe coloane')
        print('[5]. Afisare matrice transpusa')
        print('[6]. Adauga linie')
        print('[7]. Adauga coloana')
        print('[8]. Sterge linie')
        print('[9]. Sterge coloana')
        print('[10]. Liniarizare matrice (creare si afisare vector rezultat)')
        print('[11]. exit')
        print('------------------------')
        opt = input('Introduceti optiunea:')

        if opt == '1':
            cit_mat()
        elif opt == '2':
            afisare_mat()
        elif opt == '3':
            max_lin()
        elif opt == '4':
            flip_mat()
        elif opt == '5':
            transpusa()


if __name__ == '__main__':
    meniu()
