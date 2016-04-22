"""
program printed all words in list (random sort)
all words, one word -- one print
v1 // simple
v2 // with user-input list
"""

import random

# parametrization
WORDS = ("one", "two", "two", "six", "three", "four", "five", "five")
uniq = []

print("""
old words-list: """, WORDS)

# remove duplicates
for word in WORDS:
    if word not in uniq:
        uniq.append(word)

# shuffle
random.shuffle(uniq)


# output
print("""
new words-list: """, uniq)

input("""

press enter-key to exit
""")
