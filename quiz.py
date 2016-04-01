"""
computer select random word,
give user a tips: number of letter in word;
user tryin' to guess that word,
user has a 5 tries to guess is there a letter in the word,
then he must have to guess the word
"""
import random

# parameterized main params
WORDS = ("one", "two", "three", "four", "five")
tries = 0
lett = ""		# letter @ for
user_lett = ""	# user input
word = "empty"	# user input
i = 0

# initialize quiz-word
correct = random.choice (WORDS)
num = len (correct)
print (correct)

print ("""
				HELLO, MY LITTLE DUMB FRIEND!

					welcome to quiz-game,
	  			  try to guess hidden word
u have 5 attempts to find out whether there is such letter in the word
	(press "Enter" (without ur version), if u want leave the game))

					
			in ur hidden word """, num, """ letters
						good luck (;

	""")

while word:
	user_lett = input ("\nplease input the estimated letter : ")
	for lett in correct:
		if user_lett != lett:
			i = 1
	if i == 1:
		print ("\nNOPE")
	else:
		print ("\nYEP")

word = input ("please input ur version of estimated word : ")

if word == correct:
	print ("""
		GRATZ!
	YOU'RE RIGHT!
		""")
else:
	print ("""
		SORRY,
but u're typicaly dumbass!
		""")



input("\npress any key to exit")
