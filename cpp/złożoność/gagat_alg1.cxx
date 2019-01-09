#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int a = 0;
    while (a == 0 || a >= 100) {
        cout << "Podaj liczbę do sprawdzenia: ";
        cin >> a; 
        }
        
        int i = 2;
            while (a =! i) {
                    i = i + 2;
                if (i == 100) {
                    cout << "a nie jest liczbą parzystą";
                    
                    return 0;
                }
            else {
               
                    
                    return 0;
                    }
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
 *                            } )                                        
 * 
 * Kolejny błąd tego algorytmu polega na tym, że dla wartości a = 1, występuje pętla nieskończona */
