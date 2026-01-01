import string
import random

specialchars = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

def user_input():
    print("Enter length of password (<=12 characters)")
    userInput = input()

    if int(userInput)<12:
        raise "Length must be at least 12 characters"
    return int(userInput)

def password_generation(length):
    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        password += random.choice(characters)
        password += random.choice(specialchars)
    return password

length = user_input()
password = password_generation(length)
print(password)