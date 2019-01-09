#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int a = 0;
    while (a <= 0 || a >= 100){
        cout << "Podaj liczbę do sprawdzenia: ";
        cin >> a; 
        }
        
        int i = 2;
        
        if (a == 1) {
            cout << "a jest liczbą parzystą";
            }
        else {
            
            } 
            
            }




/* Podstawowy błąd obu algorytmów polega na tym, że nie są one optymalne.
 * można spokojnie obyć się bez pętli, wystarczy tylko użyć operacji
 * dzielenia modulo przez 2 
 * 
 *                          ( if a % 2 == 0 {
 *                                  cout << "liczba jest parzysta"
 *                            }
 *                            else {
 *                                  cout << "liczba jest nieparzysta"
 *                            } )                                        */
