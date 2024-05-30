def meniu():
    while True:
        print("""
    Meniul:
    1. Creare baza de date pacienti
    2. Afisare lista pacienti
    3. Afisare pacienti hipertensiune
    4. Fisier iesire cu baza de date de pacienti
    5. Exit
    --------
        """)
        opt = input('Introduceti optiunea dorita: ')
        if opt == '1':
            baza_date = creare_baza_date()
        elif opt == '2':
            afisare_lista_pacienti(baza_date)
        elif opt == '3':
            afisare_pacienti_hipertensiune(baza_date)
        elif opt == '4':
            fisier_iesire(baza_date)
        elif opt == '5':
            break
        else:
            print('Optiune invalida, va rugam sa reincercati.')

def creare_baza_date():
    baza_date = []
    n = int(input('Dati numarul de pacienti pe care vreti sa ii adaugati: '))
    for i in range(n):
        pacient = {}
        pacient['ID'] = input(f'ID Pacient {i + 1}: ')
        pacient['Nume'] = input(f'Nume Pacient {i + 1}: ')
        pacient['Prenume'] = input(f'Prenume Pacient {i + 1}: ')
        pacient['TS'] = float(input(f'Tensiune Sistolica (TS) Pacient {i + 1}: '))
        pacient['TD'] = float(input(f'Tensiune Diastolica (TD) Pacient {i + 1}: '))
        pacient['TM'] = pacient['TS'] + pacient['TD']
        baza_date.append(pacient)
    return baza_date


def afisare_lista_pacienti(baza_date):
    print('ID \t Nume \t Prenume \t TS \t TD \t TM')
    for pacient in baza_date:
        print(
            f"{pacient['ID']} \t {pacient['Nume']} \t {pacient['Prenume']} \t {pacient['TS']} \t {pacient['TD']} \t {pacient['TM']}")


def afisare_pacienti_hipertensiune(baza_date):
    print('ID \t Nume \t Prenume \t TS \t TD \t TM')
    for pacient in baza_date:
        if pacient['TS'] > 40 or pacient['TM'] > 100:
            print(
                f"{pacient['ID']} \t {pacient['Nume']} \t {pacient['Prenume']} \t {pacient['TS']} \t {pacient['TD']} \t {pacient['TM']}")


def fisier_iesire(baza_date):
    with open('baza_date_pacienti.txt', 'w') as file:
        file.write('ID \t Nume \t Prenume \t TS \t TD \t TM\n')
        for pacient in baza_date:
            file.write(
                f"{pacient['ID']} \t {pacient['Nume']} \t {pacient['Prenume']} \t {pacient['TS']} \t {pacient['TD']} \t {pacient['TM']}\n")
    print('Datele au fost salvate in fisierul baza_date_pacienti.txt')


if __name__ == '__main__':
    baza_date = []
    meniu()
