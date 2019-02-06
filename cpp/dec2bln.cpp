#include <iostream>

using namespace std;
void dec2any(int liczba, int podstawa, int tab[]) {
    int i = 0
    do {
        tab[i] = liczba % podstawa;
        liczba = liczba / podstawa;
        i++;
    } while (liczba != 0);
    return i-1;
}
    
void bin2dec(int tab[]){
    ;
    }

    return 0;
}

