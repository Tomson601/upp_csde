def print_menu():
    # TODO: while open
    menu = open("menu.txt", "r")
    print(menu.read())
    menu.close()
    return None
