# Import the random module to enable random selection and shuffling
import random

# List of uppercase and lowercase letters that can be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of numbers that can be used in the password
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of symbols that can be used in the password
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Display a welcome message to the user
print("Welcome to the PyPassword Generator!")

# Ask the user how many letters, symbols, and numbers they want in the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Hard Level - Password characters will be randomized

# Create an empty list to store the selected characters
password_list = []

# Randomly select the specified number of letters and add them to the password list
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Randomly select the specified number of symbols and add them to the password list
for symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

# Randomly select the specified number of numbers and add them to the password list
for number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

# Shuffle the characters to create a stronger and less predictable password
random.shuffle(password_list)

# Create an empty string to store the final password
password = ""

# Combine all characters in the shuffled list into a single password string
for char in password_list:
    password += char

# Display the generated password to the user
print(f"Your Password is: {password}")