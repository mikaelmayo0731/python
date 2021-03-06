import random, time

choices = ["rock", "paper", "scissors"]
playerScore = 0
computerScore = 0
score = 0


print("Let's play Rock, Paper, Scissors!")

while True:
    try:
        score = int(input("Enter the score you want to play to: "))
    except ValueError:
        print("Invalid entry!")
        continue
    if score <= 0:
        print("Score must be higher than 0.")
    else:
        break

while True:
    if playerScore >= score or computerScore >= score:
        if playerScore >= score:
            gameResult = "won"
        else:
            gameResult = "lost"
        print(f"Your score: {playerScore}")
        print(f"Computer score: {computerScore}")
        playAgain = input(f"You {gameResult} the game! Play again? (y) or (n): ").lower().replace(" ", "")
        if playAgain == "y":
            playerScore = 0
            computerScore = 0
            while True:
                try:
                    score = int(input("Enter the score you want to play to: "))
                except ValueError:
                    print("Invalid entry!")
                    continue
                if score <= 0:
                    print("Score must be higher than 0.")
                else:
                    break
        elif playAgain == "n":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice!")
            continue
    else:
        print(f"Your score: {playerScore}")
        print(f"Computer score: {computerScore}")
        computerChoice = random.choice(choices)
        playerChoice = input("Enter your choice: ").lower().replace(" ", "")
        time.sleep(.5)
        if playerChoice == computerChoice:
            print(f"The computer chose {computerChoice}, it's a draw!")
        elif playerChoice == "rock":
            if computerChoice == "paper":
                print(f"The computer chose {computerChoice}, you lose!")
                computerScore += 1
            elif computerChoice == "scissors":
                print(f"The computer chose {computerChoice}, you win!")
                playerScore += 1
        elif playerChoice == "paper":
            if computerChoice == "scissors":
                print(f"The computer chose {computerChoice}, you lose!")
                computerScore += 1
            elif computerChoice == "rock":
                print(f"The computer chose {computerChoice}, you win!")
                playerScore += 1
        elif playerChoice == "scissors":
            if computerChoice == "rock":
                print(f"The computer chose {computerChoice}, you lose!")
                computerScore += 1
            elif computerChoice == "paper":
                print(f"The computer chose {computerChoice}, you win!")
                playerScore += 1
        else:
            print("Invalid choice!")
