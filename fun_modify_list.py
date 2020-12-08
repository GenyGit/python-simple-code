#функция должна модифицировать список, ничего не передает и не выводит на экран
def modify_list(l):
    n = len(l)
    i = 0
    while i != n:
        #print('i : l : n ', i, l[i], n)
        if l[i] % 2 != 0:
            l.remove(l[i])
            #print(l)
            i -= 1
            n -= 1
        else:
            l[i] = l[i] // 2
        i += 1
#решение с форума в одну строчку !!!!!!!!!!!!!!!!!!!!!!!!!!!!
#def modify_list(l):
#   l[:] = [i // 2 for i in l if not i % 2] - генерируем новый список с условием, конструкция l[:] - называется срезом списка - надо читать



lst = [int(i) for i in input().split()]
modify_list(lst)
for c in lst:
    print(c, end = ' ')