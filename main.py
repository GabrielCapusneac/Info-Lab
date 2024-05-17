# import math
import math as lib


def ec2(a, b, c):
    delta = b ^ 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + lib.sqrt(delta)) / (2 * a)
        x2 = (-b - lib.sqrt(delta)) / (2 * a)
        return x1, x2
    elif delta == 0:
        return (-b) / (2 * a)
    else:
        x1 = (-b + lib.sqrt(delta) * 1j) / (2 * a)
        x2 = (-b - lib.sqrt(delta) * 1j) / (2 * a)
        return x1, x2


def citire():
    a = int(input("introduceti valoarea lui a: "))
    b = int(input("introduceti valoarea lui b: "))
    c = int(input("introduceti valoarea lui c: "))
    return a, b, c


if __name__ == '__main__':
    a, b, c = citire()
    print(ec2(a, b, c))
