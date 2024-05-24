
def citire():
   with open('input.txt', 'rt') as f:
        mat = []
        rang = int(f.readline())
        for i in range(rang):
            linie = [int(x) for x in f.readline().split()]
            mat.append(linie)
        subrang = int(f.readline())
        return mat, subrang


def meniu():
    print("1. Citire matrice")
    print("2. Afisare matrice")
    print("3. Scriere submatrice")
    print("4. Informatii autor")
    print('5. Exit')
    print('____________')
    opt = input("Introduceti optiunea dorita: ")
    while True:
        if opt == '1':
            mat, subrang = citire()
        elif opt == '2':
            print(mat)
        elif opt == '5':
            break
#codu asta nu merge

if __name__ == '__main__':
    meniu()
