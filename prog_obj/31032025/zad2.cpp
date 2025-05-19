#include <iostream>
#include <vector>
using namespace std;


int print_vector(vector<int> vec) {
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << " ";
    }
    cout << endl;

    return 0;
}

int main() {
    vector<int> vec1 = {1, 2, 5, 0, 3, 1, 7, 5, 7, 1, 3, 5, 3, 0, 6, 4, 6, 3, 7, 9};
    vector<int> vec2;

    for (int i = 0; i < vec1.size(); i++) {
        if (i == 0){
            if (vec1[i] < vec1[i+1]){
                cout << i << "." << " " << vec1[i] << " " << vec1[i+1];
                vec2.push_back(vec1[i]);
            }
        }
        else if (i == vec1.size()-1){
            if (vec1[i] > vec1[i-1]){
                cout << i << "." << " " << vec1[i] << " " << vec1[i-1];
                vec2.push_back(vec1[i]);
            }
        }
        else{
            if (vec1[i] > vec1[i-1] && vec1[i] < vec1[i+1]){
                cout << i << "." << " " << vec1[i] << " " << vec1[i-1] << " " << vec1[i] << " " << vec1[i+1];
                vec2.push_back(vec1[i]);
            }
        }

        // cout << vec1[i] << " ";
    }
    cout << endl;
    print_vector(vec2);

    return 0;
}
