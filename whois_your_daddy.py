"""
Напишите программу «Кто твой папа?», в которой пользователь будет вводить имя человека, а программа
- называть отца этого человека. Чтобы было интереснее, можно «научить» программу родственным
отношениям среди литературных персонажей, исторических лиц и современных знаменитостей. Предоставьте
пользователю возможность добавлять, заменять и удалять пары «СЫН - отец».
"""

# parametrization
pairs = {"Arthas": "Terenas",
         "Icarus": "Daedalus",
         "Drizzt": "Zaknafein"}
user_choice = None

# menu
while user_choice != 0:
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
    """
    )
    user_choice = int(input("input your choice: "))
    print()

    # exit
    if user_choice == 0:
        print("goodbye!")

    # view
    if user_choice == 1:
        name = input("""please input son name:
        """)
        print(pairs.get(name, "sorry, but your name not in pairs-list"))

    # add
    if user_choice == 2:
        son = input("""please input son name:
        """)
        if son not in pairs:
            father = input("""please input father name:
            """)
            pairs[son] = father
        else:
            print("""
            sorry, but your son/father pair alredy exist""")

input("""
press 'enter'-key to exit
""")


