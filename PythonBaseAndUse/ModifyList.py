#Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
#
#lst = [1, 2, 3, 4, 5, 6]
#print(modify_list(lst))  # None
#print(lst)               # [1, 2, 3]
#modify_list(lst)
#print(lst)               # [1]
#
#lst = [10, 5, 8, 3]
#modify_list(lst)
#print(lst)               # [5, 4]
#
#Также функция не должна осуществлять ввод/вывод информации.

def modify_list(l):
    i=0
    lenl = len(l)
    while i<lenl:
        if l[i] % 2 == 0:
            l[i] //= 2
            i +=1
        else:
            l.pop(i)
            lenl -=1

lst = [1, 2, 3, 4, 5]
print(lst)
modify_list(lst)
print("finish: ",lst)
# from forum
#def modify_list(numbers):
#    numbers[:] = [i//2 for i in numbers if i%2 == 0]
#    краткая запись генератора списка  lst = [ fun(i) for i in range(10) if i > 5]
#                                   сделать что-то
#                                                   с перечнем элементов
#                                                                      при выполнении условия
# если просто использовать присвоение lst1 = lst2, то создастся новый объект lst1,
# и в случае если это происходит внутри функции, изменения внешнего объекта не произойдет
# lst[2:8] означает присвоить значения элементам со второго по седьмой
# lst[:] =        - заменить  все элементы списка