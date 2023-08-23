#from replit import clear
from artday9 import logo
#HINT: You can call clear() to clear the output in the console.
import os

def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
bids = {}

def bidresult(bids):
  winning_bid = 0
  winner = ""
  for bidder in bids:
    if bids[bidder] > winning_bid:
      winning_bid = bids[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of ${winning_bid}")


bid_goes = True

while bid_goes:
  name = input("What's your name? ")
  bid_amount = int(input("What is your bid?: $"))
  bid_more = input("Are there any other bidders? Type 'yes or 'no'.")

  bids[name] = bid_amount
    
  if bid_more == "no":
    bid_goes = False
    bidresult(bids)
  elif bid_more == "yes":
    clear()
    