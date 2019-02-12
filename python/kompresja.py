#!/usr/bin/env python
# -*- coding: utf-8 -*-

def wspolczynnik(Vk, Vnk):
    Rc = int(Vk) / int(Vkn) * 100
    R2c = (1 - int(Vk) / int(Vkn)) * 100   
    print('O ile zmniejszyły się dane: ', Rc)
    print('Zaoszczędzone miejsce: ', R2c)
    
def main(args):
    for i in range(2):
        Vk = input('Rozmiar danych skompresowanych (B): ')
        Vkn = input('Rozmiar danych nieskompresowanych (B): ')
        
        wspolczynnik(Vk, Vnk)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
