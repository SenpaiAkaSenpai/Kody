#include <iostream>

using namespace std;

int suma(int a, int b) {
    return a + b;
    }

int roznica(int a, int b) {
    return a - b;
    }

int iloczyn(int a, int b) {
    return a * b;
    }

int iloraz(int a, int b) {
    return a / b;
    }

int main(int argc, char **argv)
{
    int a, b;
    a = b = 0;
	cout << "Podaj liczbę:" << endl;
    cin >> a;
    cout << a << endl;
    cout << "Podaj drugą liczbę" << endl;
    cin >> b;
    cout << b << endl;
    
    cout <<"Suma wyników: " << suma(a, b) << endl;
    
	return 0;
}

