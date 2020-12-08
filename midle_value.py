#читаем файл. формат файла фамилия_студента;оценка_физика;оценка_математика;оценка_рус_язык. (разделены данные - ";")
# вывести по каждому студенту среднюю оценку и  в конце среднюю по каждому предмету
import os
flout = open(os.path.join('/','home','user','usersmb','middle_val.txt'),'w')
with open('/home/user/usersmb/studvalue.txt') as studval:
    svm = 0.0
    svp = 0.0
    svr = 0.0
    countst = 0
    for line in studval:
        countst += 1 # считаем студентов
        rec = [b for b in line.strip().split(';')] #разбиваем строку на отдельные значения
        cs = 0 # среднее значение оценок для текущего студента
        cd = 0 # current discipline 1 - math, 2 - phis , 3 - rus lang
        for c in rec:
            if c.isnumeric():
                cs += float(c) #считаем сумму оценок текущего студента
            if cd == 1:
                svm += float(c) # сумма оценок по математике
            elif cd == 2:
                svp += float(c) # сумма оценок по физике
            elif cd == 3:
                svr += float(c) # сумма оценок по русскому языку
            cd += 1 # увеличиваем номер индекса в массиве
        outstr = str(cs / 3) + '\n'
        flout.write(str(outstr))
outstr = str(svm / countst) + ' ' + str(svp / countst) + ' ' + str(svr / countst)
flout.write(outstr)
flout.close()


#koll, a1, b1, c1 = 0, 0, 0, 0
#with open('dataset_3363_4.txt', 'r') as inf:
#    for line in inf:
#        line = line.strip().split(';')
#        a, b, c = int(line[1]), int(line[2]), int(line[3])
#        print((a+b+c)/3)
#        koll += 1
#        a1 += a
#        b1 += b
#        c1 += c
#print((a1/koll), (b1/koll), (c1/koll))

#st = [x.split(';') for x in open('fl.txt').readlines()]
#print(*[sum([int(y) for y in x[1:]])/3 for x in st], sep='\n')
#print(*[sum([int(y) for y in [st[x][z] for x in range(len(st))]])/len(st) for z in range(1,4)])
