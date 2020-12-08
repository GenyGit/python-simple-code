#ищеет наиболее часто встречаемое слово в тексте
countw = {}
tempmax = 0
tempmaxvalue = ''
with open('/home/user/usersmb/text.txt') as finp:
    for st in finp:
        print(st)
        stmas = [w.lower() for w in st.split()]
        for c in stmas:
            if c not in countw:
                countw[c] = 1
            else:
                countw[c] += 1
                if countw[c] > tempmax:
                    tempmax = countw[c]
                    tempmaxvalue = c
print(countw)
print(countw[tempmaxvalue],' ',tempmaxvalue)
print(tempmax,'',tempmaxvalue)



