#вывод части таблицы умножения, первая пара чисел задают высоту квадрата, вторая пара ширину.
# Первая колонка диапазон введенных значений первой пары,  первая строка диапазон второй пары
a, b, y, z = int(input()),int(input()), int(input()), int(input())
fs = 0
print(end = '\t')
for i in range(a - 1 , b + 1):
    if fs != 0:
        print(i, end = '\t')
    for j in range(y, z + 1):
        if fs == 0:
            print(j, end = '\t')
        else:
            print(i*j, end='\t')
    print()
    fs = 1
