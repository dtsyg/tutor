'''
программа тянет 1 из 5 печений с предсказаниями,
читает предсказание, повторяет по желанию пользователя
'''

print('''\n			ДОБРО ПОЖАЛОВАТЬ В ПРОГРАММУ "ПЕЕЕЧЕНЬКА С ПРЕДСКАЗАНИЕМ"\n\n''')
print('''					КРУТИТЕ БАРАБАН РЕВОЛЬВЕРА\n''')

import random

response = "y"
COOKIES = ("завтра вы не проснётесь", "вы не достигнете успеха", "вас ждут разачарования",
			"вы не станете занименитым", "у вас найдут рак")

while response != "n":
	if response == "y":
		coo = random.choice (COOKIES)
		print('''печенина предсказывает Вам: ''', coo)
		response = input("\nВы хотите продолжить? (y/n) ")
		print("\n\n")
	elif response == "n":
		pass
	else:
		response = input ("\nвведите валидный ответ -- 'y(yes)' или 'n(no)': ")
		print ("\n")

input("\npress Enter-key to exit...")