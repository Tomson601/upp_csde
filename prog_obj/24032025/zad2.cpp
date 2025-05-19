#include <iostream>
using namespace std;

double add(double& a, double& b) {
    return a + b;
}

double subtract(double& a, double& b) {
    return a - b;
}

double multiply(double& a, double& b) {
    return a * b;
}

double divide(double& a, double& b) {
    return a / b;
}


int main() {
    double a, b;

    cout << "MENU:" << endl;
    cout << "1. Dodawanie" << endl;
    cout << "2. Odejmowanie" << endl;
    cout << "3. Mnożenie" << endl;
    cout << "4. Dzielenie" << endl;
    cout << "Wybierz operację: ";

    int choice;
    cin >> choice;

    cout << "Podaj pierwszą liczbę: ";
    cin >> a;
    cout << "Podaj drugą liczbę: ";
    cin >> b;

    switch (choice) {
        case 1:
            cout << "Wynik dodawania: " << add(a, b) << endl;
            break;
        case 2:
            cout << "Wynik odejmowania: " << subtract(a, b) << endl;
            break;
        case 3:
            cout << "Wynik mnożenia: " << multiply(a, b) << endl;
            break;
        case 4:
            cout << "Wynik dzielenia: " << divide(a, b) << endl;
            break;
        default:
            cout << "Niepoprawny wybór" << endl;
    }

    return 0;
}
