#python program

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# This will generate a random number
secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")

else:
    print(f"Game over! The number was {secret_number}.")
