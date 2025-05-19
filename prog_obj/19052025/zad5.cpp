#include <iostream>
using namespace std;

enum Weapon {
    SWORD,
    STAFF,
    BOW
};

template <typename T>
class WeaponType {
public:
    Weapon type;
    T damage;
    T cost;
    T durability;
};

template <typename T>
class Character {
public:
    string name;
    T health;
    WeaponType<T> weapon;
};

template <typename T>
class Warrior : public Character<T> {
public:
    void attack() {
        cout << "Warrior " << this->name << " attacks with " << this->weapon.type << endl;
    }
};
template <typename T>
class Mage : public Character<T> {
public:
    void castSpell() {
        cout << "Mage " << this->name << " casts a spell with " << this->weapon.type << endl;
    }
};
template <typename T>
class Archer : public Character<T> {
public:
    void shoot() {
        cout << "Archer " << this->name << " shoots an arrow with " << this->weapon.type << endl;
    }
};

void fight(Character<int>& character) {
    string enemy_name = "Goblin";
    float enemy_health = 50;
    Weapon enemy_weapon = SWORD;
    float enemy_damage = 10;
    float enemy_cost = 0;
    float enemy_durability = 100;
    cout << "You encounter a " << enemy_name << "!" << endl;

    while (character.health > 0 && enemy_health > 0) {
        cout << character.name << " attacks the " << enemy_name << "!" << endl;
        cout << enemy_name << " takes " << character.weapon.damage << " damage!" << endl;
        enemy_health -= character.weapon.damage;
        cout << enemy_name << " has " << enemy_health << " health left!" << endl;

        if (enemy_health <= 0) {
            cout << enemy_name << " has been defeated!" << endl;
            break;
        }
        else if (character.health <= 0) {
            cout << character.name << " has been defeated!" << endl;
            break;
        }
        cin.get();
}}


int main(){
    Warrior<int> warrior;
    warrior.name = "Conan";
    warrior.health = 100;
    warrior.weapon.type = SWORD;
    warrior.weapon.damage = 20;
    warrior.weapon.cost = 50;
    warrior.weapon.durability = 100;
    
    fight(warrior);
    return 0;
}