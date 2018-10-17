#include <iostream>
using namespace std;

void prostokat(int a, int b, char znak) {
    for (int i = 0; i < a; i++){
        for (int j = 0; j < b; j++){
            if (j == 0 || j == b-1 || i == 0 || i == a-1)
                cout << znak;
            else 
                cout << " ";
            }
        cout << endl;
        }
    }

int main(int argc, char **argv)
{
    char znak;
    int a, b;
    a = b = 0;
    cout << "Podaj boki prostokąta: ";
    cin >> a >> b;
    cout << "\nPodaj znak: ";
    cin >> znak; 
    prostokat(a, b, znak);
    
	return 0;
}

