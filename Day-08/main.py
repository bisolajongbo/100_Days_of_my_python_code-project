# Import the art module and display the Caesar Cipher logo
import art

print(art.logo)

# List containing all lowercase letters of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Function to encode or decode a message using the Caesar Cipher technique
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # If the user chooses decode, reverse the shift direction
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Loop through each character in the user's message
    for letter in original_text:

        # Keep spaces, numbers, and symbols unchanged
        if letter not in alphabet:
            output_text += letter
        else:
            # Find the new position after shifting
            shifted_position = alphabet.index(letter) + shift_amount

            # Wrap around the alphabet if the position exceeds its length
            shifted_position %= len(alphabet)

            # Add the shifted letter to the output text
            output_text += alphabet[shifted_position]

    # Display the encoded or decoded message
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Variable to control whether the program should continue running
should_continue = True

# Main program loop
while should_continue:

    # Ask the user whether to encode or decode a message
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Get the message from the user
    text = input("Type your message:\n").lower()

    # Get the shift value from the user
    shift = int(input("Type the shift number:\n"))

    # Call the Caesar Cipher function
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user if they want to perform another operation
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    # End the program if the user enters "no"
    if restart == "no":
        should_continue = False
        print("Goodbye")