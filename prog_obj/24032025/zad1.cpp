#include <iostream>
using namespace std;

int main() {
    int rozmiar;
    cout << "Podaj rozmiar tablicy: ";
    cin >> rozmiar;

    int *tablica = new int[rozmiar];

    for (int i = 0; i < rozmiar; i++) {
        cout << "Podaj " << i + 1 << " element tablicy: ";
        cin >> *(tablica + i);
    }

    int suma = 0;
    for (int i = 0; i < rozmiar; i++) {
        suma += *(tablica + i);
    }

    int min = *tablica;
    int max = *tablica;

    for (int i = 1; i < rozmiar; i++) {
        if (*(tablica + i) < min) {
            min = *(tablica + i);
        }
        if (*(tablica + i) > max) {
            max = *(tablica + i);
        }
    }

    cout << endl << "Suma wyrazów tablicy: " << suma << endl;
    cout << "Minimalny wyraz w tablicy: " << min << endl;
    cout << "Maksymalny wyraz w tablicy: " << max << endl;

    int sorted_tab[rozmiar];

    for (int i = 0; i < rozmiar; i++) {
        sorted_tab[i] = tablica[i];
    }

    for (int i = 0; i < rozmiar - 1; i++) {
        for (int j = 0; j < rozmiar - i - 1; j++) {
            if (sorted_tab[j] > sorted_tab[j + 1]) {
                int temp = sorted_tab[j];
                sorted_tab[j] = sorted_tab[j + 1];
                sorted_tab[j + 1] = temp;
            }
        }
    }

    cout << "Posortowana tablica:" << endl;
    for (int i = 0; i < rozmiar; i++) {
        cout << sorted_tab[i] << " ";
    }
    
    cout << endl << "KONIEC" << endl;

    delete[] tablica;

    return 0;
}
