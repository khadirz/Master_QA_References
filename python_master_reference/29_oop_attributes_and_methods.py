"""
29 - OOP: Attributes and Methods
Attributes are data inside an object.
Methods are actions inside a class.
"""

# Create a class called Person.
# A class is a blueprint for creating person objects.
class Person:

    # This method runs automatically when we create a new Person object.
    def __init__(self, name, age):

        # Store the person's name inside the object.
        self.name = name

        # Store the person's age inside the object.
        self.age = age

    # Create a method called introduce.
    # This method belongs to the Person class.
    def introduce(self):

        # Print a sentence using the object's name and age.
        print(f"My name is {self.name} and I am {self.age} years old.")


# Create a list of Person objects and save it in the variable persons.
persons = [
    Person("Khadir", 56),
    Person("Jaakko", 44)
]

# Loop through the list of persons and call the introduce method for each person.
for person in persons:
    person.introduce()
