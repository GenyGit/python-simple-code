#A durak deck contains 36 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S). Each card also has a value of either 6 through 10, jack, queen, king, or ace (denoted 6, 7, 8, 9, 10, J, Q, K, A). For scoring purposes card values are ordered as above, with 6 having the lowest and ace the highest value.
#
#Напишите программу, которая определяет, бьёт ли одна карта другую.
#Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
#Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
#Если карты разных мастей и нет козырных, то никто не побеждает.
#
#Формат ввода:
#На первой строке через пробел указываются две карты в формате <значение><масть>, а на следующей строке указывается козырная масть.
#
#Формат вывода:
#Программа должна вывести слово
#First, если первая карта бьёт вторую,
#Second, если вторая карта бьёт первую,
#Error, если ни одна из карт не может побить другую.

def compcardval(ffc,fsc):
    if ffc > fsc:
        print("First")
        return
    if ffc < fsc:
        print("Second")
    else:
        print("Error")

cardValue={'6': 0,'7': 1,'8': 2,'9': 3,'10': 4,'J': 5,'Q':6,'K':7,'A':8}
#fc, sc = input().split(" ")
#kzr = input()
fc, sc, kzr = "AD", "KS", "S"
if fc[-1] == kzr:
    if sc[-1] == kzr:
        compcardval(cardValue[fc[0:-1]], cardValue[sc[0:-1]])
    else:
        print("First")
else:
    if sc[-1] == kzr:
        print("Second")
    else:
        if fc[-1] == sc[-1]:
            compcardval(cardValue[fc[0:-1]], cardValue[sc[0:-1]])
        else:
            print("Error")

#from forum
#(c1, c2), m = input().replace('10', 'T', 2).split(), input() считываем значения, 10 заменяем на Т
#r1 = (c1[1] == m, '6789TJQKA'.find(c1[0]) * (c1[1] == c2[1])) сравниваем с козырем первую карту, а также  высчитываем величину карты
# (номер индекса в списке ) если масти одинаковые. Если масти разные, то умножаем величину на 0, в этом случае будет расматриваться только козырь или нет
#r2 = (c2[1] == m, '6789TJQKA'.find(c2[0]) * (c1[1] == c2[1]))
#ans = 0 if r1 > r2 else 1 if r1 < r2 else 2 получаем значение 0 если первая карта больше, 1 если вторая и 0 если неопределено
#print(['First', 'Second', 'Error'][ans]) выводим элемент по полученому номеру









