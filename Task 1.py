#Random_password_genrator

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
password_length = int(input("Enter the desired length of the password: "))

# Generate and display the password
generated_password = generate_password(password_length)
print(f"Generated Password: {generated_password}")
