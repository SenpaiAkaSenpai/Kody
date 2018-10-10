#!/usr/bin/env python
# -*- coding: utf-8 -*-

def liczby2():
    
    ile2 = 0
    
    for i in range(10, 99):
        if i % 11 != 0:
            print(i)
            ile2 += 1
    print()
    print(ile2)
    
def liczby3():
    
    ile3 = 0

    for j in range(100, 999):
        if j % 111 != 0 and j % 101 != 0:
            print(j)
            ile3 += 1
    print()
    print(ile3)

def main(args):
    liczby2()
    liczby3()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
