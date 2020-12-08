#частотный анализ текста, для моноалфавитного шифрования Помогите расшифровать его письмо и понять, в каком же городе пройдет встреча:
#
#ФЙИ-ЭЕИ ЦСИЧМСО М ШДТЫСЮБШДС, ЩС ЦЙТЫЙМЖЙЬ ЖИПГА УЧБШДЙ. ЧЩ М ЩСЬ ЩСМЛЩШЦШЬ ЛШМШЮЙМШИ ЦШЬ Й М ЩСЬ ФС УАИПИ М ШДТЫСЮБШДС.
#
#Но, чтобы Шерлок не упустил ни одной детали, лучше расшифровать все сообщение.
# В ответ запишите всю фразу, оставляя все знаки препинания из шифртекста (дефисы, запятые, точки, пробелы).
#ответ:
# Жил-был человек в Амстердаме, не чистивший шляпу годами. Он в ней невзначай заваривал чай и в ней же гулял в Амстердаме.



#s = input()
s = "ФЙИ-ЭЕИ ЦСИЧМСО М ШДТЫСЮБШДС, ЩС ЦЙТЫЙМЖЙЬ ЖИПГА УЧБШДЙ. ЧЩ М ЩСЬ ЩСМЛЩШЦШЬ ЛШМШЮЙМШИ ЦШЬ Й М ЩСЬ ФС УАИПИ М ШДТЫСЮБШДС."
ds = dict()
countS = set()
for c in s:
    countS.add(c)
#print(countS)
for c in countS:
    ds[c] = 100*s.count(c) / len(s)
    #print(f"{c} - {100*s.count(c) / len(s)}%")
    #print(f"{c} - {ds[c]}")

print("------------------------")
ssorted_list = list(sorted(ds, key = ds.get, reverse=True)) #
#print(ssorted_list)
for k in ssorted_list:
   print(f"{k} - {ds[k]}")

#encryptlist7 = list("о","е","а","и","н","т","с")
encryptlist7 = list("оеаинтр")

#print(encryptlist7)
#print(len(encryptlist7))

cryptword = "ЦСИЧМСО"
varsencrypt = list()

#for i in range(len(cryptword)):
#    varsencrypt.append(list())

print(varsencrypt)

for c in cryptword.lower():
    #print("c -", c)
    nofind = True
    for ss in range(7):
        if c == ssorted_list[ss].lower():
            print(encryptlist7[(ss+1) % 7])
            varsencrypt.append(encryptlist7[(ss+1) % 7])
            nofind = False
            break
    if nofind:
        varsencrypt.append("?")

print(varsencrypt)





