"""
program printed all words in list (random sort)
all words, one word -- one print
"""

import random

# parametrization
WORDS = ("one", "two", "three", "four", "five")
#         0    1    2    3    4
used =""
words = []
j =0

for word in WORDS:
    print("\n", word)
    i = random.randrange(0, len(WORDS) + 1)
    temp = WORDS[i]
    if temp not in used:
        words += temp
#        j += 1
        used += temp


print ("""
old words-list: """)
for word in WORDS:
    print (word, end=", ")
print ("""

new words-list:""")
for word in words:
    print (word, end=", ")

input("""

press enter-key to exit
""")
