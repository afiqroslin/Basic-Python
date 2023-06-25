import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('''
Welcome to Rock, Paper, Scissors! 
Select your choice:
0. Rock
1. Paper
2. Scissors''')
choices = [rock, paper, scissors]

player_choice = int(input())
if player_choice >= 3 or player_choice < 0:
    print("Invalid choice!")
    quit
else:
    player_pick = choices[player_choice]
    print(f"You choose:\n{player_pick}")

    computer_pick = choices[random.randint(0, 2)]
    print(f"Computer choose:\n{computer_pick}")

    if player_pick == choices[0]:
        if computer_pick == choices[0]:
            print("Draw")
        elif computer_pick == choices[1]:
            print("Computer Win")
        else:
            print("You Win")

    if player_pick == choices[1]:
        if computer_pick == choices[0]:
            print("You Win")
        elif computer_pick == choices[1]:
            print("Draw")
        else:
            print("Computer Win")

    if player_pick == choices[2]:
        if computer_pick == choices[0]:
            print("Computer Win")
        elif computer_pick == choices[1]:
            print("You Win")
        else:
            print("Draw")

# if computer_pick == choices[0] and player_pick == choices[2]:
#     print("Computer Win")

# elif computer_pick == choices[1] and player_pick == choices[2]:
#     print("You Win")

# elif computer_pick == choices[2] and player_pick == choices[2]:
#     print("Draw")

# elif computer_pick == choices[0] and player_pick == choices[1]:
#     print("You Win")

# elif computer_pick == choices[1] and player_pick == choices[1]:
#     print("Draw")

# elif computer_pick == choices[2] and player_pick == choices[1]:
#     print("Computer Win")

# elif computer_pick == choices[0] and player_pick == choices[0]:
#     print("Draw")

# elif computer_pick == choices[1] and player_pick == choices[0]:
#     print("Computer Win")

# elif computer_pick == choices[2] and player_pick == choices[0]:
#     print("You Win")
