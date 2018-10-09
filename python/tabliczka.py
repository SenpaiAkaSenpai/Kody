#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    
    a = int(input("Podaj górny zakres: "))
    print()
    
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            print("{:>3} ".format(i*j), end='')
        print()
    
    return 0
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
