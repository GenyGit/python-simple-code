# находит содержиние символов в строке и выводит процентное соотношение ко всей строке
str = input().upper()
print(((str.count('C') + str.count('G')) * 100) / len(str))
