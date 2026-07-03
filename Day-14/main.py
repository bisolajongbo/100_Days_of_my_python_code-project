import random
from art import logo, vs
from game_data import data

print(logo)


# Function to randomly select a celebrity
def get_celebrity():
    """Returns a random celebrity from the dataset."""
    return random.choice(data)


# Function to format celebrity information
def format_data(account):
    """Returns the celebrity information in a readable format."""
    return f"{account['name']}, a {account['description']}, from {account['country']}"


# Function to check if the user's guess is correct
def get_correct_answer(user_guess, cele_A, cele_B):
    """
    Returns True if the user's guess is correct,
    otherwise returns False.
    """
    if cele_A["follower_count"] > cele_B["follower_count"]:
        return user_guess == "A"
    else:
        return user_guess == "B"


# Function to play the game
def play_game():

    score = 0
    game_should_continue = True

    # Pick the first celebrity
    cele_A = get_celebrity()

    while game_should_continue:

        # Previous B becomes the next A (except first round)
        cele_B = get_celebrity()

        # Make sure both celebrities are different
        while cele_A == cele_B:
            cele_B = get_celebrity()

        # Display celebrities
        print(f"Compare A: {format_data(cele_A)}")
        print(vs)
        print(f"Against B: {format_data(cele_B)}")

        # Get user's guess
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Check answer
        is_correct = get_correct_answer(guess, cele_A, cele_B)

        # Clear screen
        print("\n" * 20)
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")

            # Winner (B) becomes the next A
            cele_A = cele_B

        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


# Start the game
play_game()