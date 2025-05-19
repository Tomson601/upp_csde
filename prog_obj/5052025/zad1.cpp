#include <iostream>
using namespace std;

struct Prostokat
{
    private:
    int a;
    int b;
    string kolor;

    public:
    Prostokat() : a(0), b(0), kolor("bialy") {}
    Prostokat(int dlugosc, int wysokosc, string kolor) : a(dlugosc), b(wysokosc), kolor(kolor) {}
    friend void Czy_Kwadrat(Prostokat& prostokat);
};

void Czy_Kwadrat(Prostokat& prostokat)
{
    if (prostokat.a == prostokat.b)
    {
        cout << "Prostokat jest kwadratem." << endl;
    }
    else
    {
        cout << "Prostokat nie jest kwadratem." << endl;
    }
}

int main()
{
    Prostokat P1;
    Czy_Kwadrat(P1);
    Prostokat prostokat2(5, 10, "czerwony");
    Czy_Kwadrat(prostokat2);

    return 0;
}
