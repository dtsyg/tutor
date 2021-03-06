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
while guest != correct and guest != "":
    print("sorry, u're wrong")
    guest = input("\nplease input ur version: ")

if guest == correct:
    print("""
                                U'RE WINNER!
                thanks for playing; like, share, retweet""")

input("\npress any key to exit")
