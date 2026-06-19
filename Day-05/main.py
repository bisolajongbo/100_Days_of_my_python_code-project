import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# Here you choose the type of password user want to generate
generate=input("Type 'easy' for easy password or 'strong' for strong password\n").lower()
# The user specifies how many letters, symbols, and numbers they want included in their password.
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []   #password generated will be store here
# In this for loop password will randomly be generated in symbols,numbers and letters

for char in range(0,nr_letters+1):
    password_list.append(random.choice(letters))

for symbol in range(0,nr_symbols+1):
    password_list.append(random.choice(symbols))

for number in range(0,nr_numbers+1):
    password_list.append(random.choice(numbers))

easy_password=""
for password in password_list:
    easy_password+=password
if generate == "easy":
    print(f"Your easy Password is:{easy_password}")

random.shuffle(password_list)
strong_password=""
for password in password_list:
    strong_password+=password
if generate == "strong":
    print(f"Your Strong Password is:{strong_password}")

