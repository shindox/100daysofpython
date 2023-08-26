#Calculator
from day10art import logo
import os

def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2

#Exponent
def exponent(n1, n2):
  return n1**n2


#Calculate Function returns the result
# def calculate_function(num1, num2, operation_symbol):
#     return operations[operation_symbol](num1, num2)

operations = {"+": add, "-": subtract, "*": multiply, "/": divide, "**": exponent}

def calculate():
  print(logo)
  keep_calculate = True
  num1 = float(input("What's the first number?: "))
  
  while keep_calculate:
  
      num2 = float(input("What's the next number?: "))
  
      for symbol in operations:
          print(symbol)
  
      operation_symbol = input("Pick an operation: ")
  
      calculation_function = operations[operation_symbol]
      answer = calculation_function(num1, num2)
  
      print(f"{num1} {operation_symbol} {num2} = {answer:.2f}")
  
      select = 'o'
      while select not in 'yne':
        select = input(f"Type 'y' to continue calculating with {answer:.2f} or type 'n' to start a new calculation or type 'e' to exit: ")
        
      if select == 'y':
          num1 = answer
      elif select == 'n':
          keep_calculate = False
          clear()
          calculate()
      elif select == 'e':
          return False
  
calculate()
