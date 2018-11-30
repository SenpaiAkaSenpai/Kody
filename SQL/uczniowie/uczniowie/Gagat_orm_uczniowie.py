#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py

import os
from modele_orm import *
from baza import dane_z_pliku

def dodaj_dane(dane):
    
    for model, plik in dane.items():
        pola = [pole for pole in model._meta.fields]
        pola.pop(0)
        
        wpisy = dane_z_pliku(plik + '.txt')
        model.insert_many(wpisy, fields=pola).execute()
        
       #model.insert_many(wpisy, fields=(''))

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()  
    baza.create_tables([Klasa, Uczen, Przedmiot, Ocena])
    
    dane = {
        Klasa: 'klasy',
        Uczen: 'uczniowie',
        Przedmiot: 'przedmioty',
        Ocena: 'oceny',
    }
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
