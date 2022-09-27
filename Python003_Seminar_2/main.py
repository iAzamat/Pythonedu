'''
1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    *Пример:*
    - Для N = 5: 1, -3, 9, -27, 81
'''

import random


def task1():
    def my_random(n):
        b = []
        for _ in range(n):
            b.append(random.randint(0, 100))
        return b

    n = int(input("Введите число N: "))
    print(my_random(n))


# =============
# from random import randint, choices
#
# for _ in range(int(input("Введите число N: "))):
#     print(randint(0,100), end=' ')

# my_list=[randint(0,100) for _ in range(int(input("Введите число N: ")))]
# print(*my_list)


'''
2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
    *Пример:*
    
    - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
'''


def task2():
    n = int(input("Введите число n: "))
    my_dict = dict()
    for i in range(1, n + 1):
        my_dict[i] = 3 * i + 1

    print(my_dict)


# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

def task31():
    text1 = input("Введите 1 строку: ")
    text2 = input("Введите 2 строку: ")
    count = 0
    poz = 0
    i = 0
    while i < (int(len(text1) / len(text2))):
        poz = text1.find(text2, poz)
        i += 1
        if poz != -1 and poz < len(text1):
            count += 1
            poz += len(text2)
        else:
            break
    print(f'Количество вхождений одной строки в другую: {count} раз(а)')


def task32():
    str1 = input('Enter the string: ')
    under_str = input('Enter the under string: ')

    print(str1.count(under_str))

# task1()
# task2()
# task31()
# task32()
