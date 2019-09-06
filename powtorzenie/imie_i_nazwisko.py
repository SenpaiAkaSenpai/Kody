#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    a = input("Podaj imię: " )
    b = input("Podaj nazwisko: " )

    print("Okej, wic masz na imię:", a, b)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
