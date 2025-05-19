#include <iostream>
using namespace std;

template <typename T>
class Kwadrat {
public:
    double a;
    void Stworz() {
        cout << "Podaj wartość boku a: ";
        cin >> a;
    }

    void Info() const {
        cout << "Pole powierzchni: " << a*a << endl << "Obwód: " << 4*a << endl;
    }
};

template <typename T>
class Prostokat {
public:
    double a;
    double b;
    void Stworz() {
        cout << "Podaj wartość boku a: ";
        cin >> a;
        cout << endl;
        cout << "Podaj wartość boku b: ";
        cin >> b;
    }

    void Info() const {
        cout << "Pole powierzchni: " << a*b << endl << "Obwód: " << ((2*a)+(2*b)) << endl;
    }
};

template <typename T>
class Trojkat {
public:
    double a;
    double b;
    double c;
    double h;
    void Stworz() {
        cout << "Podaj wartość boku a: ";
        cin >> a;
        cout << endl;
        cout << "Podaj wartość wysokosci h: ";
        cin >> h;
        cout << endl;
        cout << "Podaj wartość boku b: ";
        cin >> b;
        cout << endl;
        cout << "Podaj wartość boku c: ";
        cin >> c;
    }

    void Info() const {
        cout << "Pole powierzchni: " << 0.5*a*h << endl << "Obwód: " << a+b+c << endl;
    }
};

template <typename T>
class Okrag {
public:
    double r;
    void Stworz() {
        cout << "Podaj wartość promienia r: ";
        cin >> r;
    }

    void Info() const {
        cout << "Pole powierzchni: " << 3.141592*r*r << endl << "Obwód: " << 2*3.141592*r << endl;
    }
};


int main() {
    int wybor;
    cout << "Wybierz figurę (1 - Kwadrat, 2 - Prostokąt, 3 - Trójkąt, 4 - Okrąg): ";
    cin >> wybor;

    switch (wybor) {
        case 1: {
            Kwadrat<int> kwadrat;
            kwadrat.Stworz();
            kwadrat.Info();
            break;
        }
        case 2: {
            Prostokat<int> prostokat;
            prostokat.Stworz();
            prostokat.Info();
            break;
        }
        case 3: {
            Trojkat<int> trojkat;
            trojkat.Stworz();
            trojkat.Info();
            break;
        }
        case 4: {
            Okrag<int> okrag;
            okrag.Stworz();
            okrag.Info();
            break;
        }
        default:
            cout << "Nieznany wybór!" << endl;
    }

    return 0;
}