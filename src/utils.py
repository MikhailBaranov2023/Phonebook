import json


def list_contact():
    """
    Функция отобразения контаков в
    :return:
    """
    with open('./data.json', 'r', encoding='utf-8') as f:
        phonebook = json.load(f)

    all_contact = len(phonebook['phonebook'])
    count = 0
    for contact in phonebook['phonebook']:
        if phonebook['phonebook'].index(contact) == all_contact - 1:
            print("""
            Контактов больше нет
            """)
            while True:
                user_input = int(input("""
                Нажмите 1 чтобы выйти в главное меню.
                """))
                if user_input == 1:
                    return 'Вы вышли в главное меню'
                else:
                    continue
        else:
            print(f"""
            {contact["last_name"]} {contact["first_name"]} {contact["father_name"]} 
            Рабочий номер: {contact['work_phone']},
            Личный номер: {contact['personal_phone']}
        """)
        count += 1
        if count == 10:
            print("Страница закончилась")
            user_input = str(input("""
            Введите 1 если хотите продолжить
            Введите 2 если хотите выйти
            """))
            if user_input == '1':
                count = 0
                continue
            if user_input == '2':
                return 'Вы вышли в главное меню'


def phonebook_search(initials: str, phonebook):
    """
    Функция находит контакт и возвращает его в виде словаря
    :param initials: Фамилия Имя Отчество.
    :param phonebook: Это словарь у которого есть ключ ['phonebook'] значением которого является список контактов.
    :return: dict искомого контакта
    """
    try:
        initials_list = initials.split()
        last_name = initials_list[0]
        first_name = initials_list[1]
        father_name = initials_list[2]
        for contact in phonebook['phonebook']:
            if last_name in contact.values():
                if first_name in contact.values():
                    if father_name in contact.values():
                        return contact
    except IndexError:
        Exception("""Проверьте введенные данные. Данные должны быть введены в формате 'Фамилия Имя Отчество'""")


def search_contact(initials: str):
    """
    Функция поиска контакта в контактной книги по ФИО
    :param initials: Фамилия Имя Отчество.
    :return:Данные искомого контакта.

    """
    with open('./data.json', encoding='utf-8') as f:
        phonebook = json.load(f)

    if phonebook_search(initials, phonebook) == None:
        return """
        Контакт не найден. Проверьте введенные данные. Данные должны быть введены в формате 'Фамилия Имя Отчество'
        """
    else:
        print(f"""
        {phonebook_search(initials, phonebook)['last_name']} {phonebook_search(initials, phonebook)['first_name']} {phonebook_search(initials, phonebook)['father_name']},
        Рабочий номер: {phonebook_search(initials, phonebook)['work_phone']}, Личный номер: {phonebook_search(initials, phonebook)['personal_phone']}
        """)
        user_input = int(input("""
        Введите 1 если хотите изменить контакт
        Введите 2 если хотите завершить."""))
        if user_input == 1:
            return update_book(initials)
        elif user_input == 2:
            return 'Вы вышли в главное меню'


def update_book(initials: str):
    """
    Функция обновления контактной книги по ФИО
    :param initials: Фамилия Имя Отчество.
    :return:Измененные данные контакта.

    """
    with open('./data.json', encoding='utf-8') as f:
        phonebook = json.load(f)

    if phonebook_search(initials, phonebook) == None:
        return """
        Контакт не найден. Проверьте введенные данные. Данные должны быть введены в формате 'Фамилия Имя Отчество'
        """
    else:
        user_input = int(input(f"""
                            Вы хотите изменить контакт:
                            {phonebook_search(initials, phonebook)['last_name']} {phonebook_search(initials, phonebook)['first_name']} {phonebook_search(initials, phonebook)['father_name']},
                            Рабочий номер: {phonebook_search(initials, phonebook)['work_phone']}, Личный номер: {phonebook_search(initials, phonebook)['personal_phone']}.
    
                            Если хотите продолжить введите 1.
                            Если хотите вернуться в меню нажмите 2.
                            """))
        if user_input == 1:
            new_work_phone = str(input("""
            Введите актуальный рабочий номер телефона: 
            """))
            phonebook_search(initials, phonebook)['work_phone'] = new_work_phone
            new_personal_phone = str(input("""
            Введите актульный личный номер телефона: 
            """))
            phonebook_search(initials, phonebook)['personal_phone'] = new_personal_phone

            user_input = int(input("""
                                    Если хотите подтвердить изменение введите 1.
                                    Если хотите отменить изменения введите 2.
                                    """))
            if user_input == 1:
                with open('./data.json', 'w', encoding='utf-8') as outfile:
                    json.dump(phonebook, outfile, ensure_ascii=False, sort_keys=True)
                return f"""
                Вы обновили контактные данные у контакта:{phonebook_search(initials, phonebook)['last_name']} {phonebook_search(initials, phonebook)['first_name']} {phonebook_search(initials, phonebook)['father_name']}
                Рабочий номер телефона {phonebook_search(initials, phonebook)['work_phone']},
                Личный номер телефона {phonebook_search(initials, phonebook)['personal_phone']}
                
                """
            elif user_input == 2:
                return 'Вы отменили изменения'

        elif user_input == 2:
            return 'Вы отменили изменения'


def add_book():
    """
    Функция позволяет добаить контакт, а также в случве если такой контак уже есть выводит имеюзиеся данные.
    :return:
    """
    initials = str(input('Введите данные в формате: Фамилия Имя Отчество - ').title())
    initials_list = initials.split()
    try:
        last_name = initials_list[0]
        first_name = initials_list[1]
        father_name = initials_list[2]
        work_phone = str(input('Введите рабочий номер телефон:'))
        personal_phone = str(input('Введите ваш личный номер телефон:'))

        new_data = {'last_name': last_name, 'first_name': first_name, 'father_name': father_name,
                    'work_phone': work_phone,
                    'personal_phone': personal_phone}

        with open('./data.json', encoding='utf-8') as file:
            data = json.load(file)
        data['phonebook'].append(new_data)
        if new_data in data['phonebook']:
            print('Такой контакт уже существует')
            print(search_contact(initials))
            user_input = str(input("""
            Введите 1 если хотите изменить контакт
            Введите 2 если хотите выйти
            """))
            if user_input == '1':
                return update_book(initials)
            elif user_input == '2':
                return 'Изменения отменены'
        else:
            with open('./data.json', 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False)
            return f"""
                Вы дабавили новый контакт:
                {new_data['last_name']} {new_data['first_name']} {new_data['father_name']}
                Рабочий номер: {new_data['work_phone']}
                Личный номер: {new_data['personal_phone']}
                """
    except IndexError:
        print("""Проверьте введенные данные. Данные должны быть введены в формате 'Фамилия Имя Отчество'""")
