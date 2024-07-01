age = input("How old are you")
if age:
    age = int(age)
    if age >=21:
        print("You are allowed to drink")
    elif age >=18:
        print("You are not supposed to drink at this age")
    else:
        print("Your too young at thid age")
else:
    print("enter a age")
