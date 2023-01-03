# print('Ładowanie modułu "{0}"'.format(__name__))
############################################

def wypisz():
    for v in lista:
        print(f"{v[0]}:{v[1]};", end=' ')

def zapisz(inp):
    for s in inp.split():
        try:
            int(s)
        except ValueError:
            print("NaN encountered. Exitting...")
            exit(1)
        for i, v in enumerate(lista):
            if v[0] == int(s):
                lista[i][1] += 1
                break
        else:
            lista.append([int(s), 1])

############################################
# print('Załadowano moduł "{0}"'.format(__name__))

lista = []