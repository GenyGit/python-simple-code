#высчитывает площадь указанной фигуры
figure=input()

if figure == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c ) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)

elif figure == 'прямоугольник':
    a = float(input())
    b = float(input())
    S = a * b
    print(S)

elif figure == 'круг':
    a = float(input())
    S = 3.14 * a ** 2
    print(S)
