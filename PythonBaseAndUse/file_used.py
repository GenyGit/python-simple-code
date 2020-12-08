#Прочитайте содержимое файла file.txt, содержащий 3 строки:
#    имя файла с текстом
#   имя файла, куда необходимо дозаписать ответ (сохранив начало файла)
#    номер строки (из файла с текстом), которую надо привести к нижнему регистру и дозаписать в файл ответа
#Строки, как и элементы массива, нумеруются с 0.

#mport io
with open('/home/user/stepik/pyfile/commands.txt') as commands:
    comline=commands.readlines()
commands.close()

with open(comline[0].strip()) as infile:
    instr = infile.readlines()
outstr = instr[int(comline[2].strip())-1].lower()
infile.close()

outfile=open(comline[1].strip(),'a')
outfile.write(outstr)
outfile.close()



