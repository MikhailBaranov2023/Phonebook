from src.utils import list_contact, search_contact, update_book, add_book
import json

if __name__ == '__main__':
    print("""
        Вы используете телефонный справочник!
        Вам доступны следующие функции:
        """)
    while True:
        user_input = int(input("""
        Вы используете телефонный справочник!
        Вам доступны следующие функции:
        Введите 1 если хотите просмотреть весь справочник.
        Введите 2 если хотите воспользоваться поиском по справочнику.
        Введите 3 если хотите добавит новый контак.
        Введите 4 если хотите изменить контакт.
        Введите 5 если хотит завершить.
        """))
        if user_input == 1:
            print(list_contact())
            continue
        elif user_input == 2:
            initials = str(input('Введите Фамилию Имя Отчество контакта: ').title())
            print(search_contact(initials))
        elif user_input == 3:
            print(add_book())
        elif user_input == 4:
            initials = str(input('Введите Фамилию Имя Отчество контакта: ').title())
            print(update_book(initials))
        elif user_input == 5:
            break
