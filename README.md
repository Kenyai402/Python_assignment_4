"""
# Python Person Class Assignment

## Project Description
This project contains a Python class named `Person`, which represents a simple person with attributes like name, age, and gender. The class includes a method called `introduce` that prints a message introducing the person with their details.

## Features
- The `Person` class includes the following attributes:
  - `name`: The person's name.
  - `age`: The person's age.
  - `gender`: The person's gender.
  
- The `introduce` method prints out a simple introduction in the following format:


## Code Example

Here's an example of how the `Person` class works:

  # Creating an instance of the Person class
  person1 = Person("Keren", 21, "Female")

  # Calling the introduce method to display the person's information
  person1.introduce()

Output:

  Hello! My name is Keren. I am 21 years old, and I am Female.

## How to Run the Project
1. **Clone the repository** to your local machine using the following command:
  git clone https://github.com/your-username/your-repository.git

2. **Navigate to the project directory**:
  cd your-repository

3. **Run the Python file**:
  python person.py

Make sure you have Python installed on your machine to run the project. You can download Python [here](https://www.python.org/downloads/).

## Files in the Repository
- `person.py`: Contains the code for the `Person` class and an example of how to create and introduce a person.

## Repository Link
The project repository can be found at: https://github.com/your-username/your-repository

## License
This project is licensed under the MIT License - see the LICENSE file for details.
"""

# Python Code for Person Class

class Person:
  def __init__(self, name, age, gender):
      # Constructor to initialize the attributes
      self.name = name
      self.age = age
      self.gender = gender
  
  def introduce(self):
      # Method to introduce the person with their name, age, and gender
      print(f"Hello! My name is {self.name}. I am {self.age} years old, and I am {self.gender}.")

# Example of using the Person class
if __name__ == "__main__":
  # Creating an instance of the Person class
  person1 = Person("Keren", 21, "Female")

  # Calling the introduce method to display the person's information
  person1.introduce()
