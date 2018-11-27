#! /usr/bin/env python
# -*- coding: utf-8 -*-

import turtle

def rysuj(bok, kat, przyrost, warunek):
    turtle.forward(bok)
    turtle.right(kat)
    if kat < warunek:
        rysuj(bok, kat+przyrost, przyrost, warunek)

        
    return 0

def main(args):
    turtle.setup(800, 600)
    turtle.color('blue', 'lime')
    turtle.begin_fill()
    turtle.speed(10)
    
    rysuj(bok=50, kat=1, przyrost=1, warunek=360)
    
    turtle.end_fill()
    turtle.done()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
