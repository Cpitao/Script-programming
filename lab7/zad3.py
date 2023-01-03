import sys
print(len(list(filter(lambda x: int(x) % 2 == 0, filter(lambda x: x.isdigit(), " ".join([open(f, "r").read() for f in sys.argv[1:]]).split())))))
# python zad3.py test3.1.txt test3.2.txt
# should print 6