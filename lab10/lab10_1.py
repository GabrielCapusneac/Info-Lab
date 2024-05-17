# def meniu():
#     print("1.")
#     print("2.")
#     print("3.")
#     print("4.")
#     print('____________')
#     opt = input("Introduceti optiunea dorita: ")
#     while True:
#         if opt == '1':
#             pass
#         elif opt == '2':
#             pass
#         elif opt == '10':
#             break

# LINE BY LINE
# file=open('Note_studenti.txt','r')
# while True:
#     line=file.readline()
#     if len(line)==0:
#         break
#     print(line,end='')
# file.close()

# LISTA
# file = open('Note_studenti.txt', 'r')
# lista = list(file)
# print(lista)
# print(file)
# file.close()

# LINE_clear_LINE
# file = open('Note_studenti.txt', 'r')
# lista = list(file)
# file.close()
# for i in range(len(lista)):
#     print(i+1,':\t',lista[i])

file = open('Note_studenti.txt', 'r')
lista = list(file)
file.close()

for i, line in enumerate(lista):
    print(i + 1, ':\t', line, end='')
print()
new_list = list(enumerate(lista, 1))
print(new_list)
