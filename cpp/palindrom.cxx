#include <iostream>
using namespace std;

int zlicz(char tb[]) {
    int i = 0;
    while(tb[i] != '\0') i++;
    return i;
    }
    
bool palindrom(char tb[],int nom){
        int pol = (nom - 1) /2;
        int i = 0;
        bool czypal = 1;
        for (int j = nom - 1; j > pol; j--){
            if (tb[j] == tb[i]){
                i++;
                
            }else {
                czypal = false;
                break;
                }
            }
        return czypal;
};


int main(int argc, char **argv)
{
    int liczba = 50;
    char ilosc[liczba];
    cout << "tak" << endl;
    cin.getline(ilosc, liczba);
    if (palindrom(ilosc, zlicz(ilosc))) {
        cout << "tak";
        }
    else{
        cout << "nie tak";
        }
    
    
	return 0;
}

