from . import manage_db

BOOK_DB = 'db/book_db.json'
MAIN_DB = 'db/db_example.json'


def print_menu():
    while True:
        menu = open("func/menu.txt", "r")
        print(menu.read())
        menu.close()
        break
    return None

def handle_user_choice(choice):
    # User management
    if choice == "1":
        print("----------DODAWANIE UŻYTKOWNIKA---------")
        name = input("Podaj imię użytkownika: ")
        surname = input("Podaj nazwisko użytkownika: ")
        email = input("Podaj email użytkownika: ")

        manage_db.add_user(name=name, surname=surname, email=email, db_path=MAIN_DB)

    elif choice == "2":
        print("----------DEAKTYWACJA UŻYTKOWNIKA--------")
        uid = input("Podaj uid użytkownika: ")
        manage_db.deactivate_user(uid, MAIN_DB)

    elif choice == "3":
        print("----------UŻYTKOWNICY---------")
        manage_db.list_users(MAIN_DB)

    elif choice == "4":
        uid = input("Podaj uid użytkownika: ")
        print("----------UŻYTKOWNIK----------")
        manage_db.get_user(uid, MAIN_DB)

    # Book management
    elif choice == "5":
        print("----------DODAWANIE KSIĄŻKI---------")
        title = input("Podaj tytuł książki: ")
        author = input("Podaj autora książki: ")
        year = input("Podaj rok wydania książki: ")
        pages = input("Podaj ilość stron książki: ")
        manage_db.add_book(title, author, year, pages, BOOK_DB)

    elif choice == "6":
        print("---------DEAKTYWACJA KSIĄŻKI--------")
        id = input("Podaj id książki: ")
        manage_db.deactivate_book(id, BOOK_DB)
    
    elif choice == "7":
        print("----------KSIĄŻKI---------")
        manage_db.all_books(BOOK_DB)

    # Exit
    elif choice == "0":
        print("Zapisywanie bazy danych...")
        print("Opuszczanie programu...")
        manage_db.exit()

    else:
        print("Zły wybór!")
        return 1
