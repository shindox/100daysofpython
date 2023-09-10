from game_data import data
from art import logo, vs
from random import randint
import os

def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def select_second(selection1):
  while True:
    select2 = randint(0, 49)
    if select2 != selection1:
      return select2

def compare(selection1, selection2):
  if data[selection1]['follower_count'] > data[selection2]['follower_count']:
    return 'a'
  else:
    return 'b'

def game():
  print(logo)
  selection1 = randint(0, 49)
  score = 0
  while True:
    
    selection2 = select_second(selection1)
  
    print(f"Compare A: {data[selection1]['name']}, a {data[selection1]['description']}, from {data[selection1]['country']}")
    print(vs)
    print(f"Against B: {data[selection2]['name']}, a {data[selection2]['description']}, from {data[selection2]['country']}")
  
    pick = input(f"Who has more followers on instagram? Type 'A' or 'B' ").lower()
    answer = compare(selection1, selection2)

    clear()
    print(logo)
  
    if pick == answer:
      score += 1
      selection1 = selection2
      print(f"You're right! Current score: {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      return

game()
