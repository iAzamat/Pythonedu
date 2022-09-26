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


# task1()

# from random import random, choises
#
# for _ in range(int(input('введите число: '))):
#     print(randint(0, 100), end=' ')


'''
2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
    *Пример:*
    
    - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
'''


def task2():
    n = int(input("Введите число n: "))
    my_dict = dict
    for i in range(1, n):
        my_dict = {'ID': i, 'Value': 3 * i + 1}
        print(my_dict)


# task2()


# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

def task3():
    text1 = input("Введите 1 строку: ")
    text2 = input("Введите 2 строку: ")
    count = 0
    while poz != -1:
        poz = text1.find(text2, poz)
        if poz != -1:
            count += 1
    print(text1, text2, count)

    # for i in range(len(text1)):


task3()

#