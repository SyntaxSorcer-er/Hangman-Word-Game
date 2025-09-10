import random

def play_hangman():
    """
    Plays a simple text-based Hangman game.

    The game's rules are based on the user's specified scope:
    - Uses a small, predefined list of words.
    - The player has a maximum of 6 incorrect guesses.
    - All input and output is handled through the console.
    """

    # 1. Predefined list of words as per the simplified scope
    words = ["PYTHON", "PROGRAMMING", "COMPUTER", "DEVELOPER", "ALGORITHM"]

    # 2. Randomly select a word from the list and convert it to uppercase
    word_to_guess = random.choice(words)

    # 3. Initialize game state variables
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Let's play Hangman! 🤖")
    print(f"I've picked a word. You have {max_incorrect_guesses} chances to guess it.")

    # Main game loop. It continues as long as the player has guesses left.
    while incorrect_guesses < max_incorrect_guesses:

        # Display the current state of the word, showing guessed letters and underscores
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord to guess: " + display_word)
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        # Check for a win condition before getting the next guess
        if "_" not in display_word:
            print("\nCongratulations! You won! 🎉")
            break # Exit the loop, as the game is over

        # Get player's guess and convert to uppercase for case-insensitive matching
        guess = input("Guess a letter: ").upper()

        # Validate the guess to ensure it's a single, new letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the valid guess to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guess is correct or incorrect
        if guess in word_to_guess:
            print("Correct guess! 👍")
        else:
            print("Incorrect guess. 👎")
            incorrect_guesses += 1

    # After the loop, check if the game ended due to running out of guesses
    if incorrect_guesses >= max_incorrect_guesses:
        print("\nGame over! You lost. 😭")
        print(f"The word was: {word_to_guess}")

# Start the game
play_hangman()
