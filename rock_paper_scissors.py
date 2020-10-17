import random

choices = ["rock", "paper", "scissors"]
playerScore = 0
computerScore = 0

print("Let's play Rock, Paper, Scissors!")
print("First to 3 wins.")

while True:
    if playerScore >= 3 or computerScore >= 3:
        if playerScore >= 3:
            gameResult = "won"
        else:
            gameResult = "lost"
        print(f"Your score: {playerScore}")
        print(f"Computer score: {computerScore}")
        playAgain = input(f"You {gameResult} the game! Play again? (y) or (n): ")
        playAgain = playAgain.lower().replace(" ", "")
        if playAgain == "y":
            playerScore = 0
            computerScore = 0
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
        playerChoice = input("Enter your choice: ")
        playerChoice = playerChoice.lower().replace(" ", "")
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






