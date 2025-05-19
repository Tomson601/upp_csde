#include <iostream>

using namespace std;


class Mebel {
protected:
    string producent;
    string kolekcja;

public:
    void podajDane(){
        cout << "Podaj producenta: "; cin >> producent;
        cout << "Podaj kolekcje: "; cin >> kolekcja;
    }

    void wyswietlDane(){
        cout << "Producent: " << producent << endl;
        cout << "Kolekcja: " << kolekcja << endl;
    }
};

class Krzeslo : public Mebel {
public:
    string odbicie;
    void podajDane(){
        Mebel::podajDane();
        cout << "Podaj odbicie: "; cin >> odbicie;
    }
    void wyswietlDane(){
        Mebel::wyswietlDane();
        cout << "Odbicie: " << odbicie << endl;
    }
};

class Stol : public Mebel {
public:
    string szerokosc;
    string dlugosc;
    void podajDane(){
        Mebel::podajDane();
        cout << "Podaj szerokosc: "; cin >> szerokosc;
        cout << "Podaj dlugosc: "; cin >> dlugosc;
    }
    void wyswietlDane(){
        Mebel::wyswietlDane();
        cout << "Szerokosc: " << szerokosc << endl;
        cout << "Dlugosc: " << dlugosc << endl;
    }
};

class Szafka : public Mebel {
public:
    string wysokosc;
    string szerokosc;
    string glebokosc;
    void podajDane(){
        Mebel::podajDane();
        cout << "Podaj wysokosc: "; cin >> wysokosc;
        cout << "Podaj szerokosc: "; cin >> szerokosc;
        cout << "Podaj glebokosc: "; cin >> glebokosc;
    }
    void wyswietlDane(){
        Mebel::wyswietlDane();
        cout << "Wysokosc: " << wysokosc << endl;
        cout << "Szerokosc: " << szerokosc << endl;
        cout << "Glebokosc: " << glebokosc << endl;
    }
};

int main() {
    cout << "Podaj dane krzesła:" << endl;
    Krzeslo krzeslo;
    krzeslo.podajDane();
    krzeslo.wyswietlDane();
    cout << endl;

    cout << "Podaj dane stołu:" << endl;
    Stol stol;
    stol.podajDane();
    stol.wyswietlDane();
    cout << endl;

    cout << "Podaj dane szafki:" << endl;
    Szafka szafka;
    szafka.podajDane();
    szafka.wyswietlDane();
    cout << endl;


    return 0;
}
