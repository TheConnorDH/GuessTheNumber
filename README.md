# Guess the Number Game

A fun, interactive Python game where the user sets a custom range and then tries to guess a randomly generated number within that range. The game provides dynamic feedback based on how close the guess is to the target number, and it allows the user to play multiple rounds.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Custom Range Selection:** The user inputs a minimum and maximum value for the random number.
- **Input Validation:** All inputs (range values, guesses, replay decisions) are validated to ensure correct data types and logical values.
- **Dynamic Feedback:** After each guess, the game tells the user whether their guess is too high or too low. Feedback is nuanced based on how far the guess is from the target number (e.g., "You're extremely close" vs. "You're way off").
- **Guess Counter:** The game tracks and displays the number of guesses it takes for the user to get the correct answer.
- **Replay Option:** After each round, the user is prompted to play again or exit the game.

## Installation

1. Ensure you have [Python 3.6 or higher](https://www.python.org/downloads/) installed.
2. Clone this repository or download the source code.
3. Open a terminal (or command prompt) and navigate to the project directory.
4. Run the game with:

   ```bash
   python main.py
   ```

## Usage

- **Custom Range:** When prompted, enter the minimum and maximum values to define the range.
- **Guessing:** Input your guess when prompted. The game will tell you if your guess is too high or too low, along with dynamic feedback.
- **Winning:** When you guess the number correctly, the game will display a congratulatory message along with the number of attempts.
- **Replay:** After each game, you'll be asked if you want to play again.

## Code Overview

- `get_minimum_number(prompt)`: Prompts for and validates the minimum value.
- `get_maximum_number(prompt, minimum_number)`: Prompts for and validates the maximum value.
- `get_random_number(minimum_number, maximum_number)`: Generates a random number within the specified range.
- `get_guess(prompt, minimum_number, maximum_number)`: Prompts for and validates the user's guess.
- `get_guess_feedback(guess, random_number, minimum_number, maximum_number)`: Returns a feedback message based on the guess.
- `guess_result(random_number, guess, minimum_number, maximum_number)`: Handles the main guessing loop and tracks attempts.
- `get_replay(prompt)`: Prompts for and validates whether the user wants to play again.
- `main()`: Ties everything together and runs the game loop.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Developed as a beginner project to practice Python programming, input validation, and modular coding practices.
