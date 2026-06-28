from random import randint
from art import  logo

EASY_LEVEL=10
HARD_LEVEL=5
turns=0
# Function to check user's guess against actual answer
def check_answer(user_guess,actual_answer,turns):
    """"Checks answer against guess,returns the numbers of turns remaining """
    if user_guess > actual_answer:
        print("Too high")
        return turns-1
    elif user_guess < actual_answer:
        print("Too low")
        return turns-1
    else:
        print(f"You guessed correctly!The answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level=input("Choose a level,Type 'easy' or 'hard':")
    if level == "easy":
        return EASY_LEVEL
  
    else:
      return HARD_LEVEL

def game():
    print(logo)
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100")
    answer= randint(1,100)
    print(f"Correct  answer is: {answer} ")
    turns=set_difficulty()

    # Repeat the guessing functionality if they get it wrong
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        #Let the user guess a number
        guess = int(input("Make a guess :"))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You've run out of guesses.Game over")
            return
        elif guess!=answer:
            print("Guess again")
# Track the number of turns and reduce by 1 if they get it wrong

game()