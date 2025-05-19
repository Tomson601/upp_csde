#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

struct Student
{
    string nazwisko;
    double ocena_dyplom;
} studenci[5];

void doRekrutacji(Student studenci[], int liczba_studentow){
    int zakwalifikowani = 0;
    for (int i = 0; i < liczba_studentow; i++)
    {
        if (studenci[i].ocena_dyplom >= 3)
        {
            cout << studenci[i].nazwisko << " zakwalifikowany." << endl;
            zakwalifikowani++;
        }
    }
}

void sredniaOcen(Student studenci[], int liczba_studentow){
    double suma = 0;
    for (int i = 0; i < liczba_studentow; i++)
    {
        suma += studenci[i].ocena_dyplom;
    }
    cout << "Srednia ocen: " << suma / liczba_studentow << endl;
}

int main()
{
    srand(time(NULL));

    for (int i = 0; i < 5; i++)
    {
        studenci[i].nazwisko = "student" + to_string(i + 1);
        studenci[i].ocena_dyplom = (rand()% 4 + 2);
    }
    cout << "Oceny studentow:" << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << studenci[i].nazwisko << ": " << studenci[i].ocena_dyplom << endl;
    }
    doRekrutacji(studenci, 5);
    sredniaOcen(studenci, 5);

    return 0;
}
