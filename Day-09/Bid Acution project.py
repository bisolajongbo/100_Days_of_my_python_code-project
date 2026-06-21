import random
# Import the logo from the art module
from art import logo

# Display the auction logo
print(logo)

# Function to run the blind auction program
def biding():

    # Dictionary to store bidder names and their bid amounts
    bids = {}

    # Variables to track the winner and highest bid
    winner = ""
    highest_bid = 0

    # Controls whether the auction should continue
    continue_bidding = True

    # Keep collecting bids while there are more bidders
    while continue_bidding:

        # Get the bidder's name
        name = input("Enter your name:\n")

        # Get the bidder's price and convert it to a float
        price = float(input("What is your bidding price?\n"))

        # Store the name and bid amount in the dictionary
        bids[name] = price

        # Ask if there are more bidders
        new_bidders = input("Type 'yes' if there are other bidders that wants to bid and 'no' if there are none: ").lower()

        # If there are no more bidders, determine the winner
        if new_bidders == "no":
            continue_bidding = False

            # Loop through all bids to find the highest bidder
            for bidder in bids:

                # Get the bid amount for the current bidder
                bid_amount = bids[bidder]

                # Update the highest bid and winner if a larger bid is found
                if bid_amount > highest_bid:
                    highest_bid = bid_amount
                    winner = bidder

            # Display the winner and their bid amount
            print(f"The winner is {winner} with the bid of {highest_bid}")
            print("Goodbye")

        # Handle invalid user input and try again
        elif new_bidders not in ["yes", "no"]:
            continue_bidding = True
            print("Invalid input. Try again")
            print("\n"*10)

        # Continue the auction if there are more bidders
        elif new_bidders == "yes":
            continue_bidding = True

            # Clear the screen by printing multiple blank lines
            print("\n" * 20)

# Start the auction program
biding()