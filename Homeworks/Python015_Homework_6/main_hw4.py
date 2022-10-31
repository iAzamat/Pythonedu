import random
import json

'''
1. Вычислить число c заданной точностью d
Пример:
при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}
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
    number = float(protectinputnew(float, 'вещественное число'))
    accuracy = protectinputnew(float, 'требуемую точность вычислений "0.0001"')
    if 10 ** (-10) <= float(accuracy) <= 10 ** (-1):
        d = len(accuracy) - 2
        number_str = str(number)
        pospoint = number_str.find('.') + 1
        result = number_str[:pospoint + d]

        if (len(number_str) - pospoint) < d:
            res_buf = d - (len(number_str) - pospoint)
            result += '0' * res_buf
    else:
        print('Введите точность 10^(-10) ≤ d ≤ 10^(-1)')
        accuracy = protectinputnew(float, 'требуемую точность вычислений "0.0001"')

    print(result)


'''
2. Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.
'''


def protectinput(str_='число'):
    valid = False
    while not valid:
        num_ = input(f'Введите {str_}: ')
        try:
            num_ = int(num_)
        except:
            print('Некорректный ввод. Вы уверены, что ввели натуральное число?')
            continue
        if num_ > 0:
            valid = True
            return num_
        else:
            print('Некорректный ввод. Задайте натуральное число N')


def primemult(n):
    result = []
    temp_n = n

    for i in range(2, n):
        while not temp_n % i:
            result.append(i)
            temp_n = temp_n // i
    return result


def task2():
    n = protectinput()
    print(primemult(n))


'''
3. Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов 
исходной последовательности.
1 2 2 1 3 4 5 6 6 7 4 -> 3 5 7
'''


def original_numbers(new_list):
    result_list = []
    for val in new_list:
        if val not in result_list:
            result_list.append(val)
    result_list = sorted(result_list)
    return result_list


def task3():
    size = random.randint(5, 15)
    lst = [random.randint(0, 9) for _ in range(size)]
    print(f'Исходная последовательность:\n{lst}')
    print(f'Cписок неповторяющихся элементов:\n{set(lst)}\n')

    lst2 = [random.randint(0, 9) for _ in range(size)]
    print(lst2)
    print(original_numbers(lst2))


'''
4. Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
многочлена и записать в файл многочлен степени k.
Пример:
k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
k=9 => 2*x^9 - 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''


def polygenjson(num: int, filename='file'):
    polykoef = {k: random.randint(-100, 100) for k in reversed(range(num + 1))}
    with open(f'{filename}.json', 'w') as f:
        json.dump(polykoef, f)

    # print('Данные успешно записаны в файл')


def polygendisplay(filename='file'):
    with open(f'{filename}.json', 'r') as f:
        polykoef0 = json.load(f)

    polykoef2 = {k: polykoef0[str(k)] for k in reversed(range(len(polykoef0)))}

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
    with open(f'{filename1}.json', 'r') as f:
        polykoefb1 = json.load(f)

    with open(f'{filename2}.json', 'r') as f:
        polykoefb2 = json.load(f)

    polykoef1 = {k: polykoefb1[str(k)] for k in reversed(range(len(polykoefb1)))}
    polykoef2 = {k: polykoefb2[str(k)] for k in reversed(range(len(polykoefb2)))}

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
        json.dump(resultdict, f)


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
