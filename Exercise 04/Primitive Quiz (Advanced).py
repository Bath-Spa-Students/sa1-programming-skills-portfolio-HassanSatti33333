## Exercise 4: Primitive Quiz - 30 Marks

## In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
## 1. Write a program that asks the user "What is the capital of France?" and waits for their response.
## 2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
## 3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
## Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
## Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.

score = 0 

answer = input("What is the capital of France?  " )                   ## Questions the user
if answer.lower() == "paris" :                                      ## Code for Correct Response 
    print ("Answer is Correct")    
    score = score + 1                                               ## Increments score if answer is correct                     
else:                                                               ## Code for Incorrect Response
    print ("Answer is Incorrect")

answer = input("What is the capital of Germany? ")
if answer.lower() == "berlin":
    print("Answer is Correct")
    score += 1
else:
    print("Answer is Incorrect. The correct answer is Berlin.")

answer = input("What is the capital of Italy? ")
if answer.lower() == "rome":
    print("Answer is Correct")
    score += 1
else:
    print("Answer is Incorrect. The correct answer is Rome.")

answer = input("What is the capital of Spain? ")
if answer.lower() == "madrid":
    print("Answer is Correct")
    score += 1
else:
    print("Answer is Incorrect. The correct answer is Madrid.")

answer = input("What is the capital of Portugal? ")
if answer.lower() == "lisbon":
    print("Answer is Correct")
    score += 1
else:
    print("Answer is Incorrect. The correct answer is Lisbon.")

answer = input("What is the capital of Netherlands? ")
if answer.lower() == "amsterdam":
    print("Answer is Correct")
    score += 1
else:
    print("Answer is Incorrect. The correct answer is Amsterdam.")

answer = input("What is the capital of Belgium? ")
if answer.lower() == "brussels":
    print("Answer is Correct")
    score += 1
else:
    print("Answer is Incorrect. The correct answer is Brussels.")

answer = input("What is the capital of Switzerland? ")
if answer.lower() == "bern":
    print("Answer is Correct")
    score += 1
else:
    print("Answer is Incorrect. The correct answer is Bern.")

answer = input("What is the capital of Austria? ")
if answer.lower() == "vienna":
    print("Answer is Correct")
    score += 1
else:
    print("Answer is Incorrect. The correct answer is Vienna.")

answer = input("What is the capital of Sweden? ")
if answer.lower() == "stockholm":
    print("Answer is Correct")
    score += 1
else:
    print("Answer is Incorrect. The correct answer is Stockholm.")

print(f"\nYou got {score} out of 10 questions correct.")                                ## Prints Final score in a new line 