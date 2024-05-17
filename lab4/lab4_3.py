
def afisare_meniu():
    while True:
        print("Meniu principal")
        print("[1]. Citire sirurile: ")
        print("[2]. Gasire subsir in sir ")
        print("[9]. Exit")
        print("--------------------")
        optiune = input("Introduceti optiunea dorita: ")
        print("--------------------")

        if optiune == "1":
            sir = input("Introduce primul sir de caractere: ")
            subsir = input("Introduce subsirul de caractere: ")
        elif optiune == "2":
            

        elif optiune == "9":
            break


if __name__ == '__main__':
    afisare_meniu()
