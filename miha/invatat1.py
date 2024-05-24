def citire_matrice():
    global matrice, n, m
    n=int(input("Dati numarul de randuri in matrice: "))
    m=int(input("Dati numarul de coloane in matrice: "))
    matrice=[[0 for j in range (m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            matrice[i][j]=int(input(f"Dati numarul pe pozitia [{i}][{j}]: " ))

def afisare_matrice():
    global matrice
    for linie in matrice:
        print(linie)

def tranpuusa





def meniu():
    while True:
        print("1. Citire matrice")
        print("2. Afisare matrice")
        print("4. Transpusa matricii")
        print("0. Exit")
        print("---------------")
        opt=input("Introduceti optiunea dorita: ")
        if opt=='1':
            citire_matrice()
        elif opt=='2':
            afisare_matrice()
        elif opt=='3':
            transpusa()
        elif opt=='0':
            break

if __name__ == '__main__':
    meniu()