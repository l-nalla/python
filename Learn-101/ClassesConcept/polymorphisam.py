# Class Polymorphism in Python
# Polymorphism allows us to define methods in the parent class that have the same name as methods in the child class.
# The method in the child class overrides the method in the parent class.
# This allows us to use the same method name to perform different tasks depending on the object type.

class Animal:
    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def speak(self):
        print("Dog - Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat - Meow!")

# Create a Dog object
dog = Dog()

# Create a Cat object
cat = Cat()

# Call the speak() method on the Dog object
dog.speak()  # Output: Woof!

# Call the speak() method on the Cat object
cat.speak()  # Output: Meow!
