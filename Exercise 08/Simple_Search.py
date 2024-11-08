## Exercise 8: Simple Search - 30 Marks

## Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
## 1. Allow the user to input the search term instead of using a predefined value.
## 2. Implement the search functionality based on user input.



namelist = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

name = input("Enter the name you want to search for (Case Sensitive): ")

if name in namelist:
    print(f"{name} was found in the list.")
else:
    print(f"{name} was not found in the list.")
