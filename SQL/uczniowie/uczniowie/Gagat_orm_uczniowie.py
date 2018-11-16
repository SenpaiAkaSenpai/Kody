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
       
class Uczen(Model):
    imie = CharField(null=false) # nie pozwala żeby klasa nie miała nazwy
    nazwisko = CharField(null=false) 
    plec = BooleanField()
    egzhum = FloatField(default = 0)
    egzmat = FloatField(default = 0)
    egzjez = FloatField(default = 0)
    
    Uczen = ForeignKeyField(Klasa, related_name= 'uczniowie')
    
    class Meta:
        database = baza
        
class Klasa(BazaModel):
    nazwa = CharField(null=false) # nie pozwala żeby klasa nie miała nazwy
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
   
    class Meta:
        database = baza

class Przedmiot(BazaModel): 
   
    przedmiot = CharField(null=false) 
    imie_naucz = CharField(null=false) 
    nazwisko_naucz = CharField(null=false)
    plec_naucz = BooleanField()
    
    class Meta:
        database = baza
        
class Ocena(BazaModel): 
   
    data_d = DataField() 
    ocena = DecimalField(null=false) 
    
    Uczen = ForeignKeyField(Uczen, related_name= '')
    Uczen = ForeignKeyField(Przedmiot, related_name= '')
    
    class Meta:
        database = baza

def main(args):
    if os.path.exist(baza_plik):
        os.remove(baza.plik)
    baza.connect()
    baza.create_tables([])
       
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
