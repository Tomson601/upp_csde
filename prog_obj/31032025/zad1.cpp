#include <iostream>
#include <vector>
using namespace std;


int print_vector(vector<float> vec) {
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << " ";
    }
    cout << endl;

    return 0;
}

int main() {
    vector<float> vec1 = {3.5, 4.5, 2.25, 3.34};

    print_vector(vec1);

    vector<float> vec2;
    vec2 = vec1;

    print_vector(vec2);

  	vec2.push_back(0);
  	vec2.push_back(0);

  	vec2.insert(vec2.begin(), 0);
  	vec2.insert(vec2.begin(), 0);

    print_vector(vec2);

    vector<float> vec3;
    vec3 = vec2;

    print_vector(vec3);

    vec3.erase(vec3.begin() + 1);
    vec3.erase(vec3.begin() + 2);
    vec3.erase(vec3.begin() + 2);

    print_vector(vec3);

    return 0;
}
