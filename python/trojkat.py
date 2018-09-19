#!/usr/bin/env python
# -*- coding: utf-8 -*-

def trojkat(a, b, c):
    
    wynik = False
    
    if a + b > c and a + c > b and b + c > a:
        wynik = True 
            
    return wynik
    
def main(args):
    assert(trojkat(2, 6, 7) == True)
    assert(trojkat(3, 5, 9) == False)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
