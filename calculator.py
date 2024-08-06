import sys

try:
    symbol, num1, num2 = sys.argv[1], sys.argv[2], sys.argv[3]
except:
    print('error')
    sys.exit()

if (not num1.isdigit()) or (not num2.isdigit()):
    print('error')
    sys.exit()
else:
    num1, num2 = int(num1), int(num2)


def calc(symbol, num1, num2):
    if symbol == '+':
        result = num1 + num2
    elif symbol == '-':
        result = num1 - num2
    elif symbol == '*':
        result = num1 * num2
    elif symbol == '/':
        if num2 == 0:
            result = None
            return result
        result = num1 / num2
    elif symbol == '//':
        if num2 == 0:
            result = None
            return result
        result = num1 // num2
    elif symbol == '%':
        if num2 == 0:
            result = None
            return result
        result = num1 % num2
    else:
        result = None
        return result
    return result

if calc(symbol, num1, num2) == None:
    print('error')
else:
    print(calc(symbol, num1, num2))
