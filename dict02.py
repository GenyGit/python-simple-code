#условие не совсем корректное. По сути надо запомнить n введеных данных,
# а потом с помощью их вызывать некую функцию (реализованан ранее)
def f(a): # функция условная, для тестирования
    print('----------------- in function -----------------')
    return int(a) + 1

n = int(input())
dic= {}
for i in range(n):
    x = input()
    if x not in dic:
        dic[x] = f(x)
    print(dic[x])
