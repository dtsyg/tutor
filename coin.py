"""
программа подбрасывает монетку 100 раз,
считает количество выпавших орлов и решек
"""

import random
import time

"""
count		-- количество бросков монетки
avers		-- орёл (1)
revers	-- решка (0)
"""

avers = int(0)
revers = int(0)
count = int(0)

while count < 100:
    coin = random.randrange(2)
    count += 1
    if coin == 0:
        revers += 1
        print("выпала решка")
        time.sleep(0.1)
    elif coin == 1:
        avers += 1
        print("выпал орёл")
        time.sleep(0.1)
    else:
        print("что за хуйня тут произошла?")

print("\nрешка выпала ", revers, " раз, орёл выпал ", avers, " раз\n")
input("press enter-key to exit...")
