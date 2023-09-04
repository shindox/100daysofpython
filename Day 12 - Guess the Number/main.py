#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from day12art import logo
from random import randint
import os

EASY_TURNS = 10
HARD_TURNS = 5

def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def check_answer(guess, answer, attempts_left):
  if guess > answer:
    print("Too high.")
    return attempts_left - 1
  elif guess < answer:
    print("Too low.")
    return attempts_left - 1
  elif guess == answer:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ") or 'hard'
  if difficulty == 'easy':
    return EASY_TURNS
  else:
    return HARD_TURNS

def guess_number():
  print(logo)
  
  answer = randint(1,100)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  
  attempts_left = set_difficulty()

  guess = 0

  while guess != answer:
    print(f"You have {attempts_left} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    attempts_left = check_answer(guess, answer, attempts_left)
    if attempts_left == 0:
      print(f"You've run out of guesses, you lose. The answer was {answer}.")
      return
    elif guess != answer:
      print("Guess again.")

while input("Do you want to play Guess the Number 'y' or 'n' ? ") == 'y':
  clear()
  guess_number()
  