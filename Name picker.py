def pickname():
    import random

    print("Enter first name: ")
    name1 = input()
    print("Enter second name: ")
    name2 = input()
    print("Enter third name: ")
    name3 = input()

    mylist = [name1, name2, name3]
    random = random.choice(mylist)
    print("Random name: \n" + random)

import time
reroll = "yes"

while True:
    if reroll == "yes" or reroll == "y":
        pickname()
        time.sleep(1)
        reroll = input("\nReroll?\n(Press y to start again)\n(Press any key to quit)\n")

    else:
        print("Thank you")
        break
