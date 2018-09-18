#!/usr/bin/env python
# -*- coding: utf-8 -*-


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

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
