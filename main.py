import random


def get_minimum_number(prompt):
    """
    Prompt the user to input a minimum value that the random number can be selected from and validate that it is an integer within the allowed range.

    Args:
        prompt (str): The message displayed to the user when asking for input.

    Returns:
        int: A valid minimum number provided by the user.
    """
    while True:
        try:
            response = int(input(prompt))
        except ValueError:
            print("Input must be a number.")
            continue
        if response > 0:
            return response
        else:
            print("Value must be greater than zero.")


def get_maximum_number(prompt, minimum_number):
    """
    Prompt the user to input a maximum value that the random number can be selected from and validate that it is an integer within the allowed range.

    Args:
        prompt (str): The message displayed to the user when asking for input.
        minimum_number (int): The minimum value for the random number, inputted by the user.

    Returns:
        int: A valid maximum number provided by the user.
    """
    while True:
        try:
            response = int(input(prompt))
        except ValueError:
            print("Input must be a number.")
            continue
        if response > minimum_number:
            return response
        else:
            print(f"Value must be greater than {minimum_number}.")


def get_random_number(minimum_number, maximum_number):
    """
    Return a random integer between MINIMUM_NUMBER and MAXIMUM_NUMBER (inclusive).

    Args:
        minimum_number (int): The minimum value for the random number, inputted by the user.
        maximum_number (int): The minimum value for the random number, inputted by the user.

    Returns:
        int: A random integer within the specified range.
    """
    return random.randint(minimum_number, maximum_number)


def get_guess(prompt, minimum_number, maximum_number):
    """
    Prompt the user to input a guess and validate that it is an integer within the allowed range.

    Args:
        prompt (str): The message displayed to the user when asking for input.
        minimum_number (int): The minimum value for the random number, inputted by the user.
        maximum_number (int): The minimum value for the random number, inputted by the user.

    Returns:
        int: A valid guess provided by the user.
    """
    while True:
        try:
            response = int(input(prompt))
        except ValueError:
            print("Input must be a number.")
            continue
        if response in range(minimum_number, maximum_number + 1):
            return response
        else:
            print(
                f"Please enter a number between {minimum_number} and {maximum_number}."
            )


def get_guess_feedback(guess, random_number, minimum_number, maximum_number):
    """
    Return a string indicating how far the user's guess is from the random number.

    Args:
        guess (int): The user's initial guess.
        random_number (int): The target number to be guessed.
        minimum_number (int): The minimum value for the random number, inputted by the user.
        maximum_number (int): The minimum value for the random number, inputted by the user.

    Returns:
        str: A response indicating how far the user's guess is from the random number.
    """
    difference = guess - random_number
    absolute_difference = abs(difference)
    percent_difference = (absolute_difference / (maximum_number - minimum_number)) * 100
    if difference < 0:
        if percent_difference <= 10:
            return "You're extremely close. Your guess is too low."
        elif percent_difference <= 25:
            return "You're very close. Your guess is too low."
        elif percent_difference <= 50:
            return "You're somewhat close. Your guess is too low."
        elif percent_difference <= 75:
            return "You're not very close. Your guess is too low."
        else:
            return "You're way off. Your guess is too low."

    else:
        if percent_difference <= 10:
            return "You're extremely close. Your guess is too high."
        elif percent_difference <= 25:
            return "You're very close. Your guess is too high."
        elif percent_difference <= 50:
            return "You're somewhat close. Your guess is too high."
        elif percent_difference <= 75:
            return "You're not very close. Your guess is too high."
        else:
            return "You're way off. Your guess is too high."


def guess_result(random_number, guess, minimum_number, maximum_number):
    """
    Process the guessing loop by comparing the user's guess to the random number until the correct guess is made.
    It also tracks the number of guesses taken.

    Args:
        random_number (int): The target number to be guessed.
        guess (int): The user's initial guess.
        minimum_number (int): The minimum value for the random number, inputted by the user.
        maximum_number (int): The minimum value for the random number, inputted by the user.

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
        else:
            feedback = get_guess_feedback(
                guess, random_number, minimum_number, maximum_number
            )
            print(feedback)
            guess = get_guess("Try again: ", minimum_number, maximum_number)
            guess_count += 1


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


def main():
    """
    Run the 'Guess the Number' game. This function loops, starting a new game each time the user wins,
    and asks whether the user would like to play again. The loop terminates when the user declines to replay.
    """
    while True:
        minimum_number = get_minimum_number("Please enter a minimum value: ")
        maximum_number = get_maximum_number(
            "Please enter a maximum value: ", minimum_number
        )
        random_number = get_random_number(minimum_number, maximum_number)
        guess = get_guess(
            f"Guess a number between {minimum_number} and {maximum_number}: ",
            minimum_number,
            maximum_number,
        )
        guess_result(random_number, guess, minimum_number, maximum_number)
        replay = get_replay("Would you like to play again? (Yes or No): ")
        if replay in ("n", "no"):
            break
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
