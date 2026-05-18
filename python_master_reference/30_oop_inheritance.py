"""
30 - OOP: Inheritance
A child class can inherit from a parent class.
"""

# Create a parent class called Animal.
# This class contains common things that animals can have or do.
class Animal:

    # This method runs automatically when we create an Animal or child object.
    def __init__(self, name):

        # Store the animal's name inside the object.
        self.name = name

    # Create a method called speak.
    # This is a general version for all animals.
    def speak(self):

        print("Animal makes a sound")


# Create a child class called Dog.
# Dog inherits from Animal, so it gets Animal's attributes and methods.
class Dog(Animal):

    # Override the speak method from the Animal class.
    # This means Dog has its own version of speak.
    def speak(self):

        print(f"{self.name} says woof!")

# Create another child class called Cat that also inherits from Animal.
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says mew!")

# Create a Dog object.
# Dog uses the __init__ method from the Animal class.
dog = Dog("Buddy")

cat = Cat("Pishi")

# Call the speak method for the dog and cat objects.
dog.speak()

cat.speak()