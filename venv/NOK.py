#нахождение наименьшего общего кратного через нахождение наибольшего общего делителя
a = int(input())
b = int(input())

if a  > b :
    n = a
    m = b
else:
    n = b
    m = a

while  n % m != 0 :
    ost = n % m
    n = m
    m = ost

print(a * b // m)