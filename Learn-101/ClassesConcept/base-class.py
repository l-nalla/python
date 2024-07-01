# A class is a blueprint for creating objects (instances).
# Objects have methods (functions) and attributes (variables).
# Classes are created using the class keyword.
# The __init__() method is called automatically when an object is created.
# The self parameter is a reference to the current instance of the class.
# Attributes are accessed using the dot operator.
# Methods are called using the dot operator.

class MyClass:
    """
    This class represents a simple object with a name and a method to say hello.
    """

    def __init__(self, name):
        """
        This method initializes the object with a name.

        Args:
            name (str): The name of the object.
        """
        self.name = name # This is an attribute of the object

    def say_hello(self): # This is a method of the object
        """
        This method prints a greeting message with the object's name.
        """
        print(f"Hello, {self.name}!")


my_object = MyClass("William")
my_object.say_hello()  # Output: Hello, {name}