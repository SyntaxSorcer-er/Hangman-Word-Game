import random
import os


class HangmanGame:
    def __init__(self):
        self.words = ["python", "hangman", "program", "computer", "keyboard"]
        self.max_attempts = 6
        self.reset_game()

    def reset_game(self):
        self.secret_word = random.choice(self.words)
        self.guessed_letters = []
        self.attempts_left = self.max_attempts
        self.game_over = False
        self.won = False

    def display_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🎮 HANGMAN GAME")
        print("===============\n")

        # Display hangman progress
        hangman_stages = [
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               |
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / 
               |
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   
               |
            """,
            """
               ------
               |    |
               |    O
               |   /|
               |   
               |
            """,
            """
               ------
               |    |
               |    O
               |    |
               |   
               |
            """,
            """
               ------
               |    |
               |    O
               |   
               |   
               |
            """,
            """
               ------
               |    |
               |    
               |   
               |   
               |
            """
        ]

        print(hangman_stages[self.attempts_left])

        # Display word progress
        display_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(f"Word: {display_word}")
        print(f"Attempts left: {self.attempts_left}")
        print(f"Guessed letters: {', '.join(self.guessed_letters)}")

        if self.game_over:
            if self.won:
                print("\n🎉 Congratulations! You won!")
            else:
                print(f"\n💀 Game over! The word was: {self.secret_word}")
            print("\nPress 'n' for a new game or 'q' to quit")

    def make_guess(self, letter):
        if letter in self.guessed_letters:
            return

        self.guessed_letters.append(letter)

        if letter not in self.secret_word:
            self.attempts_left -= 1

        # Check win condition
        won = True
        for secret_letter in self.secret_word:
            if secret_letter not in self.guessed_letters:
                won = False
                break

        if won:
            self.game_over = True
            self.won = True
            return

        # Check lose condition
        if self.attempts_left <= 0:
            self.game_over = True
            self.won = False

    def play(self):
        while True:
            self.display_game()

            if self.game_over:
                choice = input().lower()
                if choice == 'n':
                    self.reset_game()
                    continue
                elif choice == 'q':
                    break
                else:
                    continue

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter!")
                continue

            self.make_guess(guess)


if __name__ == "__main__":
    game = HangmanGame()
    game.play()