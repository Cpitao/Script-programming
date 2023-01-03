from dealer import Dealer
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Expected filename argument")
    
    lines = open(argv[1], "r").readlines()
    dealer = Dealer()

    for l in lines:
        dealer.parseFileLine(l)

    while True:
        try:
            dealer.parseInputLine(input('> '))
        except EOFError:
            dealer.end_print()
            break
