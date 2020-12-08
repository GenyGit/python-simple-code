#На сервере лежит набор файлов. Известно имя первого файла.
# В каждом файле кроме полседнего содержиться имя следующего файла. Последний файл начинается со слова "We"
# Скачайте этот последний файл
import requests
cururl ='https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
wordwe = ''
while wordwe != 'We':
    r = requests.get(cururl)
    for line in r.text.splitlines():
        for w in line.split():
            wordwe = w
            cururl = 'https://stepic.org/media/attachments/course67/3.6.3/' + wordwe
            break
        break
print('----------------------------------------------------------------')
print(r.text)

#import requests
#name = '699991.txt'
#url = 'https://stepic.org/media/attachments/course67/3.6.3/'
#while 'We' not in name[:2]: перебираем по два символа строку
#    name = requests.get(url + name).text
#print(name)