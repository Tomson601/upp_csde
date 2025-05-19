#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;


int print_vector(vector<float> vec) {
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << " ";
    }
    cout << endl;

    return 0;
}

int main() {
    srand(time(NULL));

    int randomNum = rand() % 10;
    cout << randomNum << endl;

    for (int i=0;i<11;i++){
        int randomNum = rand() % 10;
        cout << randomNum << endl;
    }

    return 0;
}
