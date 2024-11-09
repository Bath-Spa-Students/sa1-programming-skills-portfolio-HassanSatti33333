## Exercise 6: Brute Force Attack - 30 Marks

## Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
## 1. Define the correct password.
## 2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
## 3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

## Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.


correct_password = "12345"                                                   ## Defining correct Passwrd
max_attempts = 5                                                             ## Defining Max attempts allowed
attempts = 0                                                                 ## Defining Current Attempts 

while attempts < max_attempts:                                               ## Code that Loops while attempts are less than 5 
    entered_password = input("Enter the password: ")                         ## Asking user to enter password
    if entered_password == correct_password:                                 
        print("Password is correct!")                                        ## If password is correct it breaks the code
        break
    else:
        attempts += 1                                                        
        if attempts < max_attempts:
            print(f"Incorrect password. You have {max_attempts - attempts} attempt(s) left.")                                             ## If password is incorrect increments attempts, displays a incorrect msg and shows you how many attemps are left 
        else:
            print("Incorrect password. You have reached the maximum number of attempts. Authorities have been alerted.")                  ## If attempts are finished displays message about authorities being informed