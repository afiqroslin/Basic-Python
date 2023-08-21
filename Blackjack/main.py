import random
from replit import clear

# rules:
# cards with number closer to 21 wins
# far than 21 will lose
# over 21 will be busted and lose
# if dealer has cards less than 17 they have to draw another card
# if both dealer and player has same cards value, it is a draw

# gameplay:
# player is to start with a  cards
# can hit to ask dealer for more card to add until the number closer to 21
# player can stand if they confident with their cards
# King, queen, jack = 10
# Ace = 1 or 11 (player can decide)


def drawCards():
  draw = random.randint(0, 11)
  return draw


def calculateScore(player_cards, dealer_cards):
  player_score = sum(player_cards)
  dealer_score = sum(dealer_cards)
  while dealer_score < 17:
    dealer_cards.append(cards[drawCards()])
    dealer_score = sum(dealer_cards)
  return player_score, dealer_score


def showScore(player_score, dealer_score):
  #Show player cards and calculate the score
  print(f"Dealer cards {dealer_cards}")
  print(f"Dealer score {dealer_score}")
  print(f"Player cards {player_cards}")
  print(f"Player score {player_score}")


###########--------MAIN PROGRAM---------################
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
player_cards = []
dealer_cards = []

#First draw cards for player and dealer
draw_card = True
while draw_card:
  player_cards.append(cards[drawCards()])
  dealer_cards.append(cards[drawCards()])
  if len(player_cards) == 2 and len(dealer_cards) == 2:
    draw_card = False

player_score, dealer_score = calculateScore(player_cards, dealer_cards)
showScore(player_score, dealer_score)

#Player draw another card
draw_another = True
while draw_another:
  if input("Draw another card? 'y' or 'n'") == "y":
      player_cards.append(cards[drawCards()])
      player_score, dealer_score = calculateScore(player_cards, dealer_cards)
      clear()
      showScore(player_score, dealer_score)

  else:
    draw_another = False

#Compare dealer and player cards
if player_score > 21 and dealer_score > 21:
  print("Draw!")
elif player_score == dealer_score:
  print("Draw!")
elif player_score == 21:
  print("Player win!")
elif dealer_score == 21:
  print("Dealer win!")
  print(dealer_score)
elif player_score > 21 and dealer_score <= 21:
  print("Dealer win!")
elif player_score <= 21 and dealer_score > 21:
  print("Player win!")
elif player_score > dealer_score:
  print("Player win!")
elif player_score < dealer_score:
  print("Dealer win!")

