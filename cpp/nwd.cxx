#include <iostream>

using namespace std;

int nwd_klas(int a, int b) {
    while a != b: {
        
    }
}

int nwd_opt(int a, int b) {
    int c;
    c = 0:
    while(a > 0){
        c = c + 1;
        a = a%b;
        b = b-a;
    };
    return b;
}

int main(int argc, char **argv) {
	int a, b;
    a = b = 0;
    cout << "Podaj liczbę a: ";
    cin >> a;
    cout << "Podaj liczbę b: ";
    cin >> b;
    cout << eee(a, b);
    cout << rrr(a, b);

	return 0;
}

