#Дан файл с таблицей в формате TSV-
#Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
#Файл состоит из набора строк, каждая из которых представляет собой три поля:
#Класс Фамилия Рост
#Класс обозначается только числом. Буквенные модификаторы не используются. Н
# омер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число,
# но при подсчёте среднего требуется вычислить значение в виде вещественного числа.
#Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый).
# Если про какой-то класс нет информации, необходимо вывести напротив него прочерк

classmas = {}
with open('/home/user/usersmb/class.txt', 'r') as f:
    for line in f:
        line = line.strip().split()
        if line[0] not in classmas:
            classmas[line[0]] = [float(line[2]), int(1)]
        else:
            classmas[line[0]] = [classmas[line[0]][0] + float(line[2]), classmas[line[0]][1] + 1]
for i in range(1, 12):
    if classmas.get(str(i)):
        print(i, end = ' ')
        print(classmas.get(str(i))[0] /classmas.get(str(i))[1] )
    else:
        print(i, '-')


#d = {i: [] for i in range(1,12)}
#with open(r'D:\Новая папка\dataset_3380_5.txt','r', encoding='utf-8') as f1:
#  for i in f1:
#    d[int(i.split()[0])].append(float(i.split()[2]))
#
#for i in range(1,12):
#  if d[i]:
#    print(i, sum(d[i])/len(d[i]))
#  else:
#    print(i, '-')
