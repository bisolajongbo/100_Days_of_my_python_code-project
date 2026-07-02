import random
from art import logo, vs
from game_data import data

print(logo)


# Function to randomly select a celebrity
def get_celebrity():
    return random.choice(data)


# Function to determine the correct answer
def get_correct_answer(cele_A, cele_B):
    if cele_A["follower_count"] > cele_B["follower_count"]:
        return "A"
    else:
        return "B"


# Function to play the game
def play_game():

    score = 0
    game_should_continue = True

    # Pick the first celebrity
    cele_A = get_celebrity()

    while game_should_continue:

        # Pick the second celebrity
        cele_B = get_celebrity()

        # Make sure they are different
        while cele_A == cele_B:
            cele_B = get_celebrity()

        # Display both celebrities
        print(f"Compare A: {cele_A['name']} a {cele_A['description']} from {cele_A['country']}")
        print(vs)
        print(f"Compare B: {cele_B['name']} a {cele_B['description']} from {cele_B['country']}")

        # Ask the user for a guess
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Get the correct answer
        correct_answer = get_correct_answer(cele_A, cele_B)

        # Check if the user's guess is correct
        if guess == correct_answer:

            score += 1
            print("\n" * 20)
            print(logo)
            print(f"You're right! Current score: {score}")

            # If B is the winner, it becomes the new A
            if correct_answer == "B":
                cele_A = cele_B

        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


# Call the game function
play_game()