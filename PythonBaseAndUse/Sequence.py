#Напишите программу, которая выводит n  первых элементов последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно).
#Формат ввода:
#Строка, содержащая одно целое число n , n>0 n \gt 0 n>0.
#Формат вывода:
#Строка, содержащая требуемую последовательность чисел, разделённых пробелом.

#n = int(input())
count = 0
i = 0
lim = int(input())
while True:
    i += 1
    for j in range(i):
        print(i, end = " ")
        count +=1
        if  count == lim:
            exit()

#from forum
#n=int(input())
#print(*[x for x in range(1,(n+1)//2+1) for y in range(x)][:n])


