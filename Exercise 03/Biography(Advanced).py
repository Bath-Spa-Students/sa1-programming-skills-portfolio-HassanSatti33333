## Exercise 3: Biography - 25 Marks

## In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
## 1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
## 2. Print the values on separate lines using a single `print()` statement.
## 3. Use variables with appropriate data types for each piece of information.



### Advanced Requirements:
## Have the user input their name, hometown, and age instead of hardcoding the values.
## Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
## Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?

name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

age = None

while age is None:
    age_input = input("Enter your age: ")
    if not age_input.isdigit():
        print("Age must be a number.")
    else:
        age = int(age_input)

Bio = {"Name": name,
    "Hometown": hometown,
    "Age": age}

print(f"Name: {Bio['Name']}\nHometown: {Bio['Hometown']}\nAge: {Bio['Age']}")



