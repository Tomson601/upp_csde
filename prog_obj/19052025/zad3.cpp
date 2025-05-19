#include <iostream>
using namespace std;

template <typename T>
class Liczba {
private:
    T wartosc;

public:
    void Wczytaj() {
        cout << "Podaj wartosc: ";
        cin >> wartosc;
    }

    void Wydrukuj() const {
        cout << "Wartosc: " << wartosc << endl;
    }
};

int main() {
    Liczba<int> liczbaInt;
    liczbaInt.Wczytaj();
    liczbaInt.Wydrukuj();

    Liczba<float> liczbaFloat;
    liczbaFloat.Wczytaj();
    liczbaFloat.Wydrukuj();

    Liczba<double> liczbaDouble;
    liczbaDouble.Wczytaj();
    liczbaDouble.Wydrukuj();

    return 0;
}
