import random

choices = ["rock", "paper", "scissor"]

print("=====Python Game=====")

while True:
    user = input("\nPick rock, paper, scissor. enter (quit) to exit: ").lower()

    if user == "quit":
        print("Thanks for playing!")
        break
    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    if user == computer:
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissor") or
        (user == "scissor" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        print("You win!")
    else:
        print("Computer win!")