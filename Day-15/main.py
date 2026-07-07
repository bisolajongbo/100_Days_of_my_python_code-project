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

def is_resource_sufficient(order_ingredients):
    """Return True when order can't be made,and False if ingredient is insufficient """
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
             print(f"Sorry there is not enough water{item}")
             return False
        return True
    
    


def transaction_successful(money_recieved,drink_cost):
     """Return True when payment is successfull and False if money are insuffient""" 
     if money_recieved >= drink_cost:
          change= round(money_recieved-drink_cost,2)
          print(f"Your change is:{change}")
          global profit
          profit += drink_cost

          return True
     else:
          print("Sorry that's not enough money.Money refunded.")
          return False

def process_coins():
    """Return the total calculated from coins inserted"""
    print("Please insert coin.")
    total = int(input("How many quarter?:")) *0.25
    total += int(input("How many dimes?:")) *0.1
    total += int(input("How many nickles?:")) *0.05
    total += int(input("How many pennies?:")) *0.01
    return total
def make_coffee(drink_name,order_ingredient):
     """Deduct the required ingredients from the resources."""
     for item in order_ingredient:
          resources[item]-= order_ingredient[item]
     print(f"Here is your{drink_name}")

is_on =True
while is_on:
        user_choice=input("What would you like? (espresso/latte/cappuccino):")
        if user_choice == "off":
             is_on = False
        elif user_choice == "report":
            print(f"Water:{resources['water']}ml") 
            print(f"Milk:{resources['milk']}ml") 
            print(f"Coffee:{resources['coffee']}g") 
            print(f"Money:{profit}") 

        else:
            drink = MENU[user_choice]
            if is_resource_sufficient(drink["ingredients"]):
               payment= process_coins()
            if transaction_successful(payment,drink['cost']):
                make_coffee(user_choice, drink["ingredients"])

                
           


     