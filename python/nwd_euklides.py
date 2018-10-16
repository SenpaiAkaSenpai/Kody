#!/usr/bin/env python
# -*- coding: utf-8 -*-



def nwd(a, b):
    
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
        
def main(args):
    a = int(input("Pierwsza liczba: "))
    b = int(input("Druga liczba: "))
    print(nwd(a, b))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
