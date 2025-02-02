# Guess a number game

# Import necessary packages
import random

# Global variables
NUM_MIN = 1
NUM_MAX = 10


# Generate the random number
def get_random_number():
    return random.randint(NUM_MIN, NUM_MAX)


def get_valid_guess(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input must be a number.")


def first_guess():
    guess = get_valid_guess(f"Guess a number between {NUM_MIN} and {NUM_MAX}: ")
    return guess


def guess_result(random_number, guess):
    while True:
        if guess == random_number:
            print(f"You win! The number was {random_number}.")
            break
        elif guess < random_number:
            guess = get_valid_guess("Too low. Try again: ")
        elif guess > random_number:
            guess = get_valid_guess("Too high. Try again: ")


# Main function
def main():
    random_number = get_random_number()
    guess = first_guess()
    guess_result(random_number, guess)


# Script to run
if __name__ == "__main__":
    main()
