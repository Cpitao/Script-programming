import sys
from dealer import Dealer
from client import Client
from car import Car


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Required magazine filename")
        exit(-1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    dealer = Dealer()
    for l in lines:
        dealer.parse_file_line(l.strip())

    while True:
        try:
            line = input('Q> ')
        except EOFError:
            print(dealer)
            exit(0)

        dealer.parse_input_line(line)

