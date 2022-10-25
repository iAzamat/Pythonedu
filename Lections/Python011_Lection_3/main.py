def task0():
    def f(x):
        return x ** 2

    g = f
    print(f(1))
    print(g(1))
    # print(type(f))


def task1():
    def calc1(x):
        return x + 10

    # print(calc1(10))

    def calc2(x):
        return x * 10

    # print(calc2(10))

    def math(op, x):
        print(op(x))

    math(calc2, 10)
    math(calc1, 10)


def task2():
    # def sum(x, y):
    #     return x + y

    # sum = lambda x, y: x + y

    def mult(x, y):
        return x * y

    def calc(op, a, b):
        print(op(a, b))
        # return op(a, b)

    calc(lambda x, y: x + y, 4, 5)


# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

def task3():
    lst = []

    for i in range(1, 101):
        if (i % 2 == 0):
            lst.append(i)

    print(lst)


def task4():
    # lst = []
    #
    # for i in range(1, 101):
    #     lst.append(i)
    #
    # print(lst)

    def f(x):
        return x ** 3

    # lst = [i for i in range(1, 101) if i % 2 == 0]
    # lst = [(i, i) for i in range(1, 101) if i % 2 == 0]
    lst = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
    print(lst)


'''
В файле хранятся числа, нужно выбрать четные и составить сисок пар (число; квадрат числа).
Пример:
1 2 3 5 8 15 23 38
Получить:
[(2, 4), (8, 64), (38, 1444)]
'''


def task5():
    # path = 'data.txt'
    # f = open(path, 'r')
    # data = f.read() + ' '
    # f.close()

    path = 'data.txt'
    with open(path, 'r') as f:
        data = f.read() + ' '

    numbers = []

    while data != '':
        space_pos = data.index(' ')
        numbers.append(int(data[:space_pos]))
        data = data[space_pos + 1:]

    out = []
    for e in numbers:
        if not e % 2:
            out.append((e, e ** 2))
    print(out)


def task6():
    def select(f, col):
        return [f(x) for x in col]

    def where(f, col):
        return [x for x in col if f(x)]

    data = '1 2 3 5 8 15 23 38'.split()

    res = select(int, data)
    res = where(lambda x: not x % 2, res)
    res = select(lambda x: (x, x ** 2), res)
    print(res)


def task7():
    li = [x for x in range(1, 20)]

    li = list(map(lambda x: x + 10, li))

    print(li)


def task8():
    # data = list(map(int, input().split()))
    # print(data)
    #
    # for e in data:
    #     print(e)

    data = list(map(int, '1 2 3'.split()))

    for e in data:
        print(e)

    print('--')

    for e in data:
        print(e)


def task9():
    # def select(f, col):
    #     return [f(x) for x in col]

    # def where(f, col):
    #     return [x for x in col if f(x)]

    data = '1 2 3 5 8 15 23 38'.split()

    res = map(int, data)
    res = filter(lambda x: not x % 2, res)
    res = list(map(lambda x: (x, x ** 2), res))
    print(res)

    # data = [x for x in range(10)]
    #
    # res = list(filter(lambda x: not x % 2, data))
    # print(res)


def task10():
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    ids = [4, 5, 9, 14, 7]
    salary = [111, 222, 333]

    data = list(zip(users, ids, salary))
    print(data)


def task11():
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    ids = [4, 5, 9, 14, 7]
    salary = [111, 222, 333]

    data = list(enumerate(users))
    print(data)


task0()
task1()
task2()
task3()
task4()
task5()
task6()
task7()
task8()
task9()
task10()
task11()
