#include <iostream>

using namespace std;

void loss(int uwu[], int n){
    srandom(time(NULL)); //inicjacja generatora liczb pseudolosowych
    for(int i = 0; i < n; i++){
        uwu[i] = rand() % 101;
    
    };
}

void killme(int uwu[], int n){
    for (int i = 0; i < n; i++) {
        cout << uwu[i] << " "; 

    }
}

void sortowanie(int i, int n){
    cout << "Podaj górny zakres: ";
    cin >> n;
    int k = 0;
        for (int i = 0; i < n ; i++) {
            for (int j = 1; j < n; j++){
                
                };
            };
        };


int main(int argc, char **argv){
	int owo = n;
    int uwu[owo];
    cout << "Wylosowana tabela:"<< endl;
    loss(uwu, owo);
    killme(uwu, owo);
    sortowanko(uwu, owo);
    
	return 0;
}



