/*
 * horner.cxx
 * 
 * W(x) = 2x^3 + 2x^2 + 5x + 4
 * W(x) = x (2x^2 + 3x + 5) + 4
 * W(x) = x (x (2x + 3) + 5) + 4 
 * 
 */
#include <iostream>
using namespace std;

float horner_ir(int stopien, float tbwsp[], float x) {
    
    float wynik = tbwsp[0];
    for (int i = 1; i < stopien + 1; i++){
        wynik = wynik * x + tbwsp[i];
    }
    return wynik;
    }

void drukujw(int stopien, float tbwsp[]) {
    //2x^3 + 3x^2 + 5x + 4;
    int i = 0;
    for (int i = 0; i < stopien ; i++) {
        cout << tbwsp[i] << "x^" << stopien - i << " + ";
        }
        cout << tbwsp[i];
    }

int main(int argc, char **argv)
{   
    
    float x = 0;
    
    int stopien = 0;
    cout << "Podaj stopień wielomianu: ";
    cin >> stopien;
    float *tbwsp; //wskaźnik
    tbwsp = new float [stopien+1];
    for (int i=0; i <= stopien; i++) {
        cout << "Podaj współczynnik przy potędze " << stopien-i << ": ";
        cin >> tbwsp[i];
        }
    

    cout << "Podaj argument: ";
    cin >> x;
    
    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    cout << "\ndla x = " << x << " wynosi: ";
    cout << horner_ir(stopien,tbwsp, x);
    cout << endl;
    


	return 0;
}

