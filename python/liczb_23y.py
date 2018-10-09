#!/usr/bin/env python
# -*- coding: utf-8 -*-

def liczby2(args):
    
    for i in range(10, 99):
        if i % 11 != 0:
            print(i)

    
def liczby3(args):
    
    for j in range(100, 999):
        if j % 111 != 0:
            print(j)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
