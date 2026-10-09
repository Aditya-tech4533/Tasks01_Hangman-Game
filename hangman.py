import random

# Predefined list of 5 words
words = ["python", "apple", "tiger", "school", "computer"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_attempts:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses left:", max_attempts - wrong_guesses)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if wrong_guesses == max_attempts:
    print("Game over! The word was:", word)
elif all(letter in guessed_letters for letter in word):
    print("The word was:", word)
