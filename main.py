import random

WORDS = ["python", "computer", "internship", "program", "developer"]
MAX_WRONG_GUESSES = 6


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("=== Hangman Game ===")
    print(f"Guess the word one letter at a time. You have {MAX_WRONG_GUESSES} incorrect guesses.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        display_word = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses remaining: {MAX_WRONG_GUESSES - wrong_guesses}")
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            return

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)
        if guess in word:
            print("Correct!")
        else:
            wrong_guesses += 1
            print("Incorrect!")

    print(f"\nGame over! The word was: {word}")


if __name__ == "__main__":
    play_hangman()
