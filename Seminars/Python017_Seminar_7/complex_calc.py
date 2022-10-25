x = [0, 0]
y = [0, 0]


def c_sum():
    a = x[0]  # для красоты и понимания
    b = x[1]
    c = y[0]
    d = y[1]
    re = a + c
    im = b + d
    return [re, im]


def c_minus():
    a = x[0]  # для красоты и понимания
    b = x[1]
    c = y[0]
    d = y[1]
    re = a - c
    im = b - d
    return [re, im]


def c_mult():
    a = x[0]  # для красоты и понимания
    b = x[1]
    c = y[0]
    d = y[1]
    re = a * c - b * d
    im = b * c + a * d
    return [re, im]


def c_div():
    a = x[0]  # для красоты и понимания
    b = x[1]
    c = y[0]
    d = y[1]
    re = (a * c + b * d) / (c ** 2 + d ** 2)
    im = (b * c - a * d) / (c ** 2 + d ** 2)
    return [re, im]


def init(compnumb1, compnumb2):
    global x
    global y
    x = compnumb1
    y = compnumb2


def do_it(op):
    if op == "+":
        return c_sum()
    elif op == "-":
        return c_minus()
    elif op == "*":
        return c_mult()
    elif op == "/":
        return c_div()
