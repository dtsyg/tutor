"""
Напишите программу «Генератор персонажей» для ролевой игры. Пользователю должно быть предоставлено
30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость
и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего «Пула», но и возвращать
их туда из характеристик, которым он решит присвоить другие значения.
"""

# parametrization
user_choice = None
char_pool = 30
strength = 0
dexterity = 0
wisdom = 0
lucky = 0

while user_choice != "0":
    print(
    """

    "CHARACTER MAKER"
    0   //        exit
    1   //  increase parameter
    2   //  decrease parameter
    """)

    print("your parameter pool = ", char_pool,
          "\nstrength / ", strength,
          "\ndexterity / ", dexterity,
          "\nwisdom / ", wisdom,
          "\nlucky / ", lucky)
    user_choice = input("\nenter your choice: ")

# exit
    if user_choice == "0":
        print(
            """
            goodbye!
            """)

#    if user_choice == "1":
#        param_choice = input()