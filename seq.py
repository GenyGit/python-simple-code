#на вход получаем число, которое определяет количество элементов последовательности
#которые необходимо вывести на печать. Последовательность определяется правилом:
#каждое число повторяется столько раз, чему оно равно 1 2 2 3 3 3 4 4 4 4 и т.д.
n = int(input())
m = 0
while True:
    m += 1
    for i in range(m):
        if n != 0:
            print(m, end = ' ')
            n -= 1
        else:
            exit(0)
