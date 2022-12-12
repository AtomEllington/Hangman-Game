import random

# Set up some variables to keep track of the game
word_list = ["apple", "banana", "orange", "strawberry"]
word = random.choice(word_list)
guesses = []
max_guesses = 6

# Start the game
print("Welcome to Hangman!")
while True:
    # Print the current state of the game
    print("\nWord: ", end="")
    for letter in word:
        if letter in guesses:
            print(letter, end="")
        else:
            print("_", end="")
    print("\n")

    # Check if the game is over
    if set(word) == set(guesses):
        print("Congratulations! You won!")
        break
    if len(guesses) >= max_guesses:
        print("Sorry, you lost. The word was '" + word + "'.")
        break

    # Get the next guess from the user
    guess = input("Guess a letter: ")
    if guess in word:
        guesses.append(guess)
    else:
        print("Incorrect! You have " + str(max_guesses - len(guesses)) + " guesses left.")
        guesses.append(guess)
