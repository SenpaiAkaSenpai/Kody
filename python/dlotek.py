#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    ileliczb = int(input("Podaj ilość typowanych liczb: "))
    maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
    print("Wytypuj {} z {} liczb".format(ileliczb, maksliczba))

    liczby = []
    i = 0
    # for i in range(ileliczb):
    while i < ileliczb:
        liczba = random.randint(1, maksliczba)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i += 1
    print(liczby)

    typy = set()
    i = 0
    while i < ileliczb:
        typ = input("Podaj liczbę {} ".format(i + 1))
        if typ not in typy:
            typy.add(typ)
            i += 1
    print(typy)


    # print("Wylosowano:", liczba)
    # for i in range(3):
    #     odp = input("Podaj liczbę od 1 do 10: ")
    #     print("Wybrałeś liczbę ", odp)

    #     if liczba == int(odp):
    #         print("Zgadłeś!")
    #         break
    #     else:
    #         print("Spróbuj jeszcze raz")
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
