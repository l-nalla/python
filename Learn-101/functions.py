# User defined functions are blocks of code that can be reused throughout a program.
# They are defined using the def keyword, followed by the function name and parentheses.
# The function body is indented below the function definition.

def my_function():
    """
    This function prints a message to the console.
    """
    print("Hello, world!")

# To call a function, simply use its name followed by parentheses.
my_function()

# Function with parameters and type annotations and a return value.
def sum_numbers(a: int, b: int) -> int:
    """
    This function takes two integers as parameters and returns their sum.
    """
    return a + b

print(sum_numbers(12, 34))