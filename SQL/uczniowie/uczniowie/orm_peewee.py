#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py

import os
from peewee import *

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik)  # instancja bazy

### MODELE DANYCH
class BazaModel(Model):
    class Meta:
        database = baza

class Klasa(BazaModel):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = IntegerField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)

class Przedmiot(BazaModel):
    przedmiot = CharField(null=False)
    imie_naucz = CharField(null=False)
    nazwisko_naucz = CharField(null=False)
    plec_naucz = IntegerField()
    
class Ocena(BazaModel):
    datad = DateField()
    uczen = ForeignKeyField(Uczen, related_name='oceny')
    przedmiot = ForeignKeyField(Uczen, related_name='przedmiot')
    ocena = FloatField(default=0)
    
def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()  
    baza.create_tables([Klasa, Uczen, Wynik])
    
    kl1a = Klasa(nazwa= "1A", roknaboru=2009, rokmatury=2012)
    kl1a.save()
    
    u1 = Uczen(imie="Siema", nazwisko="Eniu", plec = False, klasa = kl2a)
    u1.save()
    
    u2 = Uczen(imie="Anna", nazwisko="Gacek", plec = True, klasa = kl1a)
    u2.save()

    u3 = Uczen(imie="Roman", nazwisko="Polek", plec = False, klasa = kl1a)
    u3.save()
    
    uczniowie = Uczen.select()
    for uczen in uczniowie:
        print(uczen.id, uczen.nazwisko, uczen.klasa)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
