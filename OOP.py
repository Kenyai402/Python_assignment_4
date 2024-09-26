class Person:
    def __init__(self, name, age, gender):
        # Constructor to initialize the attributes
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        # Method to introduce the person with their name, age, and gender
        print(f"Hello! My name is {self.name}. I am {self.age} years old, and I am {self.gender}.")

# Creating an instance of the Person class
person1 = Person("Keren", 21, "Female")

# Calling the introduce method to display the person's information
person1.introduce()
