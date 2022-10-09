import random
from decimal import Decimal
import json

'''
1. Вычислить число c заданной точностью d
Пример:
при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''


def is_numbernew(tp, str1):
    try:
        tp(str1)
        return True
    except ValueError:
        return False


def protectinputnew(tp=float, str_='число'):
    num_ = input(f'Введите {str_}: ')
    while not is_numbernew(tp, num_):
        num_ = input(f'Введите {str_}: ')

    return num_


def task1():
    number = protectinputnew(float, 'вещественное число')
    accuracy = protectinputnew(float, 'требуемую точность вычислений "0.0001"')
    result = Decimal(number).quantize(Decimal(accuracy))
    print(result)


'''
2. Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.
'''


def is_number(str1):
    try:
        int(str1)
        return True
    except ValueError:
        return False


def protectinput(str_='число'):
    num_ = input(f'Введите {str_}: ')
    while not is_number(num_):
        num_ = input(f'Введите {str_}: ')

    return num_


def primemult(n):
    result = []
    temp_n = n

    for i in range(2, n):
        while not temp_n % i:
            result.append(i)
            temp_n = temp_n // i
    return result


def task2():
    n = int(protectinput())
    while n <= 0:
        n = int(protectinput())

    print(primemult(n))


'''
3. Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов 
исходной последовательности.
1 2 2 1 3 4 5 6 6 7 4 -> 3 5 7
'''


def task3():
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


'''
4. Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
многочлена и записать в файл многочлен степени k.
Пример:
k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
k=9 => 2*x^9 - 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''


def polygenjson(num: int, filename='file'):
    polykoef = {}
    for i in reversed(range(num + 1)):
        polykoef[i] = random.randint(-100, 100)
    with open(f'{filename}.json', 'w') as f:
        json_polykoef = json.dump(polykoef, f)

    # print('Данные успешно записаны в файл')


def polygendisplay(filename='file'):
    polykoef2 = {}
    with open(f'{filename}.json', 'r') as f:
        polykoef0 = json.load(f)

    for i in reversed(range(len(polykoef0))):
        polykoef2[i] = polykoef0[str(i)]

    str_1 = ""
    if polykoef2[len(polykoef2) - 1] != 0:
        str_1 = f"{polykoef2[len(polykoef2) - 1]}*x^{len(polykoef2) - 1}"
    for i in range(len(polykoef2) - 2, 1, -1):
        if polykoef2[i] != 0:
            znak = ' + ' if polykoef2[i] > 0 else ' - '
            str_1 += f"{znak}{abs(polykoef2[i])}*x^{i}"
    if polykoef2[1] != 0:
        znak = ' + ' if polykoef2[1] > 0 else ' - '
        str_1 += f"{znak}{abs(polykoef2[1])}*x"
    if polykoef2[0] != 0:
        znak = ' + ' if polykoef2[0] > 0 else ' - '
        str_1 += f"{znak}{abs(polykoef2[0])} = 0"
    else:
        str_1 += f" = 0"

    # print(polykoef2)
    print(str_1)


def task4():
    num = int(input("Введите натуральную степень k: "))
    polygenjson(num)
    polygendisplay()


'''
5. Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
5x^2 + 3x - 9
3x^2 - 2x - 5
8x^2 +1x - 14
'''


def polysum(filename1='file1', filename2='file2', fileresult='file3'):
    polykoef1 = {}
    polykoef2 = {}
    with open(f'{filename1}.json', 'r') as f:
        polykoefb1 = json.load(f)

    for i in reversed(range(len(polykoefb1))):
        polykoef1[i] = polykoefb1[str(i)]

    with open(f'{filename2}.json', 'r') as f:
        polykoefb2 = json.load(f)

    for i in reversed(range(len(polykoefb2))):
        polykoef2[i] = polykoefb2[str(i)]

    a = (polykoef1, polykoef2)

    resultdict = {}

    for dictionary in a:
        for key in dictionary:
            try:
                resultdict[key] += dictionary[key]
            except KeyError:
                resultdict[key] = dictionary[key]

    resultdict = dict(sorted(resultdict.items(), reverse=True))

    with open(f'{fileresult}.json', 'w') as f:
        json_polyresult = json.dump(resultdict, f)


def task5():
    k1 = random.randint(2, 6)
    k2 = random.randint(2, 6)
    polygenjson(k1, 'file1')
    polygenjson(k2, 'file2')

    polysum('file1', 'file2')

    polygendisplay('file1')
    polygendisplay('file2')
    polygendisplay('file3')


# task1()
# task2()
# task3()
# task4()
# task5()
