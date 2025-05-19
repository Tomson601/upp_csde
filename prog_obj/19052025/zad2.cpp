#include <iostream>
using namespace std;

// Szablon funkcji average
template <typename T>
T average(T* array, int size) {
    T sum = 0;
    for (int i = 0; i < size; i++) {
        sum += array[i];
    }
    return sum / size;
}

int main() {
    int arrInt[] = {10, 20, 30, 40, 50};
    int sizeInt = sizeof(arrInt) / sizeof(arrInt[0]);
    cout << "Średnia (int): " << average(arrInt, sizeInt) << endl;

    float arrFloat[] = {1.5f, 2.5f, 3.5f, 4.5f};
    int sizeFloat = sizeof(arrFloat) / sizeof(arrFloat[0]);
    cout << "Średnia (float): " << average(arrFloat, sizeFloat) << endl;

    double arrDouble[] = {2.2, 3.3, 4.4, 5.5};
    int sizeDouble = sizeof(arrDouble) / sizeof(arrDouble[0]);
    cout << "Średnia (double): " << average(arrDouble, sizeDouble) << endl;

    return 0;
}
