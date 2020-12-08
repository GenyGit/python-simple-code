#расшифровка строки по ключу.
# сначала идет строка символов, потом  строка с кодом соответствия.
# За ними следуют еще две строки,
# первую ндо расшифровать, вторую зашифровать
#Пусть, например, на вход программе передано:
#abcd
#*d%#
#abacabadaba
##*%*d*%

#Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
#Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
#*d*%*d*#*d*
#dacabac

def dcf(stf, codedict):
    stoutf =''
    for j in stf:
        stoutf += codedict[j]
    return stoutf

code = {} #ключем является символ,значение шифр
decode = {} #ключем является шифр, значение - символ

simbolstr, codestr, needcode, needdecode = input(), input(), input(), input()
for c in range(len(simbolstr)):
    code[simbolstr[c]] = codestr[c]
    decode[codestr[c]] = simbolstr[c]
print(dcf(needcode, code))
print(dcf(needdecode, decode))


#a,b,c,d=input(),input(),input(),input()
#print(''.join(b[a.index(i)] for i in c))
#print(''.join(a[b.index(i)] for i in d))



# Считываем 4 строки в цикле
#original, coding, first_string, second_string = (input() for i in range(4))
# По индексу символа из оригинала берём символ на замену из кодировки,
# для каждого символа из строки, которую нужно закодировать
#print(*[coding[original.find(symbol)] for symbol in first_string], sep='')
# Аналогично, только наоборот :D
#print(*[original[coding.find(symbol)] for symbol in second_string], sep='')




#source, dest = input(), input()
#decoded = input()
#encoded = input()
#print(decoded.translate(str.maketrans(source, dest)))
#print(encoded.translate(str.maketrans(dest, source)))