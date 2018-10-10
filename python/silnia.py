#!/usr/bin/env python
# -*- coding: utf-8 -*-


def silnia(a):
        
    wynik = 1
    
    for i in range(1, a + 1):
        wynik = wynik * i
        print(wynik)
    return wynik


def main(args):
    
    #a = int(input("Podaj liczbę z której mam wyliczyć silnię: "))
    
    #print("Silnia z {} wynosi {}".format(a, silnia(a)))

    assert(silnia(0) == 1)
    assert(silnia(1) == 1)
    assert(silnia(2) == 2)
    assert(silnia(4) == 24)
    assert(silnia(5) == 120)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
