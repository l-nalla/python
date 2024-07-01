import random
player_wins = 0
computer_wins = 0
while_loop = 5
while player_wins < while_loop and computer_wins < while_loop:
    player = input("Make your opinion: ").lower()
    rand_num = random.randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "sciccor"
    else:
        computer = "paper"
    print(f"computer playes {computer}")
    if player == computer:    
        print("It's a TIE")
    elif player == "rock":
        if computer == "sciccor":
            print("player wins!")
            player_wins += 1
        elif computer == "paper":
            print("computer wins!")
            computer_wins += 1
    elif player == "sciccor":
        if computer == "rock":
            print("computer wins!")
            computer_wins += 1
        elif computer == "paper":
            print("player wins!")
            player_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins!")
            player_wins += 1
        elif computer == "sciccor":
            print("computer wins!")
            computer_wins += 1
    else:
        print("Input a valid option")
    print(f"computer_wins:{computer_wins} and player_wins {player_wins}")