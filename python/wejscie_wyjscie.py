#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    a = int(input("Podaj liczbę: " ))
    print(a,)
    b = int(input("Podaj liczbę: " ))
    print(b) 
    
    print("Suma: ", a+b)
    print("Różnica: ", a-b)
    print("Iloczyn: ", a*b)
    print("Iloraz: ", a/b)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
