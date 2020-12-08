#дана последовательнотсть чисел одной строкой, во второй строке значение
# вывести все номера позиций последовательности равные этому значению
seq = [ int(i) for i in input().split()]
x = int(input())
if x not in seq:
    print("Отсутствует")
else:
    for i in range(len(seq)):
        if x == seq[i]:
            print(i, end = ' ')

