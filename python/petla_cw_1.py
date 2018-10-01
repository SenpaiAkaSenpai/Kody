#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main(args):
    a = 0
    b = 0
    c = 0
    while c < 75:
         a = int(input("Podaj liczbę:"))
         c = b + a
    print("D o ś ć, skończ już z tym", c)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
2
