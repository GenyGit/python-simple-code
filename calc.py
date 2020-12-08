#calculator
x=float(input())
y=float(input())
oper=input()

if oper == '+':
    print(x + y)
elif oper == '-':
    print(x - y)
elif oper == '*':
    print(x * y)
elif oper=='pow':
    print(x ** y)

elif y == 0.0:
        print('Деление на 0!')

elif oper == '/':
    print(x / y)
elif oper == 'mod':
    print(x % y)
elif oper == 'div':
    print(x // y)





