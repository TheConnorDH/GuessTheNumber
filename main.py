import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 10


def get_random_number():
    return random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)


def get_valid_guess(prompt):
    while True:
        try:
            response = int(input(prompt))
        except ValueError:
            print("Input must be a number.")
            continue
        if response in range(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1):
            return response
        else:
            print(
                f"Please enter a number between {MINIMUM_NUMBER} and {MAXIMUM_NUMBER}."
            )


def get_valid_replay(prompt):
    while True:
        response = input(prompt).lower().strip()
        if response in ("y", "yes", "n", "no"):
            return response
        else:
            print("Invalid response.")


def first_guess():
    guess = get_valid_guess(
        f"Guess a number between {MINIMUM_NUMBER} and {MAXIMUM_NUMBER}: "
    )
    return guess


def guess_result(random_number, guess):
    guess_count = 1
    while True:
        if guess == random_number:
            print(
                f"You win! The number was {random_number}. It took you {guess_count} guesses."
            )
            break
        elif guess < random_number:
            guess = get_valid_guess("Too low. Try again: ")
            guess_count += 1
        elif guess > random_number:
            guess = get_valid_guess("Too high. Try again: ")
            guess_count += 1
    return False


def main():
    while True:
        random_number = get_random_number()
        guess = first_guess()
        guess_result(random_number, guess)
        replay = get_valid_replay("Would you like to play again? (Yes or No): ")
        if replay in ("n", "no"):
            break
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
