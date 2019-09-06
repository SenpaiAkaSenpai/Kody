#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def main(args):
    
    liczby =[]
    for i in range(1):
        liczby.append(random.sample(range(0, 31), 5))
    print("A oto i pięć przecudownych oraz unikalnych liczb losowych (w zakresie od 1 do 30) ", liczby)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

