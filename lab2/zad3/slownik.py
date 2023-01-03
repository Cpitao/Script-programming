# print('Ładowanie modułu "{0}"'.format(__name__))
############################################

def wypisz():
    for k, v in slownik.items():
        print(f"{k}:{v};", end=' ')

def zapisz(inp: str):
    for s in inp.split():
        try:
            slownik[int(s)] = slownik.get(int(s), 0) + 1
        except ValueError:
            print("Encountered NaN, exitting...")
            exit(1)

############################################
# print('Załadowano moduł "{0}"'.format(__name__))

slownik = dict()
