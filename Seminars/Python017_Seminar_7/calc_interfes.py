str_num_1 = ''
str_num_2 = ''
str_op = ''
complex = False


def init():
    global str_num_1
    global str_num_2
    global str_op
    global complex


def proverka_stroki(num):
    if 'i' in num:
        return True  # комплексные
    return False  # рациональные


def racional(num):
    num = float(num)
    return num


def complex_parser(num):
    num_1 = float(num[:num.index('+')].strip())
    num_2 = float(num[num.index('+') + 1:-1].strip())
    return num_1, num_2


def input_num():
    res_list = []
    str_num_1 = input("число1 = ")
    complex = complex_parser(str_num_1)
    res_list.append(complex)
    str_num_2 = input("число2 = ")
    complex = complex_parser(str_num_2)
    res_list.append(complex)
    str_op = input("введите знак для вычисления - ")
