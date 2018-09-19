#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    
    a = int(input("Zakres od: " ))
    b = int(input("Zakres do: " ))
    
    if a > 1000000 or b > 1000000 * a:
        print("nie zesraj sie")
    elif a <= b:
        for liczba in range(a, b + 1):
            if liczba % 2 == 0:
                
                print(liczba)
    else:
         print("Ty dzbanie zidiociały, wartość początkowa musi być mniejsza od wartości wyjścia, idź usuń system32 ")
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
