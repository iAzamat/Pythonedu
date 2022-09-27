import math

'''
1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
'''


def task1():
    def protectinput():
        while True:
            num_ = input('Введите день недели (1 - 7): ')
            if not num_.isdigit():
                print("Вы должны ввести число от 1 до 7. Попробуйте еще раз")
            else:
                number_ = int(num_)
                if 0 < number_ < 8:
                    return number_
                    break
                else:
                    print("Вы должны ввести число от 1 до 7. Попробуйте еще раз")

    number = protectinput()
    if 0 < number < 6:
        print('Нет')
    else:
        print('Да')


'''
2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''


def task2():
    my_list = [0, 1]
    for x in my_list:
        for y in my_list:
            for z in my_list:
                res1 = (not (x or y or z))
                res2 = ((not x)) and (not y) and (not z)
                res = (res1 is res2)
                print(f'{x}\t{y}\t{z}\t{res1}\t{res2}\t{res}')


'''
3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def protectinput():
    while True:
        coords = (input('Введите координаты x и y через пробел: ').split())
        if (len(coords) != 2) or (not is_number(coords[0]) or not is_number(coords[1])):
            print("Было введено не число или неверное количество элементов. Попробуйте еще раз")
        else:
            x_ = int(coords[0])
            y_ = int(coords[1])
            print(f'Были введены координаты точки ({x_}, {y_})')
            return x_, y_
            break


def task3():
    x, y = protectinput()
    if y > 0:
        if x > 0:
            print(f'Точка с координатами ({x}, {y}) лежит в 1 четверти')
        else:
            print(f'Точка с координатами ({x}, {y}) лежит во 2 четверти')
    else:
        if x > 0:
            print(f'Точка с координатами ({x}, {y}) лежит в 4 четверти')
        else:
            print(f'Точка с координатами ({x}, {y}) лежит в 3 четверти')


'''
4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
'''


def task4():
    def protectinput():
        while True:
            num_ = input('Введите номер четверти (1 - 4): ')
            if not num_.isdigit():
                print("Вы должны ввести число от 1 до 4. Попробуйте еще раз")
            else:
                number_ = int(num_)
                if 0 < number_ < 5:
                    return number_
                    break
                else:
                    print("Вы должны ввести число от 1 до 4. Попробуйте еще раз")

    quarter_number = protectinput()
    if quarter_number == 1:
        print('В первой четверти: x ∈ (0, ∞) и y ∈ (0, ∞)')
    elif quarter_number == 2:
        print('Во второй четверти: x ∈ (-∞, 0) и y ∈ (0, ∞)')
    elif quarter_number == 3:
        print('В третьей четверти: x ∈ (-∞, 0) и y ∈ (-∞, 0)')
    elif quarter_number == 4:
        print('В четвертой четверти: x ∈ (0, ∞) и y ∈ (-∞, 0)')


'''
5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''


def task5():
    x1, y1 = protectinput()
    x2, y2 = protectinput()
    print(f'Первая точка с координатами ({x1}, {y1})\nВторая точка с координатами ({x2}, {y2})')
    res = math.pow(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2), 0.5)
    result = math.trunc(100 * res) / 100  # округление до 2 символов
    print((f'Расстояние между точками {result}'))

# task1()
# task2()
# task3()
# task4()
# task5()
