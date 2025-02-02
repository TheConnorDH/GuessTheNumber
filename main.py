import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 10


def get_random_number():
    """
    Return a random integer between MINIMUM_NUMBER and MAXIMUM_NUMBER (inclusive).

    Args:
        None

    Returns:
        int: A random integer within the specified range.
    """
    return random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)


def get_guess(prompt):
    """
    Prompt the user to input a guess and validate that it is an integer within the allowed range.

    Args:
        prompt (str): The message displayed to the user when asking for input.

    Returns:
        int: A valid guess provided by the user.
    """
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


def get_replay(prompt):
    """
    Prompt the user for a replay decision and validate the input is one of the accepted responses.

    Args:
        prompt (str): The message displayed to ask if the user wants to play again.

    Returns:
        str: The user's response (one of "y", "yes", "n", or "no") in lowercase.
    """
    while True:
        response = input(prompt).lower().strip()
        if response in ("y", "yes", "n", "no"):
            return response
        else:
            print("Invalid response.")


def guess_result(random_number, guess):
    """
    Process the guessing loop by comparing the user's guess to the random number until the correct guess is made.
    It also tracks the number of guesses taken.

    Args:
        random_number (int): The target number to be guessed.
        guess (int): The user's initial guess.

    Returns:
        None
    """
    guess_count = 1
    while True:
        if guess == random_number:
            print(
                f"You win! The number was {random_number}. It took you {guess_count} guesses."
            )
            break
        elif guess < random_number:
            guess = get_guess("Too low. Try again: ")
            guess_count += 1
        elif guess > random_number:
            guess = get_guess("Too high. Try again: ")
            guess_count += 1


def main():
    """
    Run the 'Guess the Number' game. This function loops, starting a new game each time the user wins,
    and asks whether the user would like to play again. The loop terminates when the user declines to replay.
    """
    while True:
        random_number = get_random_number()
        guess = get_guess(
            f"Guess a number between {MINIMUM_NUMBER} and {MAXIMUM_NUMBER}: "
        )
        guess_result(random_number, guess)
        replay = get_replay("Would you like to play again? (Yes or No): ")
        if replay in ("n", "no"):
            break
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
