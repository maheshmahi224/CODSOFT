import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

all_chars = letters + numbers + symbols

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(all_chars)

print("Generated Password:", password)
