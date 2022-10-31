import math
import random
import io

'''
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
in     -> out
6782   -> 23
0,67   -> 13
198,45 -> 27
'''


def protectinput(str='вещественное число'):
    valid = False
    while not valid:
        num_ = input(f'Введите {str}: ')
        try:
            num_ = float(num_)
            valid = True
            return num_
        except:
            print('Некорректный ввод. Вы уверены, что ввели число?')


def task1():
    number = str(protectinput())
    summa = 0
    for i in number:
        if i.isdigit():
            summa += int(i)

    print(f'1 способ. Сумма цифр числа {number} равна {summa}')

    # ====== 2 способ ========
    my_sum = 0
    n = list(number.replace('.', '').replace('-', ''))
    my_sum = sum(list(map(int, n)))
    print(f'2 способ. Сумма цифр числа {number} равна {my_sum}')


'''
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
1 - 1*1, 2 - 1*2, 3 - 1*2*3, 4 - 1*2*3*4
4 -> [1, 2, 6, 24]
6 -> [1, 2, 6, 24, 120, 720]
'''


def task2():
    number = int(protectinput('натуральное число'))
    lst = [math.factorial(i) for i in range(1, number + 1)]
    print(lst)

    my_dict = {k: num for k, num in enumerate(lst)}
    print(my_dict)
    for k, v in my_dict.items():
        print(v, end=' ')


'''
3. Задайте список из n чисел последовательности, заполненный по формуле: (1+1/n)**n и выведите на экран их сумму.
Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
'''


def task3():
    number = int(protectinput('натуральное число'))
    posl = [round(((1 + 1 / i) ** i)) for i in range(1, number + 1)]
    print(f'Для n = {number}: {posl} -> {sum(posl)}')


'''
4*. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, 
заполненых числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях(не индексах).

Позиции хранятся в файле file.txt в одной строке одно число.

Position one: 1
Position two: 3
Number of elements: 5
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] -> 15
'''


def task4():
    # number = abs(int(protectinput('натуральное число')))
    number = random.randint(5, 10)
    interval = [i for i in range(-number, number + 1)]
    print(f'Список: {interval}')

    with io.open('file.txt', 'r') as f:
        pos_one = int(f.readline().strip())
        pos_two = int(f.readline().strip())

    func1 = 0 < pos_one < len(interval) + 1
    func2 = 0 < pos_two < len(interval) + 1
    if not func1:
        print('Ошибка! Позиция первого элемента выходит за границы списка')
    if not func2:
        print('Ошибка! Позиция второго элемента выходит за границы списка')
    if func1 and func2:
        print(f'Position one: {pos_one}\nPosition two: {pos_two}\nNumber of elements: {number}')
        print(f'{interval} -> {interval[pos_one - 1] * interval[pos_two - 1]}')


'''
5**. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
10 
-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
'''


def lst_mix(lst_inp):
    lst_source = lst_inp.copy()
    lst_buf = []
    for _ in range(len(lst_inp)):
        rch = random.choice(lst_source)
        lst_buf.append(rch)
        lst_source.remove(rch)

    return lst_buf


def task5():
    number = random.randint(6, 11)
    my_list = [i for i in range(1, number + 1)]
    print(f'Исходный список:\n{my_list}')
    print(f'Перемешанный список (1 способ):\n{lst_mix(my_list)}')

    my_list = [i for i in range(1, number + 1)]
    print('Перемешанный список (2 способ):')
    print(sorted(my_list, key=lambda x: random.random()))


# task1()
# task2()
# task3()
# task4()
# task5()
