#вывести повторяющиеся более одного раза  значения списка
rec = [int(i) for i in input().split()]
rec.sort()
u = 0
a = ''
for c in rec:
    if c == a:
        u += 1
    else:
        a = int(c)
        u = 0
    if u == 1:
        print(c, end = ' ')
