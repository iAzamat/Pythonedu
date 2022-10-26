def types_func_create(data):
    text = input('Введите название типа: ')
    next_number = (data[-1][0]) + 1
    data.append((next_number, text))


def types_func_delete(data):
    min_number = (data[0][0])
    max_number = (data[-1][0])
    print(*data)
    number = int(input(f'Введите ID типа, который хотели бы удалить {min_number} - {max_number}: '))
    data.pop(number - 1)


def types_func_modify(data):
    min_number = (data[0][0])
    max_number = (data[-1][0])
    print(*data)
    number = int(input(f'Введите ID типа, который хотели бы изменить {min_number} - {max_number}: '))
    text = input('Введите название типа: ')
    data[number - 1] = (number, text)
