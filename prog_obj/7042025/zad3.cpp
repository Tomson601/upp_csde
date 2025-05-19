#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

struct Ksiazka
{
    string autor;
    string tytul;
    int rok;
    float cena;
    bool twarda_okladka;
};

void bookInfo(Ksiazka tablica[], int rozmiar)
{
    for (int i = 0; i < rozmiar; i++)
    {
        cout << "Autor: " << tablica[i].autor << endl;
        cout << "Tytul: " << tablica[i].tytul << endl;
        cout << "Rok wydania: " << tablica[i].rok << endl;
        cout << "Cena: " << tablica[i].cena << endl;
        cout << endl;
    }
}

void printBookCount(Ksiazka tablica[], int rozmiar)
{
    int twarda_okladka_count = 0;
    int miekka_okladka_count = 0;

    for (int i = 0; i < rozmiar; i++)
    {
        if (tablica[i].twarda_okladka)
        {
            twarda_okladka_count++;
        }
        else
        {
            miekka_okladka_count++;
        }
    }

    cout << "Liczba ksiazek o twardej okladce: " << twarda_okladka_count << endl;
    cout << "Liczba ksiazek o miekkiej okladce: " << miekka_okladka_count << endl;
}

int findMostExpensiveBookIndex(Ksiazka tablica[], int rozmiar)
{
    int indeksNajdrozszejKsiazki = 0;
    float najwyzszaCena = tablica[0].cena;

    for (int i = 1; i < rozmiar; i++)
    {
        if (tablica[i].cena > najwyzszaCena)
        {
            najwyzszaCena = tablica[i].cena;
            indeksNajdrozszejKsiazki = i;
        }
    }

    return indeksNajdrozszejKsiazki;
}

int main()
{
    Ksiazka tablica[5];

    tablica[0].autor = "A. Kamiński";
    tablica[0].tytul = "Kamienie na szaniec";
    tablica[0].rok = 1943;
    tablica[0].cena = 46;
    tablica[0].twarda_okladka = false;

    tablica[1].autor = "S. Żeromski";
    tablica[1].tytul = "Syzyfowe prace";
    tablica[1].rok = 1897;
    tablica[1].cena = 37;
    tablica[1].twarda_okladka = false;

    tablica[2].autor = "A. Mickiewicz";
    tablica[2].tytul = "Pan Tadeusz";
    tablica[2].rok = 1834;
    tablica[2].cena = 29;
    tablica[2].twarda_okladka = true;

    tablica[3].autor = "H. Sienkiewicz";
    tablica[3].tytul = "Quo vadis";
    tablica[3].rok = 1896;
    tablica[3].cena = 51;
    tablica[3].twarda_okladka = true;

    tablica[4].autor = "A. Fiedler";
    tablica[4].tytul = "Dywizjon 303";
    tablica[4].rok = 1942;
    tablica[4].cena = 39;
    tablica[4].twarda_okladka = false;

    cout << "Informacje o ksiazkach:" << endl;
    bookInfo(tablica, 5);
    printBookCount(tablica, 5);
    int najdrozszaKsiazkaIndex = findMostExpensiveBookIndex(tablica, 5);
    cout << "Najdroższa ksiazka: " << tablica[najdrozszaKsiazkaIndex].tytul << endl;
    cout << "Cena: " << tablica[najdrozszaKsiazkaIndex].cena << endl;
    cout << "Autor: " << tablica[najdrozszaKsiazkaIndex].autor << endl;
    cout << "Rok wydania: " << tablica[najdrozszaKsiazkaIndex].rok << endl;
    cout << "Okladka: " << (tablica[najdrozszaKsiazkaIndex].twarda_okladka ? "Twarda" : "Miekka") << endl;
    cout << endl;

    return 0;
}
