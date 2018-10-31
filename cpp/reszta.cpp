#include <iostream>
using namespace std;

void ascii(char tab[]){
    int i = 0;
        while(tab[i] != '\0'){
            cout << (int)tab[i] << " ";
            i++;
    }
}

void zamiana_liter(char tab[]) {
    int i = 0;
    
    while(tab[i] != '\0') {
        cout << int(tab[i] << " ";
        if huhu >= 65 && huhu <= 90 {
            int huhu = (int)tab[i];
            int huhu = huhu + 32;
            };
        if huhu >= 97 && huhu <= 122 {
            int huhu = (int)tab[i];
            int huhu = huhu - 32
        };
        i++;

        };
    };

void licz_znaki(char tab[]){
    int i = 0;
    int biale, inter, licz;
    biale = inter = licz = 0;
    while(tab[i] != '\0') {
        cout << tab[i] << " ";
       // if (tab[i] == ' ' || tab[i] == '\t')
          //  biale++;
      //  else
            //cout << tab[i];
        switch(tab[i]) {
            case ' ': biale++; break;
            case '\t': biale++; break;
            case ',': inter++; break;
            case '.': inter++; break;
            default: licz++; break;
        }
        i++; 
    }
    cout << "\nZnaków białych: " << biale << endl;    
    cout << "\nInterpunkcyjne: " << inter << endl;    
    cout << "\nReszta: " << licz << endl;    
}
int main(int argc, char **argv)
{
    const int rozmiar = 30; // deklaracja stałej
    char znaki[rozmiar]; // deklaracja tablicy znakowej 
    cout << "Jak się nazywasz? ";
    cin.getline(znaki, rozmiar);
    cout << "Cześć " << znaki << endl;
    //licz_znaki(znaki);
    ascii(znaki);
	
	return 0;
}
