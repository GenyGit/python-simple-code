# "архивирует строку" заменяет последовательность символов одним символом с указанием их числа
st = input()
stout = ''
i = 0
a = st[0]
for c in range(len(st)):
    if a == st[c]:
        i += 1
    else:
        stout += a + str(i)
        i = 1
        a = st[c]
stout += a + str(i)
print(stout)
