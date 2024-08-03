import sys

try:
    symbol, x, y = sys.argv[1], sys.argv[2], sys.argv[3]
except:
    print('error')
    sys.exit()

if (not x.isdigit()) or (not y.isdigit()):
    print('error')
    sys.exit()
else:
    x, y = int(x), int(y)


def calc(symbol, x, y):
    if symbol == '+':
        return print(x + y)
    elif symbol == '-':
        return print(x - y)
    elif symbol == '*':
        return print(x * y)
    elif symbol == '/':
        if y == 0:
            return print("error")
        return print(x / y)
    elif symbol == '//':
        if y == 0:
            return print("error")
        return print(x // y)
    elif symbol == '%':
        if y == 0:
            return print("error")
        return print(x % y)
    else:
        return print("error")


calc(symbol, x, y)
