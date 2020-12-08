#выводит сумму соседей каждого элемента списка,
# для крайних элементов одним из соседей считается другой крайний, если элемент один, то вывести только его
#питон сам зацикливает массивы а[-1] это последний элемент, a[-2] предпоследний
#rec = input().split()
rec = [1, 5, 6, 7, 2, 3]
if len(rec) > 1:
    print(int(rec[len(rec)-1]) + int(rec[1]), end = ' ')
    for i in range(1,len(rec)-1):
        print(int(rec[i - 1]) + int(rec[i + 1]), end = ' ')
    print(int(rec[len(rec)-2]) + int(rec[0]))
else:
    print(rec[0])

#второй вариант с отрицательными индексами
a = [int(j) for j in [1, 5, 6, 7, 2, 3] ]
for i in range(len(a)):
    print(a[i - 1] + a[i + 1 - len(a)], end = ' ')