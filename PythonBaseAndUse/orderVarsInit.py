#Дана функция s﻿:
#def s(a, *vs, b=10):
#   res = a + b
#   for v in vs:
#       res += v
#   return res

#В результате каких вызовов данная функция вернет число 31?

def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res


print(s(11, 10, 10), 1)
print(s(11, 10, b=10), 2)
print(s(11, 10),3)
#print(s(b=31, 0), 4)
print(s(21),4)
print(s(11, b=20), 5)
print(s(b=31), 6)
print(s(0, 0, 31),7 )
print(s(5, 5, 5, 5, 1), 8)