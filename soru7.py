import math


def f(x):
    return x**3


def gercekturev(x):
    return 3*x**2


def ilerifark(x, h):
    return (f(x+h) - f(x)) / h

def gerifark(x, h):
    return (f(x) - f(x-h)) / h

def merkezifark(x, h):
    return (f(x+h) - f(x-h)) / (2*h)


x = 1
h_list = [0.2, 0.1]
gercek = gercekturev(x)

for h in h_list:
    ileri = ilerifark(x, h)
    geri = gerifark(x, h)
    merkez = merkezifark(x, h)

    print(f"h = {h}:")
    print(f"  İleri Fark: {ileri:.6f}, Hata: {abs(ileri-gercek):.6f}")
    print(f"  Geri Fark: {geri:.6f}, Hata: {abs(geri-gercek):.6f}")
    print(f"  Merkezi Fark: {merkez:.6f}, Hata: {abs(merkez-gercek):.6f}")

