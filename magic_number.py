# программа "угадай число", но с ограниченным количеством попыток
# программа рандомно выкидывает число от 1 до 100, пользователь угадать
# попыток будет 10

import random

# number -- отдает программа
# answer -- вводит пользователь

print('''
	ДОБРО ПОЖАЛОВАТЬ В ИГРУ "УГАДАЙ" ЧИСЛО
	    ИГРА ЗАГАДАЛА ЧИСЛО ОТ 1 ДО 100
	   	   ПОПРОБУЙТЕ ЕГО УГАДАТЬ
			 У ВАС 10 ПОПЫТОК
	''')

number = random.randrange(10) + 1
answer = int(input("введите предполагаемое число: "))
tries = 1

while answer != number and tries < 5:
	if answer > number:
		print("меньше!\n")
	else:
		print("больше!\n")
	answer = int(input("введите предполагаемое число: "))
	tries += 1

if answer != number:
	print ('''
					извините, у Вас кончились попытки''')
else:
	print ('''
				поздравляем, Вы угадали!
			    Вам понадобилось попыток -- ''', tries)

input ("press enter-key to exit...")