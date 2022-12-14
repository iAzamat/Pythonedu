'''
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
in     -> out
6782   -> 23
0,67   -> 13
198,45 -> 27
'''


def task01():
    n = input("Введите число = ").replace('.', '').replace('-', '')
    while not n.isdigit():
        n = input("Введите число = ").replace('.', '').replace('-', '')

    my_sum = 0
    # for i in s:
    #     my_sum += int(i)
    n = list(n)
    print(map(int, n))
    my_sum = sum(list(map(int, n)))
    print(my_sum)


# task01()


'''
3. Задайте список из n чисел последовательности, заполненный по формуле: (1+1/n)**n и выведите на экран их сумму.
Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
'''


def task02():
    n = int(input('Введите число: '))
    my_list = {k: round(((1 + 1 / k) ** k)) for k in range(1, n + 1)}
    print('Последовательность чисел: ', my_list)
    print('Сумма чисел последовательности: ', sum(my_list.values()))


# task02()


from random import randint


def task03():
    lst = [1, 2, 3, 4, 5, 6]
    for index_i in range(len(lst)):
        index_j = randint(0, len(lst) - 1)
        lst[index_i], lst[index_j] = lst[index_j], lst[index_i]

    print(lst)


# task03()


import random


def task04():
    my_list = [1, 2, 3, 4, 5]
    print(my_list)
    print(sorted(my_list, key=lambda x: random.random()))


# task04()

# import random
#
# my_list = [56, 89, 56, 34, 9, 6]
# for i, elem in enumerate(my_list):
#     a = random.randint(0, len(my_list) - 1)
#     if i != a:
#         elem, my_list[a] = my_list[a], elem
#         print(elem, my_list[a])
# print(my_list)


import os
import random


def task05():
    # Очистка терминала для удобства восприятия.
    os.system('cls')

    # Реализуйте алгоритм перемещения списка. Без функции shuffle из модуля random

    basic_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'Исходный массив:\n {basic_array}')

    random_array = []
    for i in range(len(basic_array)):
        random_array.append(basic_array.pop(random.randint(0, len(basic_array) - 1)))
    print(f'Перемешанный массив:\n {random_array}')


# task05()


# my_list = [56, 89, 56, 34, 9, 6]
# new_list = []
# for _ in (range(len(my_list))):
#     elem = my_list.pop(0)
#     new_list.append(elem)
# print(new_list)


# from random import randint
#
# my_list = [56, 89, 65, 34, 9, 6]
# for i in range(len(my_list)):
#     my_list.insert(randint(i + 1, len(my_list) - 1), my_list[i])
#     del my_list[i]
# print(my_list)

# ====================================================================
# ====================================================================
# ====================================================================

'''
1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
'''


# import struct
# import time

# def lastbit(f):
#     return struct.pack('!f', f)[-1] & 1
#
# def getrandbits(k):
#     "Return k random bits using a relative drift of two clocks."
#     # assume time.sleep() and time.clock() use different clocks
#     # though it might work even if they use the same clock
#     # XXX it does not produce "good" random bits, see below for details
#     result = 0
#     for _ in range(k):
#         time.sleep(0)
#         result <<= 1
#         result |= lastbit(time.perf_counter())
#     return result


def task06():
    n = 6
    print(random.getrandbits(n))


# task06()


def task1():
    from time import time

    my_random = time()
    n = int(input("Введите число: "))
    # print(my_random)
    # print(my_random % 1)
    print(int(my_random % 1 * n))


'''
2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
'''


def task2():
    my_list = ['uff', '32', '7kw', '0ksl']

    num = input('Введите искомое число: ')

    for elem in my_list:
        if num in elem:
            print(True)
            break
    else:
        print(False)


'''
3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
*Пример:*
- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1
'''


# count = 0
#
# for i, elem in enumerate(my_list):
#     if isinstance(user_string, str) and user_string in elem:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# else:
#     print('Ее нет')


# my_list = ["123", "234", 123, "567"]
# count = 0
# user_string = input('Insert your string: ')
# for i, elem in enumerate(my_list):
#     if type(elem) == str and user_string in elem:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# else:
#     print('Ее нет')

def task3():
    my_list = ["123", "234", "123", "567"]

    user_string = my_list[0]

    if user_string in my_list[1:]:
        print(my_list.index(user_string, 1))
    else:
        print(-1)

# task1()
# task2()
# task3()
