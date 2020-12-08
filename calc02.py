#Напишите простой интерпретатор математического выражения.
#На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором:
# a operator b a \texttt{ operator } b a operator b,
# где вместо operator \texttt{operator} operator могут использоваться следующие слова: plus, minus, multiply, divide для,
# соответственно, сложения, вычитания, умножения и целочисленного деления.

a, o, b = input().split(" ")
if o == "plus":
    print(int(a) + int(b))
elif o == "minus":
    print(int(a) - int(b))
elif o == "multiply":
    print(int(a) * int(b))
elif o=="divide":
    print(int(a) // int(b))
