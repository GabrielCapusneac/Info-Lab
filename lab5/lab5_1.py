import random as rnd


# rnd.randint(a,b)
# 0,20
def afisare_meniu():
    while True:
        print("Meniu principal")
        print("[A]. Generare vector de n elemente: ")
        print("[B]. Afisare")
        print("[C]. afisare elemente mai mari decat media aritmetica a elemetelor vectorului")
        print("[D]. Valoare Max si Min")
        print("[E]. Deplasare elemente cu x-pozitii; x-citit de la tastatura")
        print("[F]. Eliminare elemente care nu apartin intervalului [c,d]")
        print("[H]. Exit")
        print("--------------------")
        optiune = input("Introduceti optiunea dorita: ")
        print("--------------------")

        match optiune:
            case 'a' | 'A':
                n = int(input("Introduceti numarul de elemente: "))
                if n > 0 or n <= 20:
                    a, b = [int(x) for x in input("Dati capetele: ").split(',')]
                    v = [rnd.randint(a, b) for i in range(n)]
                    # return v

            case 'b' | 'B':
                print(v)

            case 'c' | 'C':
                media = sum(v) / len(v)
                print('Media este:', media)
                print('Numere mai mari decat media aritmetica sunt: ')
                for i in range(n):
                    if v[i] > media:
                        print(v[i], end=',')
                print('\n')

            case 'd' | 'D':
                maxim = max(v)
                print('Maximul este', maxim, 'si indexul este: ', v.index(maxim))
                minim = min(v)
                print('Minimul este', minim, 'si indexul este: ', v.index(minim))

            case 'e' | 'E':
                x = int(input("Dati pozitia de deplasare:"))
                if x > 0:
                    v = v[x - 1:] + v[:x - 1]
                    print(v)
                elif x == 0:
                    pass
                else:
                    v = v[x + 1:] + v[:x + 1]
                    print(v)

            case 'f' | 'F':
                vec_nou = []
                c, d = [int(x) for x in input("Dati capetele: ").split(',')]
                for i in range(n):
                    if v[i] in range(c + 1, d):
                        vec_nou.append(v[i])
                v = vec_nou
                print('elementele sunt: ',v)

            case 'h' | 'H':
                break

        # if optiune == "A":
        # # sir = input("Introduce primul sir de caractere: ")
        # # subsir = input("Introduce subsirul de caractere: ")
        #     n = input("Introduceti numarul de elemente: ")
        #     for i in range(0,n):
        #         print(i)
        #
        # elif optiune == "H":
        #     break


if __name__ == '__main__':
    afisare_meniu()
