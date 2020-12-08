#Поле для игры сапёр представляет собой сетку размером n×m n \times m n×m.
# В ячейке сетки может находиться или отсутствовать мина.
#
#Напишите программу, которая выводит "решённое" поле,
# т.е. для каждой ячейки, не являющейся миной, указывается число мин,
# находящихся в соседних ячейках (учитывая диагональные направления)
#
#Формат ввода:
#На первой строке указываются два натуральных числа 1≤n,m≤100 1 \le n,m \le 100 1≤n,m≤100,
# после чего в n n n строках содержится описание поля в виде последовательности точек '.' и звёздочек '*',
# где точка означает пустую ячейку, а звёздочка − ячейку с миной.
#
#Формат вывода:
#n n n строк поля, в каждой ячейке которого будет либо число от 0 до 8,
# либо мина (обозначенная символом "*"), при этом число означает количество мин в соседних ячейках поля.

def rangefield(sn,sm,cn,cm):
    if 0 <= cn < sn and 0 <=cm < sm:
        return True
    else:
        return False

def area(sn, sm, cn, cm):
    summine = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            x = cn + i
            y = cm + j
            if rangefield(sn, sm, x, y):
                #print(fieldin[x][y], end=" ")
                if fieldin[x][y] == "*":
                    summine += 1
        #print()
    #print()
    return summine

n, m = input().split(" ")
#print(n)
#print(m)
fieldin = []
fieldout = []
for i in range(int(n)):
    fieldin.append([])
    fieldin[i] = list(input())

for i in range(int(n)):
    fieldout.append([])
    for j in range(int(m)):
        if fieldin[i][j] == "*":
            fieldout[i].append(fieldin[i][j])
        else:
            fieldout[i].append(area(int(n), int(m), i, j))
        print(fieldout[i][j], end=" ")


#        print(rangefield(int(n),int(m),i+1,j-1), end="=")
#        print(fieldin[i][j], end=" ")
    print()










