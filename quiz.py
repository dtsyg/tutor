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
tries = 0		# hints
user_lett = None	# user input
word = "empty"	# user input

# initialize quiz-word
correct = random.choice (WORDS)
num = len (correct)
print (correct)

print ("""
				HELLO, MY LITTLE DUMB FRIEND!

					welcome to quiz-game,
	  			  try to guess hidden word
you have 5 attempts to find out whether there is such letter in the word
  if you don't want use a hint -- press "Enter" without your version,

			in your hidden word """, num, """ letters
						good luck (:

	""")

#letter validate
while tries < 5:
	user_lett = input ("\nplease input the estimated letter : ")
	if user_lett:
		if user_lett.lower() in correct:
			print ("\nYEP")
			tries += 1
		else:
			print ("\nNOPE")
			tries += 1
	else:
		break

word = input ("\nplease input your version of estimated word : ")

#word validate
if word:
    if word.lower() == correct:
        print ("""
            GRATZ!
        YOU'RE RIGHT!
            """)
    elif word.lower() != correct:
        print ("""
            SORRY,
    but you're typicaly dumbass!
            """)
else:
    print("""
      GOODBYE!
    """)

input("\npress any key to exit")
