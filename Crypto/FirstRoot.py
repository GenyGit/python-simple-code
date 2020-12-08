#Нахождение первобразного корня
#g^f(m) = 1 mod m

m, f = int(input()), int(input())
for g in range(2, m):
    for k in range(1, f + 1):
        r = g ** k % m
        if r == 1:
            if k!=f:
                print(g, ": fail in k =", k)
                break
            else:
                print(g, "<---- is a first root!!!")

