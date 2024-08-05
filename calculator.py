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
            print('error')
            sys.exit()
        result = num1 / num2
    elif symbol == '//':
        if num2 == 0:
            print('error')
            sys.exit()
        result = num1 // num2
    elif symbol == '%':
        if num2 == 0:
            print('error')
            sys.exit()
        result = num1 % num2
    else:
        print('error')
        sys.exit()
    return result


print(calc(symbol, num1, num2))
