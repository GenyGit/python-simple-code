#дана  матрица, на основе ее сделать новую, где каждый член равен сумме соседей сверху и снизу
# для крайних членов соседи с противоположных концов
m1 = []
while True:
    a = [k for k in input().split()]
    if a[0] == 'end':
        break
    m1.append(a)
for i in range(len(m1)):
    for j in range (len(m1[i])):
        print(int(m1[i - 1][j]) + int(m1[i + 1 - len(m1)][j]) + int(m1[i][j - 1]) + int(m1[i][j + 1 - len(m1[i])]), end = ' ')
    print()
