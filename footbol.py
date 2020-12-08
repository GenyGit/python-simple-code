#программа считывает строки с результатами матчей
# сначала цифра N указывает количество завершенных игр
# потом идут сами результаты в формате имя_команды_1;количнство_забитых_голов1;имя_команды_2;vколичнство_забитых_голов2;
#начисление очков, победа 3, ничья 1, поражение 0
# на вывод идет следующий формат:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
# comands[] = [wins, draw, lose]
def compr(sf):
    if int(sf[1]) > int(sf[3]):
        rf = 1
    elif int(sf[1]) < int(sf[3]):
        rf = -1
    else:
        rf = 0
    return rf

def filldata(rf,sf,index):
    if sf[index] not in comands:
        comands[sf[index]] = [1, (rf + 1) // 2 , 1 - abs(rf), (1 - rf) // 2]
    else:
        comands[sf[index]] = [comands[sf[index]][0] + 1, comands[sf[index]][1] + (rf + 1) // 2, comands[sf[index]][2] + 1 - abs(rf), comands[sf[index]][3] + (1 - rf) // 2]
    return 0

N = int(input())
comands = {}
for i in range(N):
    st = input().split(';')
    res = compr(st)
    filldata(res,st,0)
    filldata(res * -1, st, 2)

for team, gameres in comands.items():
    print(team + ':',gameres[0], ' ', gameres[1], ' ',gameres[2], ' ', gameres[3],' ',(int(gameres[1]) * 3) + int(gameres[2]))
