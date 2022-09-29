import math
import random

'''
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
in     -> out
6782   -> 23
0,67   -> 13
198,45 -> 27
'''


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def protectinput(str='вещественное число'):
    num_ = input(f'Введите {str}: ')
    while not is_number(num_):
        num_ = input(f'Введите {str}: ')

    return num_


def task1():
    number = protectinput()
    sum = 0
    for i in number:
        if i.isdigit():
            sum += int(i)

    print(f'Сумма цифр числа {number} равна {sum}')


'''
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
1 - 1*1, 2 - 1*2, 3 - 1*2*3, 4 - 1*2*3*4
4 -> [1, 2, 6, 24]
6 -> [1, 2, 6, 24, 120, 720]
'''


def task2():
    number = int(protectinput('натуральное число'))
    mults = []
    for i in range(1, number + 1):
        mults.append(math.factorial(i))

    print(mults)


'''
3. Задайте список из n чисел последовательности, заполненный по формуле: (1+1/n)**n и выведите на экран их сумму.
Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
'''


def task3():
    number = int(protectinput('натуральное число'))
    posl = []
    sum = 0
    for i in range(1, number + 1):
        func = round(((1 + 1 / i) ** i))
        posl.append(func)
        sum += func

    print(f'Для n = {number}: {posl} -> {sum}')


'''
4*. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, 
заполненых числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях(не индексах).
Position one: 1
Position two: 3
Number of elements: 5
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] -> 15
'''


def task4():
    interval = []
    # number = abs(int(protectinput('натуральное число')))
    number = random.randint(5, 10)
    for i in range(-number, number + 1):
        interval.append(i)

    print(f'Список: {interval}')
    pos_one = int(protectinput('первую позицию'))
    while not 0 < pos_one < len(interval) + 1:
        pos_one = int(protectinput('первую позицию'))
    pos_two = int(protectinput('вторую позицию'))
    while not 0 < pos_two < len(interval) + 1:
        pos_two = int(protectinput('вторую позицию'))

    print(f'Position one: {pos_one}\nPosition two: {pos_two}\nNumber of elements: {number}')
    print(f'{interval} -> {interval[pos_one - 1] * interval[pos_two - 1]}')


'''
5**. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
10 
-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
'''


def lst_mix(lst_inp):
    lst_source = []
    lst_source = lst_inp.copy()
    lst_buf = []
    for _ in range(len(lst_inp)):
        rch = random.choice(lst_source)
        lst_buf.append(rch)
        lst_source.remove(rch)

    return lst_buf


def task5():
    my_list = []
    number = random.randint(6, 11)
    for i in range(number):
        my_list.append(i)

    print(f'Исходный список:\n{my_list}')
    print(f'Перемешанный список:\n{lst_mix(my_list)}')


# task1()
# task2()
# task3()
# task4()
# task5()
