#include <iostream>

using namespace std;

int o(int a, int b) {
    return a + b;
    }
    
int p(int a, int b) {
    return a * b;
    }


int main(int argc, char **argv)
{
    int a, b;
    a = b = 0;
	cout << "Podaj długość pierwszego boku: " << endl;
    cin >> a;
    cout << "Podaj długość drugiego boku: " << endl;
    cin >> b;
    
    cout <<"Pole prostokąta wynosi " << p(a, b) << ", a jego obwód " << o(a, b);
    
	return 0;
}

