import json


# Users scetion
def add_user(name, surname, email, db_path):
    with open(db_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    new_user = {
        "uid": len(data) + 1,
        "name": name,
        "surname": surname,
        "email": email,
        "is_active": True,
        "lend_books": []
    }

    data.append(new_user)
    # Zapisanie danych do pliku:
    with open(db_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print(f"Użytkownik {name} {surname} został dodany do bazy danych.")

    return None

def deactivate_user(uid, db_path):
    with open(db_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for user in data:
        if user['uid'] == uid:
            user['is_active'] = False
            break

    with open(db_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print(f"Użytkownik {user['name']} {user['surname']} został dezaktywowany.")

    return None

def list_users(db_path):
    with open(db_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for user in data:
        if user['is_active']:
            print(f"ID: {user['uid']}")
            print(f"Imię i Nazwisko: {user['name']} {user['surname']}")
            print(f"Email: {user['email']}")
            print("-" * 30)
    return None

def get_user(uid, db_path):
    with open(db_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for user in data:
        if user['uid'] == uid:
            print(f"ID: {user['uid']}")
            print(f"Imię: {user['name']}")
            print(f"Nazwisko: {user['surname']}")
            print(f"Email: {user['email']}")

            # Sprawdzenie czy użytkownik jest aktywny w systemie:
            if user['is_active']:
                print(f"Status konta: AKTYWNE")
            else:
                print(f"Status konta: DEZAKTYWOWANE")

            # Wyświetlenie wypożyczonych książek:
            # TODO
            print(f"Wypożyczone książki: {user['lend_books']}")

            print("-" * 30)
            return None

###############################################################################
# Books section
def add_book(title, author, year, pages, db_path):
    with open(db_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    new_book = {
        "id": len(data) + 1,
        "title": title,
        "author": author,
        "realse_year": year,
        "pages": pages,
    }
    data.append(new_book)

    with open(db_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print(f"Książka {title} została dodana do bazy danych.")

    return None

def get_book(file_path, book_id):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for book in data:
        if book['id'] == book_id:
            print(f"ID: {book['id']}")
            print(f"Tytuł: {book['title']}")
            print(f"Rok wydania: {book['realse_year']}")
            print(f"Ilość stron: {book['pages']}")
            print("-" * 30)
            return None

def all_books(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for book in data:
        print(f"ID: {book['id']}")
        print(f"Tytuł: {book['title']}")
        print(f"Rok wydania: {book['realse_year']}")
        print(f"Ilość stron: {book['pages']}")
        print("-" * 30)

    return None

def exit():
    quit()
