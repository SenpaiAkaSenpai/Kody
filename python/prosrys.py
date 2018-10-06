#!/usr/bin/env python
# -*- coding: utf-8 -*-

def prostokat(jednostka, a, b):
    jednostka = "*"
    jednostka = input("Podaj jednostkę ")
    a = int(input("Podaj wysokość: "))
    b = int(input("Podaj szerokość: "))
    print("Pole: ", a * b)
    print("Używana jednostka: ", jednostka)
    
    for i in range(a):
        for j in range(b):
            if i > 0 and j > 0 and i < a - 1 and j < b - 1:
                print(" ", end=" ")
            else:
                print(jednostka, end=" ")
        print()
    
    return 0
    
def trojkat(znak, c)
    znak = "*"
    znak = input("Podaj jednostkę ")
    c = int(input("Podaj szerokość podstawy: "))
    
    for i in range(a):
        print(" "*(c - i) + znak *(i*2-1)
    
    return 0

def main(args)

    prostokat('&', 10, 10)
    trojkat("$", 10)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
