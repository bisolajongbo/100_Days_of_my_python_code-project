import random
from art import logo

# List of possible card values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Function to randomly deal a card
def deal_cards():
    return random.choice(cards)


# Function to calculate the score of a hand
def calculate_score(cards):
    score = sum(cards)

    # Check for Blackjack (Ace + 10-value card)
    if score == 21 and len(cards) == 2:
        return 0

    # Convert Ace from 11 to 1 if score exceeds 21
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)

    return score


# Function to compare scores and determine the winner
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack."
    elif user_score == 0:
        return "You win with Blackjack!"
    elif user_score > 21:
        return "You lose."
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."


# Function to play one complete game of Blackjack
def play_game():

    # Display the game logo
    print("\n" * 20)
    print(logo)

    # Create empty hands for user and computer
    user_cards = []
    computer_cards = []

    # Variable to control the game loop
    game_over = False

    # Deal two cards to both player and computer
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    # Main game loop
    while not game_over:

        # Calculate current scores
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Show current game status
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # End the game if someone has Blackjack or the user busts
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            # Ask the user whether they want another card
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()

            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                game_over = True

    # Computer keeps drawing until score reaches 17 or higher
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    # Display final hands and scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Display the result
    print(compare(user_score, computer_score))


# Keep asking the user if they want to play
while True:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if choice == 'y':
        play_game()
    else:
        print("Thanks for playing!")
        break