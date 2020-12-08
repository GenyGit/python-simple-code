#Вычисляет количество различных объектов в списке
#Два объекта a и b считаются различными, если a is b равно False.
#Вашей программе доступна переменная с названием objects, которая ссылается на список,
# содержащий не более 100 объектов. Выведите количество различных объектов в этом списке.

objects = [4,5,8,4,5]
uni = set(objects)
print(len(uni))
uni.clear()
ans = 0
for obj in objects:
    if ( obj not in uni):
        uni.add(obj)
        ans += 1
print(ans)