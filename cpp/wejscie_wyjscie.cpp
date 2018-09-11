#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int a, b;
    a = b = 0;
	cout << "Podaj liczbę:" << endl;
    cin >> a;
    cout << a << endl;
    cout << "Podaj drugą liczbę" << endl;
    cin >> b;
    cout << b;
    
    cout << endl << "Wynik: " << (a*b+a+b)/2;
    
	return 0;
}

