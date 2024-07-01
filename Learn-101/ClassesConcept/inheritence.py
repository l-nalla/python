# Inheritence is a way to create a new class based on an existing class.
# The new class is called the child class, and the existing class is called the parent class.
# The child class inherits all of the attributes and methods of the parent class.
# You can also add new attributes and methods to the child class.
# To create a child class, you use the following syntax:

# class ChildClass(ParentClass):
#     # Add new attributes and methods here

# For example, the following code creates a child class called Child that inherits from the parent class Parent:

# Create a parent class called Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal is speaking")

# Create a child class called Dog that inherits from the Animal class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(self.name + " says: Bark!")

# Create a child class called Cat that inherits from the Animal class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        print(self.name + " says: Meow!")

# Create a dog object
dog = Dog("Rex", "Golden Retriever")

# Create a cat object
cat = Cat("Fluffy", "White")

# Print the name and breed of the dog
print(dog.name + " is a " + dog.breed)

# Print the name and color of the cat
print(cat.name + " is " + cat.color)

# Make the dog speak
dog.speak()

# Make the cat speak
cat.speak()
