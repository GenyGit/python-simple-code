#разархивирование строки и запись в файл.
# Архивированные данные представляют полседовательность символов и чисел
#символ должен повторится указанное числом раз  r2T5s1 --> rrTTTTTs
fl = open('/home/user/usersmb/dataset_3363_2.txt', 'r')
s = fl.readline().strip()
fl.close()
#s = 'g4t3d10K2'
a = s[0]
n = ''
sout = ''
for i in range(1, len(s)):
    #print('current simbol:', s[i])
    if s[i].isnumeric():
        n += s[i]
    else:
        #print(n)
        for j in range(int(n)):
            sout += a
        a = s[i]
        n = ''
        #print('a = ', a)
for j in range(int(n)):
    sout += a
print(sout)
outf = open('/home/user/usersmb/fout.txt', 'w')
outf.write(sout)
outf.close()


#s, d = input(), []
#for i in s:
#    if not i.isdigit(): d.append(i)
#    else: d[-1] += i
#print(*[i[0]*int(i[1:]) for i in d], sep='')



#m, s, n = '', '', 0
#with open('dataset_3363_2.txt', 'r+') as f:     # открываем файл в режиме чтения и запись
#    for i in f.readline():                      # читаем строку
#        if '0' <= i <= '9':                     # если цифра, соединяем в строку
#            n += i                              #
#            continue
#        m += s * int(n)                         # если символ, то повторяем его n-раз (если начало строки, то n=0 и ничего не запишет)
#        s, n = i, ''
#    f.seek(0)                                   # перемещаем указатель в начало
#    f.write(m)                                  # записываем строку в файл