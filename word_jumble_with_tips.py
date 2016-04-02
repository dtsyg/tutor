"""
words jumble with tips (hints)
user gets the anagram and tries to restore word
if user can't guess -- give him a tips (hints)
"""

import random

# create a sequence of words
# and create a variable == random word at WORDS
# and create a jumble
WORDS = ("python", "anagram", "simple", "strong", "answer", "coaster")
word = random.choice(WORDS)
correct = word

# special params to tips&scores
score = 5
tips = ""

jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start game
print("""
                                WILLKOMMEN!
                            LET'S START THE GAME!
u have to rearrange the letters in word, so would happen is the right word
     (press "Enter" (without ur version), if u want leave the game)
      """)
print("ur anagram = ' ", jumble, " '")
guest = input("\nplease input ur version: ")

# tries to restore word
while guest != correct and guest != "" and score != 1:
	print("sorry, u're wrong")
#	tips += word [position]
#	print ("\nu'r tip now -- ", tips)
	guest = input("\nplease input ur version: ")
	score -= 2

if guest == correct:
    print("""
                                U'RE WINNER!
                thanks for playing; like, share, retweet""")
    print ("""
    		u have earned """, score, """scores!

    				""")

input("\npress any key to exit")
