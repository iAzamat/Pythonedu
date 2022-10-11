def task1():
    n = float(input('Введите вещественное число: '))
    sum = 0
    while not n.is_integer():
        n = n * 10
    while n != 0:
        sum += n % 10
        n //= 10

    print(int(sum))


def task2():
    my_list = [2, 3, 5, 9, 3]
    print(sum(my_list[1::2]))


def task3():
    my_list = [2, 3, 5, 9, 3]
    my_sum = 0
    for i in range(1, len(my_list), 2):
        my_sum += my_list[i]
    print(my_sum)


def task4():
    n = [1, 2, 3, 4, 5, 6, 7]
    print(n[4:1:-1])
    print(n[::-1])


from random import uniform, randrange


def task5():
    my_list = [1.1, 1.2, 3.1, 5, 10.01]
    new_list = [round(val % 1, 2) for val in my_list if isinstance(val, float)]

    print(new_list)
    print(max(new_list) - min(new_list))
    # type(a)==float


'''
1. Задайте строку из набора чисел. 
Напишите программу, которая покажет большее и меньшее число. 
В качестве символа-разделителя используйте пробел.
'''


def task6():
    my_list = []
    my_list = input('Введите числа через пробел: ').split()

    res_list = [int(elem) for elem in my_list if elem.isdigit()]

    val_min = min(res_list)
    val_max = max(res_list)

    print(f'max = {val_max}, min = {val_min}')


'''
2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
1) с помощью математических формул нахождения корней квадратного уравнения
2) с помощью дополнительных библиотек Python
'''

import math


def task7():
    a = int(input('Введите переменную a: '))
    b = int(input('Введите переменную b: '))
    c = int(input('Введите переменную c: '))
    d = b ** 2 - 4 * a * c
    if a == 0:
        x = -c / b
        print(round(x, 2))
    elif d > 0:
        x_1 = (-b + math.sqrt(d)) / (2 * a)
        x_2 = (-b - math.sqrt(d)) / (2 * a)
        print(f'Дискриминант > 0 (D = {d})\nУравнение имеет 2 корня: x1 = {round(x_1, 2)}, x2 = {round(x_2, 2)}')
    elif d == 0:
        x = (-b) / (2 * a)
        print(f'Дискриминант = 0 (D = {d})\nУравнение имеет 1 корень: x = {round(x, 2)}')
    else:
        print(f'Дискриминант < 0 (D = {d})\nУравнение не имеет корней')


from sympy.solvers import solve
from sympy import Symbol


def fun(a, b, c):
    x = Symbol('x')
    return solve(f'{a}*x**2+{b}*x+{c}', x)


def task72():
    a = int(input('Введите переменную a: '))
    b = int(input('Введите переменную b: '))
    c = int(input('Введите переменную c: '))
    my_lst = [0, 0]
    my_lst[0], my_lst[1] = fun(a, b, c)
    flag = False
    for elem in my_lst:
        if not 'I' in str(elem):
            flag = True

    if flag:
        print(f'Корни уравнения: {my_lst[0]}, {my_lst[1]}')
    else:
        print('Действительных корней нет')
        print(f'Корни уравнения в комплексных переменных: {my_lst[0]}, {my_lst[1]}')


'''
3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
'''


def task8():
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    i = max(num_1, num_2)

    while not (i % num_1 == 0 and i % num_2 == 0):
        # print(i % num_1)
        # print(i % num_2)
        i += max(num_1, num_2)

    print(f'НОК ({num_1}; {num_2}) = {i}')


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mcd(n, m):
    return int((n / gcd(n, m)) * m)


def task9():
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    print(f'НОД ({num_1}; {num_2}) = {gcd(num_1, num_2)}')
    print(f'НОК ({num_1}; {num_2}) = {mcd(num_1, num_2)}')


# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
# task7()
# task72()
# task8()
# task9()
