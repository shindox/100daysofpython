MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resource_sufficient(order_ingredients):
  for item in order_ingredients:
    if order_ingredients[item] > resources[item]:
      print(f"​Sorry there is not enough {item}.")
      return False
    else:
      return True

def process_coins():
  print("Please insert coins.")
  total = int(input("how many quarters?: ")) * 0.25
  total += int(input("how many dimes?: ")) * 0.10
  total += int(input("how many nickles?: ")) * 0.05
  total += int(input("how many pennies?: ")) * 0.01
  return total

def transaction_successful(total_coins, drink_cost):
  if total_coins >= drink_cost:
    change = round(total_coins - drink_cost, 2)
    print(f"Here is ${change} in change.")
    global profit
    profit += drink_cost
    return True
  else:
    print("Sorry that's not enough money. Money refunded.")
    return False

def make_coffee(drink_name, order_ingredients):
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]
  print(f"Here is your {drink_name} ☕. Enjoy!")
  
    
machine_on = True

while machine_on:  
  
  selection = input("What would you like? (espresso/latte/cappuccino): ")
  if selection == 'off':
    machine_on = False
  elif selection == 'report':
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
  else:
    drink = MENU[selection]
    if check_resource_sufficient(drink["ingredients"]):
      payment = process_coins()
      if transaction_successful(payment, drink["cost"]):
        make_coffee(selection, drink["ingredients"])
    

