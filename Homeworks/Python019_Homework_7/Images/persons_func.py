def persons_func_create(data):
    next_number = (data[-1][0]) + 1
    lastname = input('Введите фамилию: ')
    firstname = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    note = input('Введите описание: ')
    data.append((next_number, lastname, firstname, patronymic, note))


def persons_func_delete(data):
    min_number = (data[0][0])
    max_number = (data[-1][0])
    print(*data)
    number = int(input(f'Введите ID человека, которого вы хотели бы удалить {min_number} - {max_number}: '))
    data.pop(number - 1)


def persons_func_modify(data):
    min_number = (data[0][0])
    max_number = (data[-1][0])
    print(*data)
    number = int(input(f'Введите ID человека, которого вы хотели бы изменить {min_number} - {max_number}: '))
    lastname = input('Введите фамилию: ')
    firstname = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    note = input('Введите описание: ')
    data[number - 1] = (number, lastname, firstname, patronymic, note)
