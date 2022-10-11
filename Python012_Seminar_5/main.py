import random


def task1():
    # [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
    num = 8
    my_list = [1, 0, 1]
    for _ in range(1, num):
        print(my_list[0], my_list[1] - my_list[0])
        print(my_list[-1], my_list[-2] + my_list[-1])
        my_list.append(my_list[-2] + my_list[-1])
        my_list.insert(0, my_list[1] - my_list[0])


def task2():
    n = 8
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b


def pow(n, mult):
    '''
    Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая
    перемножается с mult, а n – положительное целое
    '''

    I = [[1, 0], [0, 1]]
    x = [[1, 1], [1, 0]]
    if n == 0:
        # print('Возвращается I, равна:', I)
        return I
    elif n == 1:
        # print('Возвращается Х, равен:', x)
        return x
    else:
        # print('n // 2, mult:', n // 2, I, mult)
        y = pow(n // 2, mult)
        # print('y = mult(y, y), y =', y)
        y = mult(y, y)
        if n % 2:
            # print('y = mult(x, y), x, y =', x, y)
            y = mult(x, y)
        # print('Возвращается y =', y)
        return y


def matrix_multiply(A, B):
    BT = list(zip(*B))
    # print('BT', BT)
    res = [[sum(a * b
                for a, b in zip(row_a, col_b))
            for col_b in BT]
           for row_a in A]
    # print('matrix_multiply=', res)
    return res


def task3():
    print(pow(8, matrix_multiply)[0][1])


def task4():
    lst = []
    size = random.randint(5, 15)
    for _ in range(size):
        lst.append(random.randint(0, 9))

    print(f'Исходная последовательность:\n{lst}')

    result = [i for i in lst if lst.count(i) == 1]
    result = sorted(result)

    print(f'Cписок неповторяющихся элементов:\n{result}')
    # print(f'Ручная проверка:\n{sorted(lst)}')

    # print(*result, sep='\n')

    # result2 = lst[:]
    # result2 = set(result2)
    # print(result2)


'''
3. Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов 
исходной последовательности.
1 2 2 1 3 4 5 6 6 7 4 -> 3 5 7
'''
from random import randrange


def original_numbers(new_list):
    result_list = []
    for val in new_list:
        if val not in result_list: result_list.append(val)
    result_list = sorted(result_list)
    return result_list


def task42():
    random_list = [randrange(1, 10) for _ in range(20)]
    print(random_list)
    print(original_numbers(random_list))

    # =============================

    print(random_list)
    random_list = set(random_list)
    print(random_list)


def task5():
    my_list = [34, 6547, 87, 345, 23, 765, 3]
    my_dict = {i: num for i, num in enumerate(my_list)}
    print(my_dict)


def task6():
    num = int(input("Введите натуральную степень k: "))

    def magit_to_file(num: int):
        str_1 = ""
        if num > 0:
            num1 = random.randint(0, 100)
            if num1 != 0:
                str_1 = f"{num1}*x^{num}"
            for i in reversed(range(2, num)):
                num1 = random.randint(0, 100)
                if num1 != 0:
                    str_1 += f" + {num1}*x^{i}"
            num1 = random.randint(0, 100)
            if num1 != 0:
                str_1 += f" + {num1}*x"
            num1 = random.randint(0, 100)
            if num1 != 0:
                print(f"{str_1} + {num1} = 0")
                with open('file.txt', 'w') as data:
                    print(f"{str_1} + {num1} = 0", file=data)
                print('Данные записаны в файл')
            else:
                print(f"{str_1} = 0")
                with open('file.txt', 'w') as data:
                    print(f"{str_1} = 0", file=data)
                print('Данные записаны в файл')

    magit_to_file(num)


'''
7. В файле находится N натуральных чисел, записанных через пробел. 
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
Найдите это число.
'''


def task7():
    missnumber = random.randint(2, 10)
    size = missnumber + random.randint(1, 5)
    str1 = ''
    for i in range(1, size + 1):
        if i < missnumber:
            str1 += f'{i} '
        if i > missnumber:
            str1 += f'{i} '

    with open('file.txt', 'w') as data:
        print(str1, file=data)

    with open('file.txt', 'r') as data:
        my_string = data.read()

    a = list(map(int, my_string.split()))
    for i in range(1, len(a)):
        if not a[i] - 1 == a[i - 1]:
            missnum = i + 1
    print(a)
    print(f'Не хватает числа: {missnum}')


'''
8. Дан список чисел. 
Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
Порядок элементов менять нельзя.
*Пример:*
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

'''


def new_list(my_string):
    if my_string[0] == max(my_string):
        return new_list(my_string[1:])

    else:
        myList = [my_string[0]]
        for i in range(1, len(my_string)):
            if myList[-1] < my_string[i]:
                myList.append(my_string[i])
        return myList


def task8():
    my_string_1 = [9, 1, 5, 2, 3, 4, 6, 1, 7]
    print(new_list(my_string_1))


'''
9. Напишите программу, удаляющую из текста все слова, содержащие "абв".
'''


def task9():
    text = 'съешь ещёабв этих мягабвких французских булок, да выпей чаю абв'
    my_list = list(filter(lambda x: 'абв' not in x, text.split()))
    print(' '.join(my_list))


# task1()
# task2()
# task3()
# task4()
# task42()
# task5()
# task6()
# task7()
# task8()
# task9()
