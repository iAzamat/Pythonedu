def phones_func_create(data1, data2, data3):
    print('Список людей: ')
    for elem in range(len(data2)):
        print(data2[elem][0:4])

    max_number = (data1[-1][0])
    person_id = int(input('Введите ID человека: '))
    phone_number = '+' + input('Введите номер телефона: +')
    print(data3)
    phone_type = int(input('Введите ID типa телефона: '))
    data1.append((max_number + 1, person_id, phone_type, phone_number))


def phones_func_delete(data1, data2, data3):
    print('Список людей: ')
    for elem in range(len(data2)):
        print(data2[elem][0:4])

    person_id = int(input('Введите ID человека: '))
    for elem in data1:
        if elem[1] == person_id:
            index = int(elem[2]) - 1
            type_telefon = data3[index][1:]
            print(elem[0::3] + type_telefon)
    phone_id = int(input('Введите ID телефона: '))
    data1.pop(phone_id - 1)


def phones_func_modify(data1, data2, data3):
    print('Список людей: ')
    for elem in range(len(data2)):
        print(data2[elem][0:4])
    person_id = int(input('Введите ID человека: '))
    for elem in data1:
        if elem[1] == person_id:
            index = int(elem[2]) - 1
            type_telefon = data3[index][1:]
            print(elem[0::3] + type_telefon)
    phone_id = int(input('Введите ID телефона: '))
    phone_number = '+' + input('Введите номер телефона: +')
    print(data3)
    phone_type = int(input('Введите ID типa телефона: '))
    data1[phone_id - 1] = (phone_id, person_id, phone_type, phone_number)
