"""
program printed all words in list (random sort)
all words, one word -- one print
v1 // simple
v2 // with user-input words-list and prepared words-list
v3 // with auto-generate words-list, (and with user-input words-list and prepared words-list -- menu)
"""

import random

# parametrization
WORDS = ("one", "two", "two", "six", "three", "four", "five", "five")

user_words = []
user_word = " "
uniq_prep = []
uniq_user = []

# user input
user_choice = input(
    """
    whether you want himself type the words-list? Y / N
    """)
user_choice.lower

# user-input words-list
if user_choice == "y":

    # user-input words-list
    while user_word:
        user_word = input(
            """
            please type the word,
            if you have finished -- press enter-key without word
            """)
        user_words.append(user_word)
    print("""
    old words-list: """, user_words)

    # remove duplicates
    for word in user_words:
        if word not in uniq_user:
            uniq_user.append(word)

    # shuffle
    random.shuffle(uniq_user)

    # output
    print("""
    new words-list: """, uniq_user)

# prepared words-list
elif user_choice == "n":
    print("""
    old words-list: """, WORDS)

    # remove duplicates
    for word in WORDS:
        if word not in uniq_prep:
            uniq_prep.append(word)

    # shuffle
    random.shuffle(uniq_prep)

    # output
    print("""
    new words-list: """, uniq_prep)

# implicit user_choice
else:
    print("sorry, but your choice implicit, try again;")
    user_choice = input(
        """
        whether you want himself enter a words-list? Y / N
        """)

input("\npress enter-key to exit")
