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


def polygenjson(num: int):
    polykoef = {}
    for i in reversed(range(num + 1)):
        polykoef[i] = random.randint(-100, 100)
    with open('file.json', 'w') as f:
        json_polykoef = json.dump(polykoef, f)

    # print('Данные успешно записаны в файл')


def polygendisplay():
    polykoef2 = {}
    with open('file.json', 'r') as f:
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


def polygen(k):
    lst = []
    for i in range(k, -1, -1):
        randkoef = random.randint(0, 100)
        if randkoef != 0:
            if i == 0:
                # str1 = f'+{randkoef}' if randkoef > 0 else f'{randkoef}'
                str1 = f'+{randkoef}'
                lst.append(str1)
            elif i == 1:
                # str1 = f'+{randkoef}*x' if randkoef > 0 else f'{randkoef}*x'
                str1 = f'+{randkoef}*x'
                lst.append(str1)
            elif i == k:
                # str1 = f'{randkoef}*x^{i}'
                str1 = f'{randkoef}*x^{i}'
                lst.append(str1)
            else:
                # str1 = f'+{randkoef}*x^{i}' if randkoef > 0 else f'{randkoef}*x^{i}'
                str1 = f'+{randkoef}*x^{i}'
                lst.append(str1)
    lst.append('=0')
    return lst


def task5():
    lst1 = polygen(random.randint(2, 6))
    lst2 = polygen(random.randint(2, 6))

    with open('file1.txt', 'w') as data:
        for elem in lst1:
            data.write(elem)

    with open('file2.txt', 'w') as data:
        for elem in lst2:
            data.write(elem)

    with open('file1.txt', 'r') as data:
        str1 = data.read().replace('=0', '')
        str1 = str1.split('+')

    with open('file2.txt', 'r') as data:
        str2 = data.read().replace('=0', '')
        str2 = str2.split('+')

    print(f'Первый многочлен: {str1}')
    print(f'Второй многочлен: {str2}')

    for elem in range(len(str1)):
        if str1[elem].find('*x') == -1:
            str1[elem] = f'{str1[elem]}*x^0'

    for elem in range(len(str1)):
        if str1[elem].find('^') == -1 and str1[elem].find('*') != -1:
            str1[elem] = f'{str1[elem]}^1'

    for elem in range(len(str2)):
        if str2[elem].find('*x') == -1:
            str2[elem] = f'{str2[elem]}*x^0'

    for elem in range(len(str2)):
        if str2[elem].find('^') == -1 and str2[elem].find('*') != -1:
            str2[elem] = f'{str2[elem]}^1'

    # print(str1)
    # print(str2)

    str1_koef = {}
    for elem in str1:
        a1, b1 = elem.split('*x^')
        str1_koef[int(b1)] = int(a1)

    str2_koef = {}
    for elem in str2:
        a2, b2 = elem.split('*x^')
        str2_koef[int(b2)] = int(a2)

    # print(str1_koef)
    # print(str2_koef)

    a = (str1_koef, str2_koef)

    resultdict = {}

    for dictionary in a:
        for key in dictionary:
            try:
                resultdict[key] += dictionary[key]
            except KeyError:
                resultdict[key] = dictionary[key]

    resultdict = dict(sorted(resultdict.items(), reverse=True))
    # print(resultdict)

    reslst = []
    for el in range(len(resultdict) - 1, -1, -1):
        if el == 0:
            reslst.append(f'+{resultdict[el]}')
        elif el == 1:
            reslst.append(f'+{resultdict[el]}*x')
        elif el == len(resultdict) - 1:
            reslst.append(f'{resultdict[el]}*x^{el}')
        else:
            reslst.append(f'+{resultdict[el]}*x^{el}')
    reslst.append('=0')

    print(f'Результат: {reslst}')

    with open('file3.txt', 'w') as data:
        for elem in reslst:
            data.write(elem)

    print('Данные записаны в файл')


# task1()
# task2()
# task3()
# task4()
# task5()
