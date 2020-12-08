#Напишите программу, которая принимает на вход список целых чисел и выводит на экран значения, которые повторяются в нём более одного раза.
#
#Для решения задачи может пригодиться метод sort списка.
#
#Формат ввода:
#Одна строка с целыми числами, разделёнными пробелом.
#
#Формат вывода:
#Строка, содержащая числа, разделённые пробелом. Числа не должны повторяться, порядок вывода может быть произвольным.

m = list(map(int, input().split()))
n = set()
u = set()
for i in m:
    if i in u:
        n.add(i)
    else:
        u.add(i)
for i in n:
    print(i, end = " ")

#Может кому пригодится.Я создал файл с 1 млн значений.
#Затем считывал значения в лист lst.
#С помощью time() замерял время обработки разными методами.\
#Прикладываю код и время:
#
#print(*[e for e in set(lst) if lst.count(e) > 1])
#
#Время: не дождался)
#
#
#
#d = dict()
#for i in lst:
#    if i in d:
#d[i] += 1
#else:
#d[i] = 1
#for i in d:
#    if
#d[i] > 1:
#print(i, end=' ')

#Время: 3.2439730167388916
#
#lst = sorted(lst)

#for i, j in groupby(lst):
#    if
#len(list(j)) > 1:
#print(i, end=' ')
#
#Время: 7.661556005477905
#
#res = Counter(lst)
#for it in res.keys():
#    if res[it] > 1: print(it, end=' ')
#
#Время: 3.404210090637207

#lst.sort()
#for i in range(1, len(lst) - 1):
#    if
#lst[i] != lst[i + 1] and lst[i] != lst[i - 1]:
#lst[i] = None
#lst[0], lst[-1] = None, None
#print(*[lst[x] for x in range(1, len(lst)) if (lst[x] is not None and lst[x] != lst[x - 1])])
#
#Время: 6.667062997817993

#Отсюда вывод: Словари и Counter лучше всего подходят для этой задачи.