#include <iostream>
#include <cstdlib>

using namespace std;

void los(int tab[], int ile)
{
        srand(time(NULL)); 
        for(int i = 0; i < ile; i++)
        {
            tab[i] = rand() % 31;
        }
}

void drukuj(int tab[], int ile)
{
        for(int i = 0; i < ile; i++)
        {
            cout << tab[i] << ' ';
        }
    cout << "A oto i pięć tajemniczych liczb losowych. Po co ta pajacerka? Po co przydługie zdania? Ja nie wiem.";
}

int main(int argc, char **argv)
{
    int ile = 5;
    int liczby[ile]; 
    los(liczby, ile);
    drukuj(liczby, ile);
	
	return 0;
}
