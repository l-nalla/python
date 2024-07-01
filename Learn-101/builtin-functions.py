# A function is a block of code which only runs when it is called.

# Built-in functions in Python

# Mathematical functions
print(abs(-42))  # Absolute value
print(pow(2, 3))  # Exponentiation
print(max(3, 1, 4, 1))  # Maximum value
print(min(3, 1, 4, 1))  # Minimum value
print(round(3.14159, 2))  # Rounding

# String functions
print(len("Hello world"))  # String length
print("Hello world".upper())  # Convert to uppercase
print("Hello world".lower())  # Convert to lowercase
print("Hello world".strip())  # Remove leading/trailing whitespace
print("Hello world".split())  # Split into a list of words

# List functions
print(len([1, 2, 3]))  # List length
print([1, 2, 3].append(4))  # Add an element to the end of a list
print([1, 2, 3].pop())  # Remove and return the last element from a list
print([1, 2, 3].sort())  # Sort a list in ascending order
print([1, 2, 3].reverse())  # Reverse the order of a list

# Dictionary functions
print(len({"key1": "value1", "key2": "value2"}))  # Dictionary length
print({"key1": "value1", "key2": "value2"}.keys())  # Get the keys of a dictionary
print({"key1": "value1", "key2": "value2"}.values())  # Get the values of a dictionary
print({"key1": "value1", "key2": "value2"}.items())  # Get the key-value pairs of a dictionary

# File functions
print(open("myfile.txt", "r").read())  # Read the contents of a file
print(open("myfile.txt", "w").write("Hello world"))  # Write to a file
print(open("myfile.txt", "a").write("Hello world"))  # Append to a file
print(open("myfile.txt", "r").close())  # Close a file
