for num in range(1,20):
    if num == 6 or num == 12:
        print(f"{num} is unlucky")
    elif num % 2 == 0:    
        print(f"{num} is even")    
    else:
        print(f"{num} is odd")
