#include <iostream>

using namespace std;


class JednostkaMiary {
protected:
    string jednostka;
    string wartosc;
};

class Dlugosc : public JednostkaMiary {
};

class Masa : public JednostkaMiary {
};

class Czas : public JednostkaMiary {
};

