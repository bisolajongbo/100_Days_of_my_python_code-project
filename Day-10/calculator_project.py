from art import logo
print(logo)
# ----------------------------
# Basic Arithmetic Functions
# ----------------------------

def add(n1, n2):
    # Returns the sum of two numbers
    return n1 + n2


def subtract(n1, n2):
    # Returns the difference between two numbers
    return n1 - n2


def multiply(n1, n2):
    # Returns the product of two numbers
    return n1 * n2


def divide(n1, n2):
    # Returns the division of two numbers
    # (Note: no division-by-zero handling added here)
    return n1 / n2


# ----------------------------
# Dictionary Mapping Symbols to Functions
# ----------------------------

maths_symbol = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# ----------------------------
# Main Calculator Function
# ----------------------------

def calculation():
    # Welcome message
    print("Welcome to My Simple Calculator\n")

    # Flag to control loop execution
    continue_cal = True

    # Get the first number from the user
    num1 = int(input("Enter the first number for calculation: "))

    # Loop continues while user wants more calculations
    while continue_cal:

        # Display available operations
        for symbol in maths_symbol:
            print(symbol)

        # Ask user to choose an operation
        operation = input("Choose an operation: ")
       
        # Validate operation input
        if operation not in maths_symbol:
            print("Invalid operation")
            continue  # Restart loop if invalid input

        # Get next number for calculation
        num2 = int(input("Enter the next number for calculation: "))

        # Perform calculation using selected operation
        result = maths_symbol[operation](num1, num2)

        # Display result of calculation
        print(f"{num1} {operation} {num2} = {result}")

        # Ask user if they want to continue with result
        choice = input("Enter 'yes' or 'no' for more calculation: ")

        # If yes, continue using result as first number
        if choice == "yes":
            num1 = result
        else:
            # Stop the loop and display final result
            continue_cal = False
            print(f"Result = {result}")


# ----------------------------
# Start the Program
# ----------------------------

calculation()