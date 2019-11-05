import random
player = input("player make your choice: ").lower()

rand_num = random.randint(0,2)

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "scissor"
else:
    computer = "paper"

print(f"computer plays {computer}")

if player == computer:
    print("It's an tie")
elif player == "rock":
    if computer == "paper":
        print("computer wins!")
    elif computer == "scissor":
        print("player wins!")
elif player == "scissor":
    if computer == "rock":
        print("computer wins!")
    elif computer == "paper":
        print("player wins!")
elif player == "paper":
    if computer == "rock":
        print("player wins!")
    elif computer == "scissor":
        print("computer wins!")
else:
    print("Something went wrong")
