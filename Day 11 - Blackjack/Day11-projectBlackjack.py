############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from day11art import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
  return random.choice(cards)

def calculate_score(card_list):
  score = sum(card_list)
  if score == 21 and len(card_list) == 2:
    return 0
  elif score > 21 and 11 in card_list:
    card_list.remove(11)
    card_list.append(1)
  return sum(card_list)

def compare(user_score, computer_score):
  if user_score > 21:
    return "You went over. You lose 😤"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score == computer_score:
    return "Draw 🙃"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
    
def play_blackjack():
  print(logo)
  
  game_ends = False
  user_cards = []
  computer_cards = []
  
  for i in range(2): # Deal the user and computer 2 cards each
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    

  while not game_ends:
    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)

    print(f"Your cards are: {user_cards}, your current score is : {user_score}")
    print(f"Computer's first card is: {computer_cards[0]}")


    
    if computer_score == 0 or user_score == 0 or user_score >= 21:
      # user_score >= 21 is to prevent drawing another card when you reach 21
      game_ends = True

    else:
      want_card = input("Do you want to draw another card? 'y' or 'n' ")
      if want_card == 'y':
        user_cards.append(deal_card())

      else:
        game_ends = True
        
    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)

  
  print(f"Your final hand is: {user_cards}, final score is : {user_score}")
  print(f"Computer's final hand is: {computer_cards}, final score is : {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? 'y' or 'n'? ") == 'y':
  clear()
  play_blackjack()




        
  

    
  



