#include <iostream>
using namespace std;

class Produkt
{
    string nazwa;
public:
    string cena;
    string ID;
    void Wyswietl()
    {
        cout << "ID: " << ID << endl;
        cout << "Nazwa: " << nazwa << endl;
        cout << "Cena: " << cena << endl;
    }
    void Dodaj()
    {
        cout << "Podaj ID: ";
        cin >> ID;
        cout << "Podaj nazwe: ";
        cin >> nazwa;
        cout << "Podaj cene: ";
        cin >> cena;
    }
};

class Koszyk
{
    Produkt produkty[100];
    int liczbaProduktow;
public:
    Koszyk() : liczbaProduktow(0) {}

    int liczba_produktow()
    {
        return liczbaProduktow;
    }

    void DodajProdukt(Produkt& produkt)
    {
        if (liczbaProduktow < 100)
        {
            produkty[liczbaProduktow] = produkt;
            liczbaProduktow++;
        }
    }

    void UsunProdukt(int index)
    {
        if (index >= 0 && index < liczbaProduktow)
        {
            for (int i = index; i < liczbaProduktow - 1; i++)
            {
                produkty[i] = produkty[i + 1];
            }
            liczbaProduktow--;
        }
    }

    void WyswietlKoszyk()
    {
        for (int i = 0; i < liczbaProduktow; i++)
        {
            produkty[i].Wyswietl();
        }
    }

    void WyswietlSume()
    {
        double suma = 0;
        for (int i = 0; i < liczbaProduktow; i++)
        {
            suma += stod(produkty[i].cena);
        }
        cout << "Suma: " << suma << endl;
    }

    void WlozProdukt(Produkt& produkt)
    {
        DodajProdukt(produkt);
    }

    void WyjmijProdukt(int index)
    {
        UsunProdukt(index);
    }
};

int main()
{
    Koszyk koszyk;
    Produkt produkt1;
    produkt1.Dodaj();
    Produkt produkt2;
    produkt2.Dodaj();

    while (true)
    {
        cout << "=== MENU USER===" << endl;
        cout << "0. Wyswietl produkty" << endl;
        cout << "1. Wloz produkt do koszyka" << endl;
        cout << "2. Wyjmij produkt" << endl;
        cout << "3. Wyswietl koszyk" << endl;
        cout << "4. Wyswietl sume" << endl;
        cout << "9. Wyjdz" << endl;

        int choice;
        cout << "Wybierz opcje: ";
        cin >> choice;

        switch (choice)
        {
            case 0:
                cout << "Dostepne produkty: " << endl;
                produkt1.Wyswietl();
                produkt2.Wyswietl();
                break;
            case 1:
            {
                cout << "Podaj ID produktu: ";
                string id;
                cin >> id;
                if (id == produkt1.ID)
                {
                    koszyk.WlozProdukt(produkt1);
                }
                else if (id == produkt2.ID)
                {
                    koszyk.WlozProdukt(produkt2);
                }
                else
                {
                    cout << "Nie znaleziono produktu o podanym ID." << endl;
                }

                break;
            }
            case 2:
            {
                int index;
                cout << "Podaj indeks produktu do usuniecia: ";
                cin >> index;
                koszyk.WyjmijProdukt(index);
                break;
            }
            case 3:
                koszyk.WyswietlKoszyk();
                break;
            case 4:
                koszyk.WyswietlSume();
                break;
            case 9:
                return 0;
            default:
                cout << "Nieprawidlowa opcja. Wybierz ponownie." << endl;
                break;
        }
    }

    return 0;
}
