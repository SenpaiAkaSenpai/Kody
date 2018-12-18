5#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    a = 0
    b = 0
    while a <= 75:
        b = int(input("Podaj liczbę: "))
        a = b + a
    print("Końcowa licza:", a)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
