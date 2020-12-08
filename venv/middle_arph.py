# среднне арифметическое диапазона чисел, которые делятся на 3
a, b = int(input()), int(input())
if a % 3 == 0:
    st = a
elif (a + 1) % 3 == 0:
    st = a + 1
else:
    st = a + 2
count3 = (b - st) // 3
print((2 * st + count3 * 3) / 2)
