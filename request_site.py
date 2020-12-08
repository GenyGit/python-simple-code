#с помощью подключенного можуля обратиться к сайту и скачать файл, подсчитать количество строк в файле
import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/267.txt')
print(len(r.text.splitlines()))