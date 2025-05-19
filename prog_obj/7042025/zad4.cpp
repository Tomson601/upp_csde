#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

struct Zawodnik
{
    double numer;
    string imie;
    double czas;
};

struct Zawody
{
    string bieg;
    float dystans;
    Zawodnik zawodnik;
};

void wypiszWynik(Zawody zawody[], int liczbaZawodow)
{
    cout << "Wyniki zawodow:" << "\n" << endl;
    cout << "Nazwa biegu" << "\t\tDystans \tZawodnik\tNumer\tCzas" << endl;
    for (int i = 0; i < liczbaZawodow; i++)
    {
        cout << zawody[i].bieg << "\t\t" << zawody[i].dystans << "\t\t"
             << zawody[i].zawodnik.imie << "\t\t" << zawody[i].zawodnik.numer << "\t"
             << zawody[i].zawodnik.czas << endl;
    }
}

int main()
{
    Zawody zawody[] = {
        {"Bieg uliczny", 5, {1, "Adam", 28}},
        {"Bieg uliczny", 5, {2, "Tomek", 22}},
        {"Bieg terenowy", 3, {1, "Adam", 17}},
        {"Bieg terenowy", 3, {2, "Tomek", 14}}};

    int liczbaZawodow = 4;

    wypiszWynik(zawody, liczbaZawodow);

    return 0;
}
