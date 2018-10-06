#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    
    a = int(input("Podaj liczbę: " ))

    for liczba in range(0, a + 1):
        print(liczba * liczba)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
