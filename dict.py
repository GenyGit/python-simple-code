#Словари. Сделать функцию принимает на вход словарь и  два числа f(dict_name, key_name, value)
# каждый элемент словаря - список
#Если такой ключ уже есть, то значение добавить следующим элементом списка для этого ключа,
# если нет, то добавить значение к  ключу с номером key_name*2,
# если такой key_name*2 не существует, то создать и добавить
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key * 2 in d:
        d[key * 2].append(value)
    else:
        d[key * 2] = [value]
dic = {}
dic[10] = [4]
dic[5] = [2, 2, 2, 2]
dic[1] = [1]
print(dic)
update_dictionary(dic, 1, 17 )
update_dictionary(dic, 2, 'u17' )
update_dictionary(dic, 2, 'u17x2' )
update_dictionary(dic, 10, 'u10' )
for key, value in dic.items():
    print(key,' = ', value)
print(dic)
# решений с форума
#def update_dictionary(d, key, value):
#key += key * (key not in d)
#d[key] = d.key(key, []) + [value]


#еще одно
#def update_dictionary(d, key, value):
#    if key in d:
#        d[key] += [value]
#    elif key * 2 in d:
#        d[key * 2] += value
#    else:
#        d[key * 2] = [value]
#