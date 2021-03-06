#Последовательность n>0 n \gt 0 n>0 целых чисел называется jolly jumper в случае, если значения абсолютных разностей последовательных
# элементов принимают все возможные значения между 1 1 1 и n−1 n-1 n−1.
#
#Например, последовательность 1 -3 -4 -1 1 является jolly jumper последовательностью,
# так как абсолютные разности равны 4 1 3 2, соответственно, а n−1=4 n-1 = 4 n−1=4.
#Будем считать, что последовательность из одного числа является jolly jumper.
#
#Напишите программу, которая проверяет, является ли введённая последовательность jolly jumper.
#
#Формат ввода:
#
#Строка, содержащая 1≤n≤10000 1 \le n \le 10000 1≤n≤10000 целых чисел, разделённых пробелом.
#
#Формат вывода:
#Одна строка, содержащая "Jolly" (без кавычек), если последовательность является jolly jumper и "Not jolly" в противном случае.
#import math

a = list(map(int, input().split()))
n = set()
for i in range(len(a) - 1):
    t = a[i] - a[i + 1]
    if not(t.__abs__() in n):
        n.add(t.__abs__())
if len(a) == 1 or (1 in n) and len(n) == len(a) - 1:
    print("Jolly")
else:
    print("Not jolly")




print(a)
print(n)