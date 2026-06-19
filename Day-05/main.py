# Import the random module to generate random characters
import random

# Lists containing letters, numbers, and symbols that can be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Display a welcome message to the user
print("Welcome to the PyPassword Generator!")

# Ask the user whether they want an easy or strong password
generate = input("Type 'easy' for easy password or 'strong' for strong password\n").lower()

# Get the number of letters, symbols, and numbers the user wants in the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Create an empty list to store the randomly generated password characters
password_list = []

# Randomly select the specified number of letters and add them to the password list
for char in range(0, nr_letters + 1):
    password_list.append(random.choice(letters))

# Randomly select the specified number of symbols and add them to the password list
for symbol in range(0, nr_symbols + 1):
    password_list.append(random.choice(symbols))

# Randomly select the specified number of numbers and add them to the password list
for number in range(0, nr_numbers + 1):
    password_list.append(random.choice(numbers))

# Combine all selected characters into an easy password
# The characters remain in the order they were added
easy_password = ""

for password in password_list:
    easy_password += password

# Display the easy password if the user selected "easy"
if generate == "easy":
    print(f"Your Easy Password is: {easy_password}")

# Shuffle the password characters to make the password more secure
random.shuffle(password_list)

# Combine the shuffled characters into a strong password
strong_password = ""

for password in password_list:
    strong_password += password

# Display the strong password if the user selected "strong"
if generate == "strong":
    print(f"Your Strong Password is: {strong_password}")