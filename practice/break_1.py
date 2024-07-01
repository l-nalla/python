import random
rand_num = random.randint(1,10)
guess = None
while True:
    guess = input("Input your guess: ")
    guess = int(guess)
    if guess >  rand_num:
        print("your too high")
    elif guess < rand_num:
        print("your too low")
    else:
        print(" YOU WON!!!!")
        print(f"Random Number Genrated is: {rand_num}")
        play_again = input("Do you want to play again (Y/n)? : ")
        if play_again == "y":
            rand_num = random.randint(1,10)
            guess = int(guess)
        else:
            print("Well Played!")
            break
