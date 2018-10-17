#include <iostream>
#include <iomanip>
using namespace std;

int liczby2(){
    int ile = 0;
    for (int i = 1; i < 10; i++){
        for (int j = 0; j < 10; j++){
            if (i != j){
                cout << i << j << " ";
                ile ++;
            }
        }
        cout << endl;
    }
    cout << endl;
    return ile;
}

int liczby3(){
    int tak = 0;
    for (int a = 1; a < 10; a++){
        for (int b = 0; b < 10; b++){
            for (int c = 0; c < 10; c++){
                if (a != b && a != c && b != c){
                    cout << a << b << c << " ";
                    tak ++;
                }
            }
        }
        cout << endl;
    }
    cout << endl;
    return tak;
}



int main(int argc, char **argv){
    
    int ile = liczby2();
    cout <<  "\nLiczb dwucyfrowych:  " << endl << ile << endl;
    
    int tak = liczby3();
    cout <<  "\nLiczb trzycyfrowych:  "  << endl << tak << endl;
	return 0;
}

