import lista
import slownik
from sys import argv


USAGE = "USAGE: python zad3.1.py [--lista|--slownik] [args]+"

if __name__ == "__main__":
    if len(argv) < 3:
        print(USAGE)
        exit(0)
    
    if argv[1] == "--lista":
        lista.zapisz(" ".join(argv[2:]))
        lista.wypisz()
    elif argv[1] == "--slownik":
        slownik.zapisz(" ".join(argv[2:]))
        slownik.wypisz()
    else:
        print(USAGE)
