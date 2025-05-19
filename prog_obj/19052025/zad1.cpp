#include <iostream>
using namespace std;


// 1. Funkcja oblicz: a - b + c
template <typename T>
T oblicz(T a, T b, T c) {
    return a - b + c;
}

// 2. Funkcja maksimum: zwraca większy z dwóch argumentów
template <typename T>
T maksimum(T a, T b) {
    return (a > b) ? a : b;
}

// 3. Funkcja tablica: wypisuje wszystkie elementy tablicy
template <typename T>
void tablica(T arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int a1 = 5, b1 = 3, c1 = 2;
    double a2 = 5.5, b2 = 2.2, c2 = 1.1;

    cout << "oblicz<int>: " << oblicz(a1, b1, c1) << endl;
    cout << "oblicz<double>: " << oblicz(a2, b2, c2) << endl;

    cout << "maksimum<int>: " << maksimum(10, 20) << endl;
    cout << "maksimum<double>: " << maksimum(3.14, 2.71) << endl;

    int arr1[] = {1, 2, 3, 4, 5};
    double arr2[] = {1.1, 2.2, 3.3};

    cout << "tablica<int>: ";
    tablica(arr1, 5);

    cout << "tablica<double>: ";
    tablica(arr2, 3);

    return 0;
}
