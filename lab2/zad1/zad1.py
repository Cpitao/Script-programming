#-*-coding: utf-8-*-

# 1)
lancuch1 = """długi napis
o wielu liniach
to łańcuch"""
lancuch2 = """drugi
napis
wielolinijkowy
ąęśćżźó"""

print((lancuch1 + lancuch2) * 3)

lancuch = "dowolny tekst"
print(lancuch[0])
print(lancuch[:2])
print(lancuch[2:])
print(lancuch[-2])
print(lancuch[-3:])
print(lancuch[::2])

# lancuch[0] = 'a' # error - str doesn't support item assignment (immutable)
