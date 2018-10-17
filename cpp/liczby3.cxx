#include <iostream>
#include <iomanip>
using namespace std;

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
    
    cout <<  "Liczb trzycyfrowych:  "  << liczby3() << endl;
    
	return 0;
}

