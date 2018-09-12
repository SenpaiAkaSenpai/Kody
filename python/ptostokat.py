#!/usr/bin/env python
# -*- coding: utf-8 -*-

def o(a, b):
    return a + b
    
def p(a, b):
    return a * b

def main(args):
    a = int(input("Podaj długość pierwszego boku: " ))
    print(a)
    b = int(input("Podaj długość drugiego boku: " ))
    print(b) 
    
    print ("Pole trójkąta wynosi ", o(a, b), ", a jego obwód to ", p(a, b), ".", sep = "")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
