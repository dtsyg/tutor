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
tries = 0
score = 5
hint = ""


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
                      u have 5 tries and maximum 5 scores
                          for each hints u lose 1 scores
     (press "Enter" (without ur version), if u want leave the game)
      """)
print("\nur anagram = ' ", jumble," '")
guest = input("\nplease input ur version: ")

# tries to restore word
while guest.lower() != correct and guest != "" and tries != 4:
    print("\nsorry, u're wrong")
    hint += correct [tries]
    print ("\nu'r tip now -- ", hint)
    tries += 1
    score -= 1
    guest = input("please input ur version: ")

if tries == 4 and guest.lower() != correct:
    print("""
   sorry, u'r tries is over
'please enter coin to Continue' """)

if guest.lower() == correct:
    print("""
                                U'RE WINNER!
                thanks for playing; like, share, retweet""")
    print ("""
    		u have earned """, score, """scores!

    				""")

input("\npress any key to exit")
