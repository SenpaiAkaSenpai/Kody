#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from peewee import *

baza_plik = 'quiz.db'
baza = SqliteDatabase(baza_plik)  # instancja bazy

### MODELE DANYCH
class BazaModel(Model):
    class Meta:
        database = baza

class Kategoria(BazaModel):
    kategoria = CharField(null=False)
    
class Pytanie(BazaModel):
    pytanie = CharField(null=False)
    kategoria = ForeignKeyField(Kategoria, related_name='pytania')
    
class Odpowiedz(BazaModel):
    odpowiedz = CharField(null=False)
    pytanie = ForeignKeyField(Pytanie, related_name='odpowiedzi')
    odpok = IntegerField(default=0)
    

    
def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()  
    baza.create_tables([Kategoria, Pytanie, Odpowiedz])

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
