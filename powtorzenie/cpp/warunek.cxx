#include <iostream>

using namespace std;

int main(int argc, char **argv)

{
    int a, b, c;
    a = b = c = 0;
	cout << "Dawaj pierwszą liczbę, ino szybko" << endl;
    cin >> a;
    cout << "Teraz druga, albo żegnasz się z życiem" << endl;
    cin >> b;
    cout << "Nie no, żartowałem, ale podałbyś kolego trzecią" << endl;
    cin >> c;

    if (a>b && a>c) {
        cout << "Wszystkie znaki na ziemi i na niebie wskazują na to, że największa z tych liczb to " << a << endl;
        }
    else {
        if (b>c) {
            cout << "Wygląda na to, że nie ma tu żadnej liczby większej niż " << b << endl;
            }
        else {
            cout << "Wszyscy jesteśmy w stanie zgodnie stwierdzić, że największa z cyfr to " << c << endl;
            }
        }
    
	return 0;
}

