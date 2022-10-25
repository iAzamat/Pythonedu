x = 0
y = 0


def r_div():
    return x / y


def r_mult():
    return x * y


def r_minus():
    return x - y


def r_sum():
    return x + y


def init(number1, number2):
    global x
    global y
    x = number1
    y = number2


def do_it(op):
    if op == "+":
        return r_sum()
    elif op == "-":
        return r_minus()
    elif op == "*":
        return r_mult()
    elif op == "/":
        return r_div()
