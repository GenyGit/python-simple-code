#каждый объект в питоне идентифицируется по ID
# узнать ID можно через одноименную команду
l=[1,2,3]
d=l
print(id(l))
print(id(d))
print(id([1,2,3]))
l.append(4)

print(l is d)

print(id(l))
print(id(d))
print(id([1,2,3,4]))
print(id([1,2,3,4,5]))
print(id([1,2,3,4]))

