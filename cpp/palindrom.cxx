#include <iostream>
using namespace std;

int zlicz(char tb[]) {
    int i = 0;
    while(tb[i] != '\0') i++;
    return i;
    }
    
bool palindrom(char tb[],int i){
        int pol = i/2;
        int czypal = 0;
        for (int j = 0; j >= pol; j++){
            if (tb[i] == tb[i - 1 - j]){
                bool czypal = true;
                
                }
            else {
                bool czypal = false;
                break;
                }
            };
    
    
};


int main(int argc, char **argv)
{
    int liczba = 50;
    char ilosc[liczba];
    cout << "tak" << endl;
    cin.getline(ilosc, liczba);
    palindrom(char tb[], int i);
    
    
	return 0;
}

