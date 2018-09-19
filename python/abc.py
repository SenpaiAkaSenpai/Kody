#!/usr/bin/env python
# -*- coding: utf-8 -*-


def maks(a, b, c):
    maks = a
    if b > maks:
        maks = b
    if c > maks:
            maks = c
    return maks

def main(args):
    a = int(input("Podaj liczbę a: " ))
    print(a)
    b = int(input("Podaj liczbę b: " ))
    print(b) 
    c = int(input("Podaj liczbę c: " ))
    print(c) 
    
    if a > b:
        if a > c:
            print("Największa liczba to", a)
    elif b > c:
        print("Największa liczba to", b)
    else:
        print("Największa liczba to", c)


    assert(maks(3, 2, 1) == 3)
    assert(maks(2, 3, 1) == 3)
    assert(maks(1, 2, 3) == 3)
    assert(maks(1, 1, 3) == 3)
    assert(maks(3, 1, 1) == 3)
    assert(maks(1, 3, 1) == 3)
    assert(maks(1, 3, 3) == 3)
    assert(maks(3, 3, 1) == 3)
    assert(maks(3, 3, 3) == 3)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
