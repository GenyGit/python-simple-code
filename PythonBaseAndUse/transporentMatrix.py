#Напишите программу, которая принимает на вход матрицу, выполняет её транспонирование и выводит результат.
#
#Формат ввода:
#В первой строке указываются два целых числа n n n и m m m, количество строк и столбцов, соответственно.
#Далее следуют n n n строк, содержащих по m m m целых чисел, разделённых пробелом.
#
#Формат вывода:
#Программа должна вывести m m m строк содержимого транспонированной матрицы. Элементы матрицы стоит разделять пробелом.

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(m):
    for j in range(n):
        print(a[j][i], end=" ")
    print()


#n, m = map(int, input().split())
#for t in zip(*[input().split() for _ in range(n)]):
#    print(*t)

#n, m = list(map(int, input().split()))
#list(map(print, *(input().split() for q in range(n))))
