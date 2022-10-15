import random

'''
1. Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
*Пример:*
2+2 => 4;
1+2*3 => 7;
1-2*3 => -5;

Добавьте возможность использования скобок, меняющих приоритет операций.
*Пример:*
1+2*3 => 7;
(1+2)*3 => 9;

'''

# def my_action(op, digit_1, digit_2):
#     if op == '+':
#         return digit_1 + digit_2
#     elif op == '-':
#         return digit_1 - digit_2
#     elif op == '/':
#         return digit_1 // digit_2
#     elif op == '*':
#         return digit_1 * digit_2
#
#
# my_string = '1+2+3*5-6/3+7-9*0*3*4'
# my_list_symbols = [i for i in my_string if not i.isdigit()]
#
# my_list_digits = [int(i) for i in my_string if i.isdigit()]
#
# while '*' in my_list_symbols or '/' in my_list_symbols:
#     for i, e in enumerate(my_list_symbols):
#         if e in ('*', '/'):
#             my_list_digits[i] = my_action(e, my_list_digits[i], my_list_digits[i + 1])
#             del my_list_digits[i + 1]
#             del my_list_symbols[i]
# while len(my_list_symbols) > 0:
#     for i, e in enumerate(my_list_symbols):
#         my_list_digits[i] = my_action(e, my_list_digits[i], my_list_digits[i + 1])
#         del my_list_digits[i + 1]
#         del my_list_symbols[i]
#
# # print(my_list_symbols)
# print(my_list_digits)


'''
2. Дана последовательность чисел. 
Получить список уникальных элементов заданной последовательности.
*Пример:*
[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
'''


def task2():
    lst = []
    size = random.randint(5, 15)
    for _ in range(size):
        lst.append(random.randint(0, 9))

    print(f'Исходная последовательность:\n{lst}')

    # result = []
    # for i in lst:
    #     if lst.count(i) == 1:
    #         result.append(i)

    result = [i for i in lst if lst.count(i) == 1]
    result = sorted(result)

    print(f'Cписок неповторяющихся элементов:\n{result}')
    # print(f'Ручная проверка:\n{sorted(lst)}')


# task2()
