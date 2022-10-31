# '''Найти сумму чисел списка стоящих на нечетной позиции:'''
# lst = [1, 2, 3, 5, 1, 5, 3, 10]
# total = sum(lst[1::2])
#
# или
#
# my_sum = 0
#
# for i, val in enumerate(spisok):
#     if i % 2 != 0:
#     my_sum += val
# print(my_sum)
#
# ''' Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}'''
# num = int(input('Введите Num: '))
# dictio = zip([i for i in range(1, num + 1)], map(lambda i: 3 * i + 1, [i for i in range(1, num + 1)]))
# print(dict(dictio))
#
# ''' Найти расстояние между двумя точками пространства(числа вводятся через пробел)'''
#
# import math
#
# while True:
#     try:
#     numbers = list(map(float, input("Введите числа через пробел:\n").split(' ')))
# break
# except:
# continue
#
# pif = lambda k2, k1: (k2 - k1) ** 2
# print(round(math.sqrt((pif(numbers[3], numbers[0]) + pif(numbers[4], numbers[1]) + pif(numbers[5], numbers[2]))), 2))
#
# ''' Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.'''
# t_list = [3, 3, 5, 2, 4, 8, 5]
#
# print(list(map(lambda i: t_list[i] * t_list[len(t_list) - i - 1], range(len(t_list) // 2 + len(t_list) % 2))))
#
# '''Напишите программу, которая принимает на вход два числа. Задайте список из N элементов, заполненных числами из промежутка [N, -N].
# Найдите произведение элементов, на указанных позициях'''
#
# x, y, N = int(input('Insert position one: ')), int(input('Insert position two: ')), int(input('Number of elements: '))
# arr_new = list(range(-N, N + 1))
# print(arr_new)
# if (0 <= x < len(arr_new)) and (0 <= y < len(arr_new)):
#     (lambda a, b: print(a * b))(arr_new[x], arr_new[y])
# else:
# print('Incorrect positions have been entered')
#
# ''' Напишите программу, удаляющую из текста все слова, содержащие ""абв"" '''
# str = 'Какабв вкусны эти божеабвственные француабвзские абв булки'
# new_list = list(filter(lambda x: 'абв' not in x, str.split()))
# print(' '.join(new_list))
#
# '''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. F n = F n − 1 + F n − 2'''
#
# from random import randrange
#
# new_list = [0, 1]
#
#
# def definition_negative(value, number):
#
#
#     if number % 2: return -value
# return value
#
# for number in range(2, 8):
#     new_list.append(new_list[number - 1] + new_list[number - 2])
# else:
# new_list = [definition_negative(val, n) for n, val in enumerate(new_list[:0:-1])] + new_list
# print(new_list)
