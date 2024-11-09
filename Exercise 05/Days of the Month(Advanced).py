## Exercise 5: Days of the Month - 30 Marks

## Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
## 1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
## 2. Input Handling: Ask the user to input the month number.
## 3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
### Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.



month_days = {                                 ## Making a dictionary for each month and the no. of days in that month
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
   
month_number = int(input("Enter the month number (1-12): "))                                          ## Asking user for month number                            


if 1 <= month_number <= 12:                                                                           ## Making sure month number is valid 
    if month_number == 2:                                                                             ## Checking if the selected month is February
        leap_year = input("Is this a leap year? (yes/no): ").lower()                                  ## Asking user if it is Leap Year or not
        if leap_year == "yes":
            month_days[2] = 29                                                                        ## Reassigning value for Leap Year 
    print(f"The number of days in month {month_number} is {month_days[month_number]}")                ## Output for valid month numbers
else:
    print("Invalid month number! Please enter a number between 1 and 12.")                            ## Output for invalid numbers 