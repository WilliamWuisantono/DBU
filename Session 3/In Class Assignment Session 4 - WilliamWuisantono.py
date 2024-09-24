# Exercise 1: Request user input and print a greeting
# Print a greeting message using the user's name
print("Excercise 1:")
User = input("What is your name?")
print(f'hello {User}!')

print("\n\n")
# Exercise 2: Variables and Data Types
# Create two drinks variable (Milk and Water) and swap their values
# Print the old and new values of the variables
print("Exercise 2:")
milk = "Milk"
water = "Water"
print("Old Values:" + milk + " and " + water)

milk, water = water, milk

print("new Values:" + milk + " and " + water)

print("\n\n")


# Exercise 3: String Concatenation
# Create two variables with your first and last name, and print them together
print("Exercise 3:")
fname = 'William'
lname = 'Wuisantono'

print(f'{fname} {lname}')
print("\n\n")


# Exercise 4: Simple Arithmetic
# Perform basic arithmetic operations and print the results
# Addition, Subtraction, Multiplication, Division
print("Exercise 4:")
num1 = 4
num2 = 4

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multipication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print("\n\n")


# Exercise 5: Lists
# Create a list of 5 numbers and print the first and last element
print("Exercise 5:")

list = [1, 2, 3, 4, 5]

print(f"First: {list[0]}")
print(f"Last: {list[-1]}")
print("\n\n")


# Exercise 6: For Loop
# Use the list from Ex.5. Print each element in the list of numbers using a for loop
print("Exercise 6:")

list = [1, 2, 3, 4, 5]

for i in list:
    print(i)

print("\n\n")


# Exercise 7: If-Else Condition
# Write an if-else statement to check if a number is greater than or equal to 10
print("Exercise 7:")

num = int(input("What is your number: "))

if num >= 10:
    print("Your number is greater than or equal to 10.")
else:
    print("Your number is lesser than 10.")
print("\n\n")

# Exercise 8: Functions
# Create a function that takes a name as input and prints a greeting
print("Exercise 8:")

def greet(name):
    print(f"Hello {name}! Nice to meet you")

name = input("What is your name?")

greet(name)

print(greet)
print("\n\n")

# Exercise 9: Dictionaries
# Create a dictionary with three key-value pairs and print the value of one key
print("Exercise 9:")
car = {
  "brand": "Toyota",
  "model": "Camry",
  "year": 2023
}

print(car["year"])
print("\n\n")

# Exercise 10: While Loop
# Write a while loop that prints numbers from 1 to 5
print("Exercise 10:")
number = 1

while number <= 5:
    print(number)
    number += 1
print("\n\n")

# Exercise 11: String Formatting
# Task: Format the following variables into a string: "name", "age", and "city"
# Example output: "John is 30 years old and lives in New York."
print("Exercise 11:")
name = "John"
age = 30
city = "New York"

string = f"{name} is {age} years old and lives in {city}."

print(string)
print("\n\n")

# Exercise 12: Function with Default Arguments
# Task: Write a function that takes two numbers and an optional operation (add, subtract, multiply, divide).
# If no operation is provided, it defaults to addition.
print("Exercise 12:")

def calculate(num1, num2, operation="add"):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'division':
        return num1 / num2
    else:
        print("Your operation is not valid.")

# Example usage:
print(calculate(5, 3))  # Expected output: 8
print(calculate(5, 3, "subtract"))  # Expected output: 2

print("\n\n")

# Exercise 13: Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
# Task: Create a list of years [1990, 1991, 1992, 1993, 1994, 1995] and generate a new list with the approximate age of a person born in that year.
# To generate a new list, start with an empty list [], and use append() to add elements to it.
print("Exercise 13:")
years = [1990, 1991, 1992, 1993, 1994, 1995]

age = []
for year in years:
    age.append(2024 - year)

print(age)