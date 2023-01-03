from sys import argv
import getopt


USAGE = "USAGE: python zad3.1.py [--lista|--slownik] [args]+"
s = 'modul='
if __name__ == "__main__":
    try:
        optlist, args = getopt.getopt(argv[1:], [], s)
    except getopt.GetoptError as err:
        print(USAGE)
        print(err)
        exit(2)
    
    print(optlist, args)

    if optlist[0][1] == "lista":
        import lista
        lista.zapisz(" ".join(args))
        lista.wypisz()
    elif optlist[0][1] == "slownik":
        import slownik
        slownik.zapisz(" ".join(args))
        slownik.wypisz()
    else:
        print(USAGE)
