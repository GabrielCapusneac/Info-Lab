# n=int(input("limita: "))
# for i in range(n,0,-1):
#     print(i,end=" ")
#
# n=int(input("limita: "))
# for i in range(0,n,1):
#     print(i,end=" ")

# n=int(input("limita: "))
# for i in range(1,n,2):
#     print(i,end=" ")
#
# produs=1
# n=int(input("limita: "))
# # for i in range(0,n,1):
# #     print(i,end=" ")
# # while i<n:
#     for i in range(0, n, 1):
#         produs=produs*i
#         print(produs,end=" ")


# //3.facorial
# def citire():
#     n = int(input("citire numar n: "))
#     return n
#
# def prodfac(n):
#     fac = 1
#     for i in range(1, n + 1):
#         fac = fac * i
#     return fac
#
#
# if __name__ == '__main__':
#     n = citire()
#     print(prodfac(n))

# //4.suma nr divizibile
def citire():
    n = int(input("numarul n: "))
    x = int(input("numarul x: "))
    return n, x


def suma_div(n, x):
    sum = 0
    for i in range(1, n + 1):
        if i % x == 0:
            sum = sum + i
    return sum


if __name__ == '__main__':
    n, x = citire()
    print(suma_div(n, x))
