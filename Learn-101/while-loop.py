# A while loop is a control flow statement that allows code to be executed repeatedly as long as a certain condition is true.
# The syntax of a while loop is:
#while condition:
    # code to be executed
# Example 1: Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# Example 2: Calculate the factorial of a number
n = 5
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print(factorial)

# Example 3: Read input from the user until they enter a blank line
while True:
    line = input("Enter a line: ")
    if not line:
        break
    print(line)
