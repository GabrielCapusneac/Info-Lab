# sir=str(input("Introduceti sirul dorit: "))
# x=int(input("Introduceti lungimea cuvantului"))
#
# cuv=
# for cuv in sir:
#     if x==len(cuv):
#         print(cuv)

def lun_cv():
    sir = input("Introduceți textul: ")
    x = int(input("Introduceți lungimea cuvantului: "))

    cuvant = ""
    cv_lung = []
    for i in sir:
        if i != " ":
            cuvant += i
        else:
            if len(cuvant) == x:
                cv_lung.append(cuvant)
            cuvant = ""

    if len(cuvant) == x:
        cv_lung.append(cuvant)

    if cv_lung:
        print(f"Cuvintele din text care au {x} caractere sunt:")
        for cuvant in cv_lung:
            print(cuvant)

if __name__ == "__main__":
    lun_cv()
