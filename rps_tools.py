def winning_score(score):
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
