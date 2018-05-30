#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3


def main(args):
    con = sqlite3.connect('filmy.db')
    cur = con.cursor()

    with open('filmy.sql', 'r') as plik:
        cur.executescript(plik.read())

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
