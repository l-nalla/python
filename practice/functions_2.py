from random import random
def flip_coin():
    r = random()
    if r > 0.5:
        return "Heads"
    return "Tails"
#for r in range(3):
    #print(flip_coin())
print(flip_coin())

#when we use return keyword then else: condition is unnessecary

def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False
print(is_odd_number(88))

def add(a,b):
    return a+b

def math(a,b, fn=add):
    return fn(a,b)
def subtract(a,b):
    return a-b

print(math(2,2,add))