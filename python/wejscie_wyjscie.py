#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    a = input("Podaj liczbę: " )
    print(math.pow(a, 1.0/123)) 
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
