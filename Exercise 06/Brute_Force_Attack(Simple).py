## Exercise 6: Brute Force Attack - 30 Marks

## Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
## 1. Define the correct password.
## 2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
## 3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

## Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.


correct_password = "12345"                                                    ## Defining correct Password
entered_password = input("Enter the password: ")                              ## Asking for Password 

while entered_password != correct_password:                                   ## Loop which keeps asking for password until the correct password is entered
    entered_password = input("Incorrect password. Try again: ")               ## Message for incorrect password

print("Password is correct!")                                                 ## Message for correct password
