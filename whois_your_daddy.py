"""
programms "whois your daddy?"
user type son-name, programm will be find pair son-father
user also can create/delete/change pairs
"""

# parametrization
pairs = {"Arthas": "Terenas",
         "Icarus": "Daedalus",
         "Drizzt": "Zaknafein"}
user_choice = None

# menu
while user_choice != "0":
    print(
    """

    "WHOIS YOUR DADDY ?"

    ==============================
    ||  0   //  exit            ||
    ||  1   //  view pairs      ||
    ||  2   //  add pairs       ||
    ||  3   //  delete pairs    ||
    ||  4   //  replace pairs   ||
    ==============================
    """)
    user_choice = input("enter your choice: ")
    print()

# exit
    if user_choice == "0":
        print("goodbye!")

# view
    elif user_choice == "1":
        name = input(
            """
            please enter son name:
            """)
        print(
            """
            """, pairs.get(name,
            """
            sorry, but your name not in pairs-list
            """))

# add
    elif user_choice == "2":
        son = input(
                """
                please enter son name:
                """)
        if son not in pairs:
            father = input(
                """
                please enter father name:
                """)
            pairs[son] = father
        else:
            print(
                """
                sorry, but your son/father pair alredy exist
                """)
# delete
    elif user_choice == "3":
        son = input(
            """
            please enter son name:
            """)
        if son in pairs:
            del pairs[son]
        else:
            print(
            """
            sorry, but your son/father pair does not exist
            """)
# replace
    elif user_choice == "4":
        son = input(
            """
            please enter son name, what you wanna change:
            """)
        if son in pairs:
            father = input(
            """
            please, enter new father name:
            """)
            pairs[son] = father
        else:
            print(
            """
            sorry, but your son/father pair does not exist
            """)
# uncorrect input
    else:
        print(
            """
            sorry, but your choice uncorrect
            """)

input(
"""
press 'enter'-key to exit
""")
