import time

print("Введите название файла: ")
filename = input()
with open(filename, encoding="utf8") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

class Contact:
    def __init__(self, id, surname, name, patronymic, phone, mail):
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone
        self.mail = mail

contacts = {}
id = 0

for line in lines:
    id += 1
    line_cut = line.split(',')
    fio = line_cut[0].split(' ')
    contacts.update([
        (id, Contact(id, fio[0], fio[1] if len(fio) > 1 else None,
        fio[2] if len(fio) == 3 else None, line_cut[1][1:] if line_cut[1] != '' else None,
                line_cut[2][1:] if line_cut[2] != '' else None))])

command = -1
while command != 6:
    print('Выберите команду из списка:', '1) Поиск по ФИО', '2) Поиск по телефону', '3) Поиск по почте',
          '4) Поиск по отсутствующему элементу', '5) Изменение контакта', '6) Выход', sep='\n')
    command = int(input())
    result = []
    if command == 6:
        break
    elif command == 1:
        print('Введите ФИО: ')
        search = input()
        for contact in contacts.values():
            search_array = search.split(' ')
            if len(search_array) == 1:
                if contact.surname == search_array[0] or contact.name == search_array[0] or contact.patronymic == search_array[0]:
                    result.append(contact)
            elif len(search_array) == 2:
                if (contact.surname == search_array[0] and contact.name == search_array[1]) or (
                        contact.name == search_array[0] and contact.patronymic == search_array[1]):
                    result.append(contact)
            else:
                if contact.surname == search_array[0] and contact.name == search_array[1] and contact.patronymic == search_array[2]:
                    result.append(contact)

    elif command == 2:
        print('Введите телефон: ')
        search = input()
        for contact in contacts.values():
            if  contact.phone == search:
                result.append(contact)

    elif command == 3:
        print('Введите почту: ')
        search = input()
        for contact in contacts.values():
            if contact.mail == search:
                result.append(contact)

    elif command == 4:
        print('Введите тип отсутствующего элемента: 1) Телефон 2) Почта 3) Телефон и почта')
        search = int(input())
        for contact in contacts.values():
            if search == 1:
                if contact.phone is None:
                    result.append(contact)
            elif search == 2:
                if contact.mail is None:
                    result.append(contact)
            elif search == 3:
                if contact.mail is None and contact.phone is None:
                    result.append(contact)

    elif command == 5:
        print('Что изменить: 1)Телефон 2)Почта 3)Имя 4)Фамилия 5)Отчество')
        edit_field = int(input())
        print('Кому: 1) Поиск по ФИО', '2) Поиск по телефону', '3) Поиск по почте', '4) Поиск по отсутствующему элементу')
        command_2 = int(input())
        result = []
        if command_2 == 1:
            print('Введите ФИО: ')
            search = input()
            for contact in contacts.values():
                search_array = search.split(' ')
                if len(search_array) == 1:
                    if contact.surname == search_array[0] or contact.name == search_array[0] or contact.patronymic == search_array[0]:
                        result.append(contact)
                elif len(search_array) == 2:
                    if (contact.surname == search_array[0] and contact.name == search_array[1]) or (contact.name == search_array[0] and contact.patronymic == search_array[1]):
                        result.append(contact)
                else:
                    if contact.surname == search_array[0] and contact.name == search_array[1] and contact.patronymic == search_array[2]:
                        result.append(contact)
        elif command_2 == 2:
            print('Введите телефон: ')
            search = input()
            for contact in contacts.values():
                if contact.phone == search:
                    result.append(contact)
        elif command_2 == 3:
            print('Введите почту: ')
            search = input()
            for contact in contacts.values():
                if contact.mail == search:
                    result.append(contact)
        elif command_2 == 4:
            print('Введите тип отсутствующего элемента: 1) Телефон 2) Почта 3) Телефон и почта')
            search = input()
            for contact in contacts.values():
                if search == 1:
                    if contact.phone is None:
                        result.append(contact)
                elif search == 2:
                    if contact.email is None:
                        result.append(contact)
                elif search == 3:
                    if contact.email is None:
                        if contact.phone is None:
                            result.append(contact)

        print('Желаемый результат: ')
        edit_value = input()
        if len(result) > 1:
            print('Невозможно изменить сразу несколько контактов', 'Выберите другой способ поиска контакта', sep='\n')
        else:
            if edit_field == 1:
                contacts[result[0].id].phone = edit_value
            elif edit_field == 2:
                contacts[result[0].id].email = edit_value
            elif edit_field == 3:
                contacts[result[0].id].name = edit_value
            elif edit_field == 4:
                contacts[result[0].id].surname = edit_value
            elif edit_field == 5:
                contacts[result[0].id].patronymic = edit_value

    for each_result in result:
        surname = each_result.surname
        if each_result.name is None:
            name = ' '
        else:
            name  = each_result.name
        if each_result.patronymic is None:
             patronymic = ' '
        else:
             patronymic = each_result.patronymic
        if each_result.phone is None:
             phone = ' '
        else:
             phone = each_result.phone
        if each_result.mail is None:
              mail = ' '
        else:
              mail = each_result.mail
        print('Фамилия: ' + surname, 'Имя: ' + name, 'Отчество: ' + patronymic, 'Телефон:  ' + phone, 'Почта: ' + mail, sep='\n')
    time.sleep(5)