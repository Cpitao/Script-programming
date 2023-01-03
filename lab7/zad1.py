from inspect import signature

def argumenty(args):
    def inner(f):
        def inner2(*ua):
            user_args = list(ua)[1:]
            f_args = len(list(signature(f).parameters))
            last_taken_index = f_args - len(user_args)
            if last_taken_index > len(args):
                raise TypeError(f"{f.__name__}() takes exactly {f_args} arguments ({len(user_args) + len(args)} given)")
            passed_args = user_args + args[:max(min(last_taken_index, len(args)), 0)]
            f(*passed_args)
            if last_taken_index < len(args):
                return args[last_taken_index]
            else:
                return None
        return inner2
    return inner


class Operacje:
    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]

    @argumenty(argumentySuma)
    def suma(a,b,c):
        print("%d+%d+%d=%d" % (a,b,c,a+b+c))

    @argumenty(argumentyRoznica)
    def roznica(x,y):
        print("%d-%d=%d" % (x,y,x-y))

    def new_sum(a,b,c):
        print("%d+%d+%d=%d" % (a,b,c,a+b+c))

    def __setitem__(self, key, value):
        if key == 'suma':
            Operacje.argumentySuma = value
            Operacje.suma = argumenty(Operacje.argumentySuma)(Operacje.new_sum)
        elif key == 'roznica':
            Operacje.argumentyRoznica = value
            @argumenty(Operacje.argumentyRoznica)
            def sub(x,y):
                print("%d-%d=%d" % (x,y,x-y))
            Operacje.roznica = sub



# op=Operacje()
# op.suma(1,2,3) #Wypisze: 1+2+3=6
# op.suma(1,2) #Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
# op.suma(1) #Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
# op.suma() #TypeError: suma() takes exactly 3 arguments (2 given)
# op.roznica(2,1) #Wypisze: 2-1=1
# op.roznica(2) #Wypisze: 2-4=-2
# wynik=op.roznica() #Wypisze: 4-5=-1
# print(wynik) #Wypisze: 6

# #Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
# op['suma']=[1,2]
# #oznacza, że   argumentySuma=[1,2]

# #Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
# op['roznica']=[1,2,3]
# #oznacza, że   argumentyRoznica=[1,2,3]