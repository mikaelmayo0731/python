import random, time

words = ["train", "computer", "spaghetti"]
gameWord = random.choice(words)
output = ""
guesses = []
lives = 3

print("Let's play hangman!")

time.sleep(1)

while True:
    output = ""
    for letter in gameWord:
        if letter in guesses:
            output += letter
        else:
            output += "_"
    if output == gameWord:
        print(f"You win! The word was {gameWord}.")
        break
    elif lives <= 0:
        print(f"No more lives, you lose! The word was {gameWord}.")
        break
    print(output)
    print(f"Lives left: {lives}")
    letter_guess = str(input("Enter guess: ")).lower().replace(" ", "")
    time.sleep(1)
    if letter_guess in guesses:
        print(f"You already guessed the letter {letter_guess}.")
    elif letter_guess in gameWord:
        guesses.append(letter_guess)
        print(f"There are {gameWord.count(letter_guess)} letter {letter_guess}!")
    elif letter_guess not in gameWord:
        print("Guess not in word!")
        lives -= 1
    else:
        print("Invalid entry!")



