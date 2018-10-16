#include <iostream>
#include <iomanip>
using namespace std;

void tabliczka(int a, int b) {
    for (int i = 1; i <= a; i++){
        for (int j = 1; j <= b; j++){
            cout << setw(4) << i * j;
            }
        cout << endl;
        }
    }

int main(int argc, char **argv)
{
	int a, b;
    a = b = 0;
    cout << "Podaj zakres pierwszy: ";
        cin >> a;
    cout << "Podaj zakres drugi: ";
        cin >> b;
    
    tabliczka(a, b);
    
	return 0;
}

