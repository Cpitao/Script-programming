from sys import argv
from math import sqrt


def isPrime(x):
    try:
        x = int(x)
    except ValueError:
        return False
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


if __name__ == "__main__":
    for x in argv:
        if isPrime(x):
            print(x)
