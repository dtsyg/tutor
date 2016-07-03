"""
Please write program "Character Generator". The user has 30 points (pool),
which he can spend between the four characteristics: Strength, Wisdom, Dexterity и Lucky.
The user can take and return points from the pool, and change alredy filled characteristics.
"""

# parametrization
user_menu = None
user_key = None
user_num = None
char_pool = 30
param = {"strength": 5,
         "wisdom": 5,
         "dexterity": 5,
         "lucky": 5,
         }

# user menu
print(
    '''

              "CHARACTER MAKER"


    1   //           menu
    2   //    show characteristic
    3   //  increase characteristic
    4   //  decrease characteristic
    0   //           exit
    ''')

while user_menu != "0":

    user_menu = input('''
    enter your choice ("1" for menu): ''')

    # menu call
    if user_menu == "1":
        print(
    '''
              "CHARACTER MAKER"


    1   //           menu
    2   //    show characteristic
    3   //  increase characteristic
    4   //  decrease characteristic
    0   //           exit
    ''')

    # show characteristics
    elif user_menu == "2":
        print(
              '''
              ======================
                 your pool = ''', char_pool,
              '''

                 strength  : ''', param["strength"],
              '''
                 wisdom    : ''', param["wisdom"],
              '''
                 dexterity : ''', param["dexterity"],
              '''
                 lucky     : ''', param["lucky"], '''
              ======================
              '''
        )

    # edit (increase)
    elif user_menu == "3":
        user_key = input(
            '''
    please enter the name of the characterictis (strength / wisdom / dexterity / lucky) : ''')
        while user_key not in param:
            print(
                '''
                this characteristics does not exist!
                '''
            )
            user_key = input(
                '''
    please enter the name of the characteristics (strength / wisdom / dexterity / lucky) : ''')

        user_num = int(input(
            '''
        how much points added: '''))

        if user_num <= char_pool:
            char_pool -= user_num
            param[user_key] += user_num
            print(param.get(user_key))
        else:
            print('''
                you don't have as many points! you can type less or decrease other characteristics''')

    # edit (decrease)
    elif user_menu == "4":
        user_key = input(
            '''
    please enter the name of the characterictis (strength / wisdom / dexterity / lucky) : ''')
        while user_key not in param:
            print(
                '''
                this characteristics does not exist!
                '''
            )
            user_key = input(
                '''
    please enter the name of the characteristics (strength / wisdom / dexterity / lucky) : ''')

        user_num = int(input(
            '''
        how much points withdraw: '''))

        if user_num <= param[user_key] - 1:
                char_pool += user_num
                param[user_key] -= user_num
                print(param.get(user_key))
        else:
            print('''
                number of point in characteristics cannot be less than one! you can type less or first increase this characteristic''')

    # exit
    elif user_menu == "0":
        print(
            '''
            goodbye!
            ''')

    # uncorrect input
    else:
        print(
            """
            sorry, but your choice uncorrect
                       try again
            """)
