import random
print("Welcome to the Rock, Paper, Scissors game!")
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

game_images=[rock,paper,scissors]

user_choice = int(input("What do number you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor\n"))
if user_choice>=0 and user_choice <=2:
    print(f"You choose: {game_images[user_choice]}")

    computer_choice = random.randint(0,2)
    print(f"Computer choose:{game_images[computer_choice]}")

if user_choice >2  or user_choice < 0 :
    print("Wrong Input")

elif user_choice == 0 and computer_choice >= 1:
    print("You win!!")

elif computer_choice == 0 and user_choice == 2:
    print("You loose")

elif user_choice == 1 and computer_choice == 0:
    print("You loose")

elif user_choice == 1 and computer_choice == 2:
    print(" Try again!!")

elif user_choice == 2  and computer_choice ==1:
    print("Come back again")

else :
    print("It a draw!!")

