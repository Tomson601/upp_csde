#include <fstream>
#include <iostream>
using namespace std;

int srednia(int tab[], int rozmiar) {
    int suma = 0;
    for (int i = 0; i < rozmiar; i++) {
        suma += tab[i];
    }
    return suma / rozmiar;
}

int main() {
    ifstream plik;
    plik.open("/home/tomasz/Desktop/progr_ob/plik.csv");

    if (plik.good()) {
        cout << "Oppening file: SUCCESS\n" << endl;
    } else {
        cout << "Błąd odczytu pliku!";
        return 1;
    }

    string tablica[100][100];
    string wiersz;
    int i = 0;
    while (getline(plik, wiersz)) {
        int j = 0;
        string wartosc = "";
        for (int k = 0; k < wiersz.length(); k++) {
            wartosc += wiersz[k];
        }
        tablica[i][j] = wartosc;
        i++;
    }

    cout << "MENU:" << endl;
    cout << "1. Wyświetl dane z pliku" << endl;
    cout << "2. Oblicz średnią wartość w kolumnie" << endl;
    cout << "3. Wyszukaj rekordy spełniające kryteria" << endl;
    cout << "4. Posortuj dane według wartości w kolumnie" << endl;
    cout << "wybór: ";

    int choice;
    cin >> choice;

    // 1. Wyświetl dane z pliku
    if (choice == 1) {
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (!tablica[i][j].empty()) {
                    cout << tablica[i][j] << " ";
                }
            }
            cout << endl;
        }
    }

    plik.close();
    return 0;
}