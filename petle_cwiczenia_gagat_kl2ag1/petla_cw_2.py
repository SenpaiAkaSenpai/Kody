#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    
    a = int(input("Podaj liczbę: " )) 
    b = int(input("Podaj liczbę: " ))
    
    if a > 1000000 or b > 1000000 * a:
        print("podałeś za wysokie parametry, drogi użytkowniku")
    if a <= b:
        for liczba in range(a, b + 1):
                print(liczba, end=" ")
    else:
         print("Ty bambaryło przebrzydła, wartość początkowa musi być mniejsza od wartości wyjścia, idź usuń system32 ")
         
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
