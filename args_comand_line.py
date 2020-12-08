#программа запускается из командной строки и выводит список введенных аргументов
# нужно подключить модуль sys.argv
import sys
t = 0
for c in sys.argv:
    if t != 0:
        print(c)
    t = 1

#import sys
#print(*sys.argv[1:])

#import sys
#print(' '.join(sys.argv[1:]))

#import sys
#for i in range(1, len(sys.argv)):
#   print(sys.argv[i], end=' ')

#print(*__import__("sys").argv[1:])
#stepic pass geny@list.ru simple96sec
