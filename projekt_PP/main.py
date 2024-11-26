from func import handle_user


def __main__():
    while True:
        handle_user.print_menu()
        choice = input("Podaj swój wybór: ")

        handle_user.handle_user_choice(choice)

        input("Nacisnij ENTER aby kontyunuować...")

if __name__ == "__main__":
    __main__()
