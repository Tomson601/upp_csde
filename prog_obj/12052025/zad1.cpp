#include <stdio.h>
#include <iostream>

using namespace std;

class Atrakcja {
protected:
    double cena;
    string nazwa;
    string opis;

public:
    void podajDane(){
        cout << "Podaj nazwe: "; cin >> nazwa;
        cout << "Podaj cene: "; cin >> cena;
        cout << "Podaj opis: "; cin >> opis;
    }

    void wyswietlDane(){
        cout << "Nazwa: " << nazwa << endl;
        cout << "Cena: " << cena << endl;
        cout << "Opis: " << opis << endl;
    }
};

class Kolejka : public Atrakcja {
private:
    string godz_odjazdu;
    string godz_przyjazdu;

public:
    void Inicjuj(string godz_odjazdu, string godz_przyjazdu) {
        this->godz_odjazdu = godz_odjazdu;
        this->godz_przyjazdu = godz_przyjazdu;
    }
};

class Zamek : public Atrakcja {
private:
    string czas_zwiedzania;

public:
    void Inicjuj(string czas_zwiedzania) {
        this->czas_zwiedzania = czas_zwiedzania;
    }
};

class Film : public Atrakcja {
private:
    string czas_trwania;
    string tytul;

public:
    void Inicjuj(string czas_trwania, string tytul) {
        this->czas_trwania = czas_trwania;
        this->tytul = tytul;
    }
};

int main() {
    Kolejka kolejka;
    kolejka.podajDane();
    kolejka.Inicjuj("10:00", "12:00");
    kolejka.wyswietlDane();

    cout << endl;

    Zamek zamek;
    zamek.podajDane();
    zamek.Inicjuj("2 godziny");
    zamek.wyswietlDane();

    cout << endl;

    Film film;
    film.podajDane();
    film.Inicjuj("1 godzina 30 minut", "Przykładowy film");
    film.wyswietlDane();

    return 0;
}
