#Расшифровывает шифр цезаря с переменным ключом

sent = input().lower()
#abc = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ы", "ъ", "э", "ю", "я"]
abc = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
key = 5
num = 0

for k in range(len(abc)):
    for c in sent:
        if c == " ":
            print(" ", end="")
        for i in range(len(abc)):
            if c == abc[i]:
                print(abc[(i - k) % len(abc)], end="")
    print(k)