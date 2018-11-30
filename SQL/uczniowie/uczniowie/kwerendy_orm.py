#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from modele_orm import *
from baza import dane_z_pliku

def kw01()
    obj = Uczen.select().where(Uczen.imie.startswith('G'))
    for row in obj:
        print(row.nazwisko, row.imie)

def main(args):
    baza connect()
    
    kw01()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
