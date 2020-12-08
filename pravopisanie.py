#Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
#Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
#Попробуем написать подобную систему.
#На вход программе первой строкой передаётся количество d известных нам слов,
# после чего на d строках указываются эти слова.
# Затем передаётся количество l строк текста для проверки, после чего l строк текста.
#Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
d = int(input())
words = set()
mistake = set()
for i in range(d):
    words.add(input().lower())
print(words)
l = int(input())
for i in range(l):
    str = input().lower()
    print(str)
    for w in str.split():
        if w not in words:
            mistake.add(w)
for m in mistake:
    print(m)

#dic = {input().lower() for i in range(int(input()))}  генератор множества
#wrd = set()
#for w in range(int(input())):
#    wrd |= {i.lower() for i in input().split()}
#print(*wrd.difference(dic), sep="\n")

