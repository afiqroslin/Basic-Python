import random

number = random.randint(0, 10)  # Generate random number in range of 0 to 10

while True:
    print("Guess a number: ")
    print(number)

    for counter in range(3):
        answer = int(input())
        counter = counter + 1

        while answer != number and counter <= 2:
            print("Try again!")
            break

        if answer != number and counter == 3:
            print("You lose")
            break

        if answer == number:
            print("You are right")
            break
    break
