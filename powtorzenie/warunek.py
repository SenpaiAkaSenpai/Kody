#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    
    a = int(input("Liczba pierwsza: " ))
    b = int(input("Podaj drugą liczbę poproszę kochanie: " ))
    c = int(input("Teraz trzecia i ostatnia, nie poproszę o nic więcej: " ))
    print("Podane liczby to", a, b, c) 
    
    if a > b and a > c:
        print("No wygląda na to, że największa wartość to", a)
    else:
        if b > c:
            print("No czyli największa wartość to", b)
        else:
            print("Wychodzi na to, że największe to jednak", c, "jest")
    
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
