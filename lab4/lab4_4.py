# def afisare_vocale(sir):
#     print("Numarul de vocale A,a este de ",sir.count('A')+sir.count('a')," vocale")
#     print("Numarul de vocale E,e este de ", sir.count('E') + sir.count('E'), " vocale")
#     print("Numarul de vocale I,i este de ", sir.count('I') + sir.count('i'), " vocale")
#     print("Numarul de vocale O,o este de ", sir.count('O') + sir.count('o'), " vocale")
#     print("Numarul de vocale U,u este de ", sir.count('U') + sir.count('u'), " vocale")

sir = str(input("Introduce sir: "))
vocale = 'AaEeIiOoUu'

sir_dub = ''
for i in sir:
    sir_dub += i
    if i in vocale:
        sir_dub += i
print(sir_dub)
