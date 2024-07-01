# Type casting is the process of converting one data type to another.
# There are two types of type casting in Python: implicit and explicit.

# Implicit type casting
a = 10  # integer
b = 10.5  # float
c = a + b  # c will be a float (10.5)
print("a:", type(a), "b:", type(b), "c:", type(c))

# Explicit type casting
a = 10  # integer
b = "10.5"  # string
c = float(b)  # c will be a float (10.5)
print("a:", type(a), "b:", type(b), "c:", type(c))

a = 10.5  # float
b = "10"  # string
c = int(a)  # c will be an integer (10)
print("a:", type(a), "b:", type(b), "c:", type(c))

a = "10"  # string
b = 10.5  # float
c = str(b)  # c will be a string ("10.5")
print("a:", type(a), "b:", type(b), "c:", type(c))
