def echivalent(sir1, sir2):
    sir_maj = ""
    for upper in sir2:
        if upper.isupper():
            sir_maj += upper
    return sir_maj, sir_maj == sir1

def afisare_meniu():
    while True:
        print("Meniu principal")
        print("[1]. Citire sirurile: ")
        print("[2]. Afisarea sirului echivalent ")
        print("[9]. Exit")
        print("--------------------")
        optiune = input("Introduceti optiunea dorita: ")
        print("--------------------")

        if optiune == "1":
            sir1 = input("Introduce primul sir de caractere: ")
            sir2 = input("Introduce al doilea sir de caractere: ")
        elif optiune == "2":
            sir_maj, echivalenta = echivalent(sir1, sir2)
            print("Sirul de caractere majuscule echivalent este:", sir_maj)
            if echivalenta:
                print("Sirul sir1 este echivalent cu sir2")
            else:
                print("Sirul sir1 nu este echivalent cu sir2")
        elif optiune == "9":
            break


if __name__ == '__main__':
    afisare_meniu()
