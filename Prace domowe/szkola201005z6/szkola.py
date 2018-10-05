import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(szkola_oceny, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter='\t')
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # oczyszczamy dane
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane

def main(args):
    con = sqlite3.connect('szkola.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open('szkola.sql', 'r') as plik:
        cur.executescript(plik.read())

    # dodawanie danych do bazy
    oceny = dane_z_pliku('szkola_oceny.txt')
    oceny.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO szkola_oceny VALUES(?, ?, ?, ?)', szkola_oceny)

    # przykład zapytania (kwerendy)
    con.commit()
    con.close()
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
