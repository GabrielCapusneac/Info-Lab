# suma=0
# suma=suma+x%10
# x=x//10
#
#
#
def citire():
    n=int(input("Introduceti numarul n: "))
    return n

def suma_numere_numar(n):
    sum=0
    while n:
        sum=sum+n%10
        n=n//10
    return sum

if __name__ == '__main__':

    n=citire()
    print(suma_numere_numar(n))