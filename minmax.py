#три числа на вход, вывод сначала макс, потом мин, далее оставшееся
a, b, c = int(input()), int(input()), int(input())

if a > b :
    max = a
    min = b
else:
    max = b
    min = a

other = c

if c > max:
    other = max
    max = c
elif c < min:
    other = min
    min = c

print(max)
print(min)
print(other)
