#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py

import sqlite3


def kwerenda1(cur):
    cur.execute("""
        WITH srednie AS(
            SELECT nazwisko, imie, AVG(ocena) AS poile FROM uczniowie 
            INNER JOIN oceny ON uczniowie.id=oceny.id_uczen 
            GROUP BY uczniowie.id
            ) SELECT nazwisko, imie, poile FROM srednie
            WHERE poile >= 4.75
    """)
    
    #SELECT klasa, COUNT(uczniowie.id) AS ile FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa GROUP BY klasa ORDER BY ile DESC
    #        WITH srednie AS( SELECT nazwisko, imie, AVG(ocena) AS poile FROM uczniowie  INNER JOIN oceny ON uczniowie.id=oceny.id_uczen  GROUP BY uczniowie.id) SELECT nazwisko, imie, poile FROM srednie WHERE poile >= 4.75

    wynik = cur.fetchall()
    for row in wynik:
        print(row)
    return 0

def main(args):
    baza_nazwa = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    kwerenda1(cur)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
