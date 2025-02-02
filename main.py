# Guess a number game

# Import necessary packages
import random

# Global variables
NUM_MIN = 1
NUM_MAX = 10


# Generate the random number
def get_random_number():
    return random.randint(NUM_MIN, NUM_MAX)


# Main function
def main():
    random_number = get_random_number()

    print(f"Guess a number between {NUM_MIN} and {NUM_MAX}.")
    print(random_number)


# Script to run
main()
