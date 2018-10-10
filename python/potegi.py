#!/usr/bin/env python
# -*- coding: utf-8 -*-


def potega(a, b):
        
    wynik = 1
    
    for i in range(b):
        wynik = wynik * a
    return wynik
            
    print(wynik)


def main(args):
    
    a = int(input("Podaj podstawę: "))
    b = int(input("Podaj wykładnik potęgi: "))
    
    if b == 0:
        print("Każda wartość poniesiona do potęgi zerowej zwraca wartość 1")
    elif a == 0:
        print("Zero podniesione do każdej potęgi dalej zwraca 0")
    else:
        print("{} do potęgi {} wynosi {}".format(a, b, potega(a, b)))
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
