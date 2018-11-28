/*
 * potega.cpp
 */

#include <iostream>
using namespace std;

int fibonacci_re(int n)
{
    if (n == 0) return 0;
    if (n == 1) return 1;
    return (fibonacci_re(n - 2) + fibonacci_re(n - 1));
}

int main(int argc, char **argv)
{
    int n;
    cout << "Podaj liczbę: "; cin >> n;
    cout << "Wynik: " << fibonacci_re(n) << " ";
    for (int i = 0; i <= n; i++){
        cout << fibonacci_re(i) << " ";
        if (i < 2) continue;
        else  {
            cout << (float)fibonacci_re(i) / (float)fibonacci_re(i-1) << endl;
    }
}
    return 0;
}

