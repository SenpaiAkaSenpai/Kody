#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    
