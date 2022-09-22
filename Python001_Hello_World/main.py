# print("Hello World")


# # типы данных и переменная
# # int, float, boolean, str, list, None

# value = None
# # print(type(value))
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# value = 12334
# print(value)
# # print(type(value))
# s = 'hello \'world'
# print(s)  # вывод строки

# # способы вывода
# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')


# f = True
# print(f)
# f = False
# print(f)


# list = ['1', '2', '3']
# col = ['hello', 1, 2, 4, 5, True]
# print(list)
# print(col)


# Ввод и вывод данных
# print, input

# print('Введите a')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, '+', b, '=', a + b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')


# Арифметические операции
# +, -, *, /, %, //, **
# **, +, -, *, /, //, %, +, -
# (), Сокращённые операции

# деление в целых числах - //
# возведение в степень - **
# a = 1.31231223
# b = 3
# c = round(a * b, 7)
# print(c)

# a = 3
# a += 5
#
# print(a)

# логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 'qwe'
# b = 'qwe'
# a = [1, 2]
# b = [1, 2]
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 123
#
# print(func<T>(x))

# f = 1 > 2 or 4 < 6
#
# print(f)

# f = [1, 2, 3, 4]
# # print(f)
# # print(not 2 in f)
#
# is_odd = not f[0] % 2
# print(is_odd)

# if condition:
#     # operator 1
#     # operator 2
#     # ...
#     # operator n
# else:
#     # operator n + 1
#     # operator n + 2
#     # ...
#     # operator n + m

# username = input('Введите имя: ')
# if(username=='Маша'):
#     print('Ура, это же МАША!')
# else:
#     print('Привет, ', username)


# Управляющие конструкции
# if, if-else


# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)


# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина')
# elif username == 'Азамат':
#     print('Азамат - топ')
# else:
#     print('Привет, ', username)


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Управляющие конструкции:
# for

# list = [1, 2, 3, 4, 10, 5]
# for i in list:
#     print(i)


# for i in range(1, 10, 2):
#     print(i)

# for i in 'qwe - rty':
#     print(i)


# text = 'съешь ещё этих мягких французских булок'

# help(str)

# print(len(text))                    # 39
# print('ещё' in text)                # True
# print(text.isdigit())               # False
# print(text.islower())               # True
# print(text.replace('ещё', 'ЕЩЁ'))   # Замена
#
#
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])             # c
# print(text[1])             # ъ
# # print(text[len(text)])     # IndexError
# print(text[len(text)-1])   # к
# print(text[-5])            # б
# print(text[:])             # print(text)
# print(text[:2])             # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])           # ешь ещё
# print(text[6:-18])         # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6])           # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...
# print(text)

# Список - пронумерованная, изменяемая коллекция объектов произвольных типов

# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))
#
# print(numbers)  # [1, 2, 3, 4, 5]
#
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)  # [10, 2, 3, 4, 5]
#
# for i in numbers:
#     i *= 2
#     print(i)    # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]


# colors = ['red', 'green', 'blue']
#
# for e in colors:
#     print(e)        # red green blue
#
# for e in colors:
#     print(e*2)      # redred greengreen blueblue
#
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])    # True
# colors.remove('red')                                 # del colors[0] # удалить элемент
# del colors[0]


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))