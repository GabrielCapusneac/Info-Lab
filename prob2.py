import math as lib


def minim(a, b, c):
    if a < b and a < c:
        print(f'minimul este {a}')
    elif b < a and b < c:
        print(f'minimul este {b}')
    else:
        print(f'minimul este {c}')


def maxim(a, b, c):
    if a > b and a > c:
        print(f'maximul este {a}')
    elif b > a and b > c:
        print(f'maximul este {b}')
    else:
        print(f'maximul este {c}')


def citire():
    a = int(input("introduceti valoarea lui a: "))
    b = int(input("introduceti valoarea lui b: "))
    c = int(input("introduceti valoarea lui c: "))
    return a, b, c


if __name__ == '__main__':
    a, b, c = citire()
    print(minim(a, b, c))
    print(maxim(a, b, c))
