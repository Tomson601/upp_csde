#include <iostream>
#include <vector>
#include <cctype>
using namespace std;

bool contains_digit(const string& str) {
    for (char ch : str) {
        if (isdigit(ch)) {
            return true;
        }
    }
    return false;
}

vector<string> filter_strings(const vector<string>& input) {
    vector<string> result;
    for (const string& str : input) {
        if (!contains_digit(str)) {
            result.push_back(str);
        }
    }
    return result;
}

void print_vector(const vector<string>& vec) {
    for (const string& str : vec) {
        cout << str << " ";
    }
    cout << endl;
}

int main() {
    vector<string> words;
    string word;
    int n;

    cout << "Podaj liczbę ciągów znaków: ";
    cin >> n;
    cin.ignore();

    cout << "Podaj " << n << " ciągów znaków: " << endl;
    for (int i = 0; i < n; i++) {
        getline(cin, word);
        words.push_back(word);
    }

    vector<string> filtered_words = filter_strings(words);

    cout << "Wektor bez ciągów zawierających cyfry: ";
    print_vector(filtered_words);
    
    return 0;
}
