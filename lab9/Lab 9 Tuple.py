# zile_sapt=('luni', 'marti', 'miercuri','joi','vineri','sambata','duminica')
# print('weekend:', zile_sapt[5:])
# print(zile_sapt[2])

# dex = {1: 'procesor',
#        2: 'placa de baza',
#        3: 'placa video',
#        4: 'memorie RAM',
#        5: 'SSD'}
# dex[1] = 'procesor_mod'
# print(dex)

# meniu={1: 'Intoducere date db',
#        2: 'Afisare stud',
#        3: 'Afisare note',
#        4: 'Afisare stud+note',
#        5: 'Cautare stud dupa nume',
#        6: 'Afisare stud promovati'}

def optiune():
    meniu = {1: 'Intoducere date db',
             2: 'Afisare stud',
             3: 'Afisare note',
             4: 'Afisare stud+note',
             5: 'Cautare stud dupa nume',
             6: 'Afisare stud promovati',
             7: 'info autor',
             8: 'exit'}
    for k in meniu:
        print(str(k) + '. ' + meniu[k])
    opt = int(input('Intoduceti optiunea dorita: '))
    return opt


def incarcare_date():
    tabStud = {}
    tabNote = {}
    n = int(input('Dati numarul de studenti pe care vreti sa ii adaugati: '))
    # for i in range(n):
    #        tabStud[i]=input(f'Student {i}: ')
    print(
        'Introduceti date despre studenti intr-o inregistrare text formata din 3 campuri separate de caracterul <,>, primul camp fiind ID-ul studentului')
    for linie in range(n):
        student = input('Student' + str(linie + 1) + ': ').split(',')
        id = int(student[0])
        nume_stud = student[1].strip()
        note_stud = [int(i) for i in student[2].split()]
        tabStud[id] = nume_stud
        tabNote[id] = note_stud
    return tabStud, tabNote


def afisare_stud(D):
    print('ID \t Nume student')
    for k in D:
        print(k, D[k], sep='\t')


def afisare_db(DS, DN):
    print('ID \t Nume student \t Note student')
    for k in DS:
        print(k, DS[k], str(DN.get(k)), sep='\t')


def cautare_stud(NumeS, DS, DN, sir):
    for k, val in DS.items():
        if val == NumeS:
            print(sir)
            print(k, DS[k], str(DN.get(k)), sep='\t')
        print('student gasit in db')


def stud_prom(DS, DN):
    for k, val in DS.items():
        note = DN.get(k)
        media = sum(note) / len(note)
        if media >= 5:
            print(k, DS[k], '\t%.2f' % media)


if __name__ == '__main__':
    while (1):
        match optiune():
            case 1:
                tabStud, tabNote = incarcare_date()
            case 2:
                afisare_stud(tabStud)
            case 3:
                afisare_stud(tabNote)
            case 4:
                afisare_db(tabStud, tabNote)
            case 5:
                cautare_stud(input("cautare nume stud:"), tabStud, tabNote, sir='ID \t Nume student \t Note')
            case 6:
                print('Studenti promovati: \n ID \t Nume \t medie')
                stud_prom(tabStud, tabNote)
            case 8:
                break
