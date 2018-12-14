#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  uczniowie_orm.py

import os.path
import csv
from modele import *

def dane_z_pliku(nazwa_pliku, separator=';'):
    
    dane = []  # pusta lista na dane
    
    if not os.path.isfile(nazwa_pliku):
        print("Plik {} nie istnieje.".format(nazwa_pliku))
        return dane
        
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter=separator)
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # oczyszczamy dane
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane
    
def dodaj_dane(dane):
    
    for model, plik in dane.items():
        pola = [pole for pole in model._meta.fields]
        pola.pop(0)  # usunięcie klucza głównego
        print(pola)
        wpisy = dane_z_pliku(plik + '.csv')
        model.insert_many(wpisy, fields=pola).execute()
        print(wpisy)
# model.insert_many(wpisy, fields=('nazwa', 'rok_naboru' etc...))

def main(args):
    
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()  # połączenie z bazą
    baza.create_tables([Kategoria, Pytanie, Odpowiedz])
    dane = {
        # to na górze to słownik
        # klucz: wartość,
        Kategoria: 'kategorie',
        Pytanie: 'pytania',
        Odpowiedz: 'odpowiedzi',
    }
    dodaj_dane(dane)
    baza.close()
    
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
