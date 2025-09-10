import random


def play_hangman():
    """Plays a simple text-based Hangman game."""

    # 1. Predefined list of words
    words = ["python", "hangman", "computer", "programming", "developer"]

    # 2. Randomly select a word
    word_to_guess = random.choice(words).upper()

    # 3. Initialize game state
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Let's play Hangman! 🤖")

    # Main game loop
    while incorrect_guesses < max_incorrect_guesses:

        # Display the current state of the word
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord to guess: " + display_word)
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")

        # Check for a win
        if "_" not in display_word:
            print("\nCongratulations! You won! 🎉")
            break

        # Get player's guess
        guess = input("Guess a letter: ").upper()

        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add guess to the list
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word_to_guess:
            print("Correct guess! 👍")
        else:
            print("Incorrect guess. 👎")
            incorrect_guesses += 1

    # After the loop ends, determine if the player lost
    if incorrect_guesses >= max_incorrect_guesses:
        print("\nGame over! You lost. 😭")
        print(f"The word was: {word_to_guess}")


# Start the game
play_hangman()