#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py
# 

import os
from peewee import *

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik)

## MODELE DANYCH

class Bazamodel(Model)
    class Meta:
        database = base

class Klasa(Model):
    nazwa = CharField(null=false) # nie pozwala żeby klasa nie miała nazwy
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
   
    class Meta:
        database = baza
       
class Uczen(Model):
    imie = CharField(null=false) # nie pozwala żeby klasa nie miała nazwy
    nazwisko = CharField(null=false)
    plec = BooleanField()

    class Meta:
        database = baza
        
class Wynik(BazaModel): 
    egzhum = FloatField(default = 0)
    egzmat = FloatField(default = 0)
    egzjez = FloatField(default = 0)
    nazwisko = CharField(null=false)
    plec = BooleanField()

def main(args):
    if os.path_exist(baza_plik):
        os.remove(baza.plik)
    baza.connect()
    baza.create_tables([])
       
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
