#!/usr/bin/env python
# -*- coding: utf-8 -*-

kod = {'A': '.-',  'B': '-...', 'C': '-.-.', 
     'D': '-..', 'E': '.',  'F': '..-.', 
     'G': '--.', 'H': '....', 'I': '..', 
     'J': '.---', 'K': '-.-', 'L': '.-..', 
     'M': '--',  'N': '-.',  'O': '---', 
     'P': '.--.', 'Q': '--.-', 'R': '.-.', 
     'S': '...', 'T': '-',  'U': '..-', 
     'V': '...-', 'W': '.--', 'X': '-..-', 
     'Y': '-.--', 'Z': '--..',
     '0': '-----', '1': '.----', '2': '..---', 
     '3': '...--', '4': '....-', '5': '.....', 
     '6': '-....', '7': '--...', '8': '---..', 
     '9': '----.', ' ': ' '}

def koduj():
    
    wiadomosc = input("Podaj tekst to translacji: ").upper()
    for litera in wiadomosc:
        print(kod[litera], ' ')
        
def dekoduj():
    
    telst = []
    litera = ' '
    while litera > '':
        litera = input('Podaj wiadomość do dekodowania')
        tekst.append(litera
        

def main(args):
    
    koduj()
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
