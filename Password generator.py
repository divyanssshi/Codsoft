# PASSWORD GENERATOR
import random  # importing Libraries
import string


def password(size):
    # character sets for letters, digits, and some special characters
    letters = string.ascii_letters
    digits = string.digits
    special_char = "@#$!.%"

    # combining the letters, digits and characters
    combined = letters + digits + special_char

    # To check if the password length is enough to set
    if size < 8:
        return ("Password length should be at least 8 characters.")

    # This will help to generate passwords randomly
    password = ''.join(random.choice(combined) for i in range(size))
    return password


# Input from the user for the desired length of password
try:
    size = int(input("Enter the desired password length: "))
    final_pass = password(size)
    print("Final Password : ", final_pass)

# This exception will help the code not to crash and gives the name of error and details
except Exception as a:
    print(type(a).__name__, a, "\nPlease enter a integer!")
