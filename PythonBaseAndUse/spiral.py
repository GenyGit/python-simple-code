dimen = int(input()) #  размер стороны
startx = 0 # начало движения следующего отрезка пути
starty = 0 #начало движения следующего отрезка пути
step = 0 #   текущий шаг
dist = dimen #длина текущего отрезка
mres = [[0 for j in range(dimen)] for i in range(dimen)]  # запись результата
pathn = 0 # номер "поворота", с каждым вторым поворотом длина пути сокращается
while step != dimen ** 2:
    kx = pow(-1,((pathn // 2) % 2)) * ((pathn + 1) % 2) # коэффициент движения по х
    ky = pow(-1,((pathn // 2) % 2)) * ((pathn) % 2) # коэффициент движения по y
    pathn += 1
    for i in range(dist):
        step += 1
        n = startx + i*kx # в зависимости от значения коэфф. увеличиваются или уменьшаются
        m = starty + i*ky # соответсвующие индексы
        mres[n][m] = step #запись в массив номера текущего шага
    startx = n + ky*(-1)
    starty = m + kx
    dist -= 1 * (pathn % 2)

for i in range(dimen):
    for j in range(dimen):
        print(mres[j][i], end = '\t')
    print()