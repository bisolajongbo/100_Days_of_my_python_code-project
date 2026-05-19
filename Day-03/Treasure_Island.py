print("Welcome to Treasure Island")
print('''
                  *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\' . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Your mission is to find Treasure")
Choice1 = input('You\'re at a crossroad.Where do you want to go? '
                'Type "left" or "right".\n').lower()
if Choice1 == "left":
    Choice2 = input('You\'ve come to  a lake.There \'s an Island in the middle of the lake\n '
                    'Type "Wait" to wait for a boat or \n'
                    'Type "Swim" to swim to across.\n').lower()
    if Choice2 == "wait":
        Choice3 = input('You\'ve arrived at the island unharmed.\n'
            'There is a house with 3 doors: one red, one yellow, and one blue.\n'
            'Which colour do you choose?\n').lower()
        if Choice3 == "red":
            print("You\'re in a room full of fire.GAME OVER")
        elif Choice3 == "yellow":
            print("You Won!!")
            print('''
            888
            888
            888
            888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.
            888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b
            888   888    88888888.d888888"Y8888b.888  888888    88888888
            Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.
             "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888
            ''')
        elif Choice3 == "blue":
            print("You\'re in a room full of beasts. Game Over.")
    else:
        print("You fell into a hole. Game Over.")

else:
    print("Invalid choice.GAME OVER!! ")


