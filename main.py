import random
import string
import time
print("Welcome to the password generator which gives you strong but ridiculous passwords!")


time.sleep(2)

print("Password is coming!")

time.sleep(2)

def generate_password(length =12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    return password
my_password = generate_password()

print("Generated Password:" , my_password)
