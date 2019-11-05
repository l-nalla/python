print("rock")
print("scissors")
print("paper")

player1 = input("Player1  choice: ")
player2 = input("Player2 choice: ")

if player1 == "rock":
    if player2 == "scissor":
        print("player1 wins!")
    elif player2 == "paper":
        print("plaryer2 wins!")
elif player1 == "scissor":
    if player2 == "rock":
        print("player2 wins!")
    elif player2 == "paper":
        print("player1 wins!")
elif player1 == "paper":
    if player2 == "scissor":
        print("player2 wins!")
    elif player2 == "rock":
        print("player1 wins!")
elif player1 == player2:
    print("It's a Tie")
else:
    print("something went wrong")
