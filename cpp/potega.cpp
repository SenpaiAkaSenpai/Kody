/*
 * potega.cpp
 */

#include <iostream>

float potega_re(float x, int n)
{
    if (n == 0) return 1;
    return potega_re(x, n-1) * x;
}

int main(int argc, char **argv)
{
    float podstawa;
    int wykładnik;
    cout << "Podstawa: "; cin >> podstawa;
    cout << "Wykładnik: "; cin >> wykladnik;
    cout << "Wynik: " << potega_re(podostawa, wykladnik);
}

int main(int argc, char **argv)
{
	
	return 0;
}

