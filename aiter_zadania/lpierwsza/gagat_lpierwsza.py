#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    n = int(input("Podaj liczbę: "))
    i = 2
        
    if i * i < n:
        print("Liczba pierwsza")
        return 0
    else:
        while not i * i < n:
            if n % i == 0:
                print("Liczba złożona")
                return 0
            else:
                i = i + 1

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

