#подключение внешних модулей,
# в даном случае подключаем модуль math и используем значение числа пи из него

import math
pi = math.pi
r = float(input())
print(2 * pi * r)

#from math import tau подключаем  не весь модуль, а часть его, в частности tau - это 2pi
#print(float(input()) * tau)