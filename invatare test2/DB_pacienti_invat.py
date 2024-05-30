def input_pacienti():
    db=[]
    n=int(input('introduceti numarul de pacienti: '))
    for i in range(n):
        pacient={'ID':input(f'introduceti id pacient {i+1}'),
                 'Nume/Prenume':input(f'Introduceti numele si prenumele pacientului {i+1}')}
        db.append(pacient)
    return db
def afisare_date(db):
    for pacient in db:
        print(f'{pacient['ID']} \t {pacient['Nume/Prenume']}')
def meniu():
    db=[]
    while True:
        text_meniu=' 1. Introducere date \n 2. Afisare date \n 3. Afisare pacienti hipertensiune \n 4. Transfer date in fisier \n 4. Transfer date in fisier'
        print(text_meniu)
        optiune=input('introduceti optiunea dorita: ')
        if optiune=='1':
            db=input_pacienti()
        elif optiune=='2':
            afisare_date(db)
        elif optiune=='9':
            break
        else:
            print('Optiunea introdusa este gresiita')



if __name__ == '__main__':
    meniu()