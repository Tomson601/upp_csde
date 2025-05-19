#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

struct DaneOsobowe
{
    string imie;
    string nazwisko;
};

struct Wynagrodzenie
{
    double styczen;
    double luty;
    double marzec;
    double kwiecien;
    double maj;
    double czerwiec;
    double lipiec;
    double sierpien;
};

struct Pracownicy
{
    DaneOsobowe dane;
    Wynagrodzenie wynagrodzenie;

    void Wpisz()
    {
        cout << "Podaj imie: ";
        cin >> dane.imie;
        cout << "Podaj nazwisko: ";
        cin >> dane.nazwisko;

        cout << "Podaj wysokosc wynagrodzenia za styczen: ";
        cin >> wynagrodzenie.styczen;
        cout << "Podaj wysokosc wynagrodzenia za luty: ";
        cin >> wynagrodzenie.luty;
        cout << "Podaj wysokosc wynagrodzenia za marzec: ";
        cin >> wynagrodzenie.marzec;
        cout << "Podaj wysokosc wynagrodzenia za kwiecien: ";
        cin >> wynagrodzenie.kwiecien;
        cout << "Podaj wysokosc wynagrodzenia za maj: ";
        cin >> wynagrodzenie.maj;
        cout << "Podaj wysokosc wynagrodzenia za czerwiec: ";
        cin >> wynagrodzenie.czerwiec;
        cout << "Podaj wysokosc wynagrodzenia za lipiec: ";
        cin >> wynagrodzenie.lipiec;
        cout << "Podaj wysokosc wynagrodzenia za sierpien: ";
        cin >> wynagrodzenie.sierpien;
    }

    void Drukuj()
    {
        cout << "Imie: " << dane.imie << endl;
        cout << "Nazwisko: " << dane.nazwisko << endl;
        cout << "Wynagrodzenie za styczen: " << wynagrodzenie.styczen << endl;
        cout << "Wynagrodzenie za luty: " << wynagrodzenie.luty << endl;
        cout << "Wynagrodzenie za marzec: " << wynagrodzenie.marzec << endl;
        cout << "Wynagrodzenie za kwiecien: " << wynagrodzenie.kwiecien << endl;
        cout << "Wynagrodzenie za maj: " << wynagrodzenie.maj << endl;
        cout << "Wynagrodzenie za czerwiec: " << wynagrodzenie.czerwiec << endl;
        cout << "Wynagrodzenie za lipiec: " << wynagrodzenie.lipiec << endl;
        cout << "Wynagrodzenie za sierpien: " << wynagrodzenie.sierpien << endl;
    }
};

double SrednieZarobki(Pracownicy pracownicy[], int liczbaPracownikow)
{
    double suma = 0;
    int liczbaMiesiecy = 8;
    for (int i = 0; i < liczbaPracownikow; i++)
    {
        suma += pracownicy[i].wynagrodzenie.styczen + pracownicy[i].wynagrodzenie.luty +
                pracownicy[i].wynagrodzenie.marzec + pracownicy[i].wynagrodzenie.kwiecien +
                pracownicy[i].wynagrodzenie.maj + pracownicy[i].wynagrodzenie.czerwiec +
                pracownicy[i].wynagrodzenie.lipiec + pracownicy[i].wynagrodzenie.sierpien;
    }
    return suma / (liczbaPracownikow * liczbaMiesiecy);
}

int main()
{
    Pracownicy pracownicy[3];
    for (int i = 0; i < 3; i++)
    {
        pracownicy[i].Wpisz();
    }

    for (int i = 0; i < 3; i++)
    {
        pracownicy[i].Drukuj();
    }

    double srednieZarobki = SrednieZarobki(pracownicy, 3);
    cout << "Srednie zarobki: " << srednieZarobki << endl;

    return 0;
}
