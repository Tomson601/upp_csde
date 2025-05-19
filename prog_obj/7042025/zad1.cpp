#include <iostream>

using namespace std;

struct samochod{
    char marka[20];
    char model[20];
    int rok_produkcji;
    double pojemnosc;
};

int main()
{
    samochod volkswagen_golf = {"volkswagen", "golf", 2007, 1.6};
    samochod opel_astra = {"opel", "astra", 2007, 1.7}; 

    cout << "Marka" << "\t\t" << "Model" << "\t\t" << "Rok produkcji" << "\t\t" << "Pojemnosc" << endl;
    cout << volkswagen_golf.marka << "\t" << volkswagen_golf.model << "\t\t" << volkswagen_golf.rok_produkcji << "\t\t\t" << volkswagen_golf.pojemnosc << endl;
    cout << opel_astra.marka << "\t\t" << opel_astra.model << "\t\t" << opel_astra.rok_produkcji << "\t\t\t" << opel_astra.pojemnosc << endl;

    return 0;
}
