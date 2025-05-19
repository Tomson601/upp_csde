#include <iostream>
using namespace std;

class Student;
class Prowadzacy;
void EgzaminInfo(class Egzamin& egzamin);

class Egzamin
{
private:
    string przedmiot[100];
    string prowadzacy[100];
    string termin[100];
    string liczba_pytan[100];
    string tresc_pytan[100];
public:
    friend class Prowadzacy;
    friend class Student;
    friend void EgzaminInfo(Egzamin& egzamin);
};

void EgzaminInfo(Egzamin& egzamin){
    cout << "Przedmiot: " << egzamin.przedmiot[0] << endl;
    cout << "Prowadzacy: " << egzamin.prowadzacy[0] << endl;
    cout << "Termin: " << egzamin.termin[0] << endl;
    cout << "Liczba pytan: " << egzamin.liczba_pytan[0] << endl;
    cout << "Tresc pytan: " << egzamin.tresc_pytan[0] << endl;
}

class Prowadzacy
{
    string imie;
    string nazwisko;
public:
    void DodajEgzamin(Egzamin& egzamin, string przedmiot, string prowadzacy, string termin, string liczba_pytan, string tresc_pytan)
    {
        egzamin.przedmiot[0] = przedmiot;
        egzamin.prowadzacy[0] = prowadzacy;
        egzamin.termin[0] = termin;
        egzamin.liczba_pytan[0] = liczba_pytan;
        egzamin.tresc_pytan[0] = tresc_pytan;

        cout << "Egzamin dodany pomyslnie!" << endl;
    }
};

class Student
{
    string imie;
    string nazwisko;
public:
    void InformujOPrzedmiocie(const Egzamin& egzamin)
    {
        cout << "Przedmiot: " << egzamin.przedmiot[0] << endl;
    }
    void InformujOProwadzacym(const Egzamin& egzamin)
    {
        cout << "Prowadzacy: " << egzamin.prowadzacy[0] << endl;
    }
    void InformujOLiczbiePytan(const Egzamin& egzamin)
    {
        cout << "Liczba pytan: " << egzamin.liczba_pytan[0] << endl;
    }
};

int main()
{
    Egzamin egzamin;
    Prowadzacy prowadzacy;
    prowadzacy.DodajEgzamin(egzamin, "Matematyka", "Jan Kowalski", "2023-06-15", "10", "Podaj wynik dzialania 2+2");


    // Student student;
    // student.InformujOPrzedmiocie(egzamin);
    // student.InformujOProwadzacym(egzamin);
    // student.InformujOLiczbiePytan(egzamin);

    EgzaminInfo(egzamin);

    return 0;
}
