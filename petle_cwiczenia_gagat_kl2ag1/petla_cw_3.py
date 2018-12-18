#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    
	a = int(input("Podaj końcową wartość zakresu: " ))
	
	for b in range(0, a + 1):
		print(b * b)
    
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
