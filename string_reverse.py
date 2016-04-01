"""
program will be grabing user input
and reverse it
"""

user_string = input("pls input a new string\n")
new_string = ""
print(len(user_string), "string length")

for i in range(len(user_string) - 1, -1, -1):
    new_string += user_string[i]
    print("position", i)
    print("ur new reverse-string -- ", new_string)
"""
for i in range(0, len(user_string), 1):
    i = -i
    new_string += user_string[i]
    print("position", i)
    print("ur new reverse-string -- ", new_string)
"""

input("press any key to exit")
