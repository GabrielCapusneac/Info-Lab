def citire_fis(fisier):
    with open(fisier, 'r') as f:
        mat = []
        rang = int(f.readline())
        for i in range(rang):
            linie = [int(x) for x in f.readline().split()]
            mat.append(linie)
        subrang = int(f.readline())
        return mat, subrang


def calcul_suma(mat, i, j, subrang):
    suma = 0
    output = ''
    for x in range(i, i + subrang):
        suma += sum(mat[x][j:j + subrang])
        output += str(mat[x][j:j + subrang]) + '\n'
    output += 'Suma = ' + str(suma) + '\n'
    return suma, output


def suma_submatrici(mat, subrang):
    sume = []
    out = ''
    for i in range(len(mat) - subrang + 1):
        for j in range(len(mat) - subrang + 1):
            suma, output = calcul_suma(mat, i, j, subrang)
            out += output
            sume.append(suma)
    return sume, out


def optiune():
    meniu = {}
    meniu[1] = 'Citire din fisier'
    meniu[2] = 'Afisare matrice'
    meniu[3] = 'Calcul sume submatrici + salvare in fisier a rezultatului'
    meniu[4] = 'Info autor'
    meniu[5] = 'Exit'
    for k in meniu:
        print(k, meniu[k])
    opt = int(input('Dati o optiune:'))
    return opt


if __name__ == '__main__':
    while (1):
        match optiune():
            case 1:
                mat, subrang = citire_fis('input.txt')
            case 2:
                print(mat)
            case 3:
                suma, output = suma_submatrici(mat, subrang)

#cod de la duceac