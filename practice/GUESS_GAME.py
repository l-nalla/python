import random
rand_num = random.randint(1,10)
guess = None
while guess != rand_num:
    guess = input("Input your guess: ")
    guess = int(guess)

    if guess >  rand_num:
        print("your too high")
    elif guess < rand_num:
        print("your too low")
    else:
        print(" YOU WON!!!!")
print(rand_num)
