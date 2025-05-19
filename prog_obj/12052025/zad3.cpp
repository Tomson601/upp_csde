#include <iostream>

using namespace std;

class Samochod {
protected:
    string marka;
    double poj_baku;
    int dystans;
    float zuzycie_paliwa;
    float predkosc;
public:
    Samochod() {}

    Samochod(string m, double pb, int d, float zp, float pr) {
        marka = m;
        poj_baku = pb;
        dystans = d;
        zuzycie_paliwa = zp;
        predkosc = pr;
    }

    int liczbaTankowan() {
        return dystans / (poj_baku * zuzycie_paliwa);
    }

    void ustawDystans(int d) {
        dystans = d;
    }

    void pokazDystans() {
        cout << "Dystans: " << dystans << endl;
    }

    void ustawDane(string m, double pb, int d, float zp, float pr) {
        marka = m;
        poj_baku = pb;
        dystans = d;
        zuzycie_paliwa = zp;
        predkosc = pr;
    }
    
    void pokazDane() {
        cout << "Marka: " << marka << endl;
        cout << "Pojemnosc baku: " << poj_baku << endl;
        cout << "Dystans: " << dystans << endl;
        cout << "Zuzycie paliwa: " << zuzycie_paliwa << endl;
        cout << "Predkosc: " << predkosc << endl;
    }

    friend float SrednieSpalanieNa100(const Samochod& samochod);
    friend float SrednieSpalanieNaOdcinku(const Samochod& samochod, int dystans);
    friend int LiczbaTankowan(const Samochod& samochod, int dystans);
};

class Kabriolet : public Samochod {
protected:
    bool dach_otwarty;
public:
    Kabriolet() {
        dach_otwarty = false;
    }

    void otworzDach() {
        dach_otwarty = true;
    }

    void zamknijDach() {
        dach_otwarty = false;
    }

    float getZuzyciePaliwa() const {
        if (dach_otwarty) {
            return zuzycie_paliwa * 1.15;
        }
        return zuzycie_paliwa;
    }

    void czyDachOtwarty() {
        if (dach_otwarty) {
            cout << "Dach jest otwarty." << endl;
        } else {
            cout << "Dach jest zamkniety." << endl;
        }
    }
};

float SrednieSpalanieNa100(const Samochod& samochod) {
    return samochod.zuzycie_paliwa;
}

float SrednieSpalanieNa100(const Kabriolet& kabriolet) {
    return kabriolet.getZuzyciePaliwa();
}

float SrednieSpalanieNaOdcinku(const Samochod& samochod, int dystans) {
    return (samochod.zuzycie_paliwa / 100) * dystans;
}

float SrednieSpalanieNaOdcinku(const Kabriolet& kabriolet, int dystans) {
    return (kabriolet.getZuzyciePaliwa() / 100) * dystans;
}

int LiczbaTankowan(const Samochod& samochod, int dystans) {
    return dystans / (samochod.poj_baku * samochod.zuzycie_paliwa);
}

int main() {
    Samochod samochod("Audi A3 Cabrio", 50, 1000, 5.0, 120);

    float spalanieNa100 = SrednieSpalanieNa100(samochod);
    cout << "Srednie spalanie na 100 km: " << spalanieNa100 << endl;
    float spalanieNaOdcinku = SrednieSpalanieNaOdcinku(samochod, 500);
    cout << "Srednie spalanie na odcinku 500 km: " << spalanieNaOdcinku << endl;
    int liczbaTankowan = LiczbaTankowan(samochod, 1000);
    cout << "Liczba tankowan na dystansie 1000 km: " << liczbaTankowan << endl;
    samochod.pokazDystans();

    cout << endl;

    Kabriolet kabriolet;
    kabriolet.ustawDane("Audi A3 Cabrio", 50, 1000, 5.0, 120);
    kabriolet.pokazDane();
    kabriolet.czyDachOtwarty();
    kabriolet.otworzDach();
    kabriolet.czyDachOtwarty();

    float spalanieNa100Kabriolet = SrednieSpalanieNa100(kabriolet);
    cout << "Srednie spalanie na 100 km kabrioletu: " << spalanieNa100Kabriolet << endl;
    float spalanieNaOdcinkuKabriolet = SrednieSpalanieNaOdcinku(kabriolet, 500);
    cout << "Srednie spalanie na odcinku 500 km kabrioletu: " << spalanieNaOdcinkuKabriolet << endl;
    int liczbaTankowanKabriolet = LiczbaTankowan(kabriolet, 1000);
    cout << "Liczba tankowan kabrioletu na dystansie 1000 km: " << liczbaTankowanKabriolet << endl;

    return 0;
}
