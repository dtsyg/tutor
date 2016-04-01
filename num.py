import random

number = random.randrange(1, 10)
answer = int(input("введите предполагаемое число: "))
tries = 1

while answer != number:
	if answer > number:
		print("меньше!\n")
	else:
		print("больше!\n")
	answer = int(input("введите предполагаемое число: "))
	tries += 1

print("поздравляем! вы угадали число за ", tries, " попыток!")

input ("press enter-key to exit...")