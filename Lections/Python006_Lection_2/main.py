# ======================================================
#             Файлы
# ======================================================

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
# data.writelines(colors)  # разделителей не будет
data.write('Line 1\n')
data.write('Line 2\n')
data.close()

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()


# ======================================================
#             Функции и модули
# ======================================================


# import hello as h

# print(h.f(1))

def new_string(symbol, count=3):
    return symbol * count


print(new_string('!', 5))  # !!!!!
print(new_string('!'))  # !!!
print(new_string(4))  # 12


def concatenatio(*params):
    res: str = ''
    for item in params:
        res += item
    return res


print(concatenatio('a', 's', 'd', 'w'))  # asdw
print(concatenatio('a', '1', 'd', '2'))  # a1d2


# print(concatenatio(1, 2, 3, 4))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)  # 1 1 2 3 5 8 13 21 34

# ======================================================
#             Кортежи
# ======================================================

a = (3, 4, 5)
a = (3,)
print(a)
print(a[0])

for item in a:
    print(item)

t = tuple(['red', 'green', 'blue'])
print(t[0])  # red
print(t[2])  # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2])  # green
# print(t[-200]) # IndexError: tuple index out of range

for e in t:
    print(e)  # red green blue

# t[0] = 'black'  # TypeError: 'tuple' object does not support item assigment


t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))
# r: red g: green b: blue

# ======================================================
#             Словари
# ======================================================

dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }

print(dictionary)  # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary['left'])  # ←
# типы ключей могут отличаться


for k in dictionary.keys():
    for k in dictionary.values():
        print(k)

for v in dictionary:
    print(dictionary[v])

for k in dictionary:
    print(k)

print(dictionary['up'])  # типы ключей могут отличться

dictionary['left'] = '←'
print(dictionary['left'])  # ←
# print(dictionary['type'])  # KeyError: 'type'
del dictionary['left']  # удаление элемента

for item in dictionary:  # for (k, v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# ======================================================
#             Множества
# ======================================================

colors = {'red', 'green', 'blue'}

print(colors)  # {'red', 'green', 'blue'}
colors.add('red')
print(colors)  # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)  # {'green', 'gray', 'blue', 'red'}
colors.remove('red')
print(colors)  # {'green', 'blue', 'gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red')  # ok
print(colors)  # {'blue', 'gray', 'green'}
colors.clear()
print(colors)  # set()

# ======================================================
#             Множества
# ======================================================

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()  # c = {1, 2, 3, 5, 8}
print(c)
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}
print(u)
i = a.intersection(b)  # i = {8, 2, 5}
print(i)
dl = a.difference(b)  # dl = {1, 3}
print(dl)
dr = b.difference(a)  # dr = {13, 21}
print(dr)

q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}
print(q)

s = frozenset(a)

# ======================================================
#             Списки
# ======================================================

list1 = [1, 2, 3, 4, 5]
list2 = list1

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

print(list1)
print(list1.pop())
print(list1)
print(list1.pop())
print(list1)
print(list1.pop())
print(list1)

# print(list1.pop(2))
print(list1)
print(list1.insert(2, 11))
print(list1)
print(list1.append(11))
print(list1)
