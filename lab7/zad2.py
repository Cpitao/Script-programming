import sys; a=list(map(len, sys.stdin.read().split())); print(dict(set((x, a.count(x)) for x in a)))