## Exercise 7: Some Counting - 20 Marks

## Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console in each case.
## * Write a loop that counts up from 0 to 50 in increments of 1.
## * Write a loop that counts down from 50 to 0 in decrements of 1.
## * Write a loop that counts up from 30 to 50 in increments of 1.
## * Write a loop that counts down from 50 to 10 in decrements of 2.
## * Write a loop that counts up from 100 to 200 in increments of 5.
## *You may include all loops in a single project*




print("Counting up from 0 to 50:")                                     # Loop that counts up from 0 to 50 in increments of 1
i = 0
while i <= 50:
    print(i, end=", ")
    i += 1
print("\n")


print("Counting down from 50 to 0:")                                   # Loop that counts down from 50 to 0 in decrements of 1
i = 50
while i >= 0:
    print(i, end=", ")
    i -= 1
print("\n")


print("Counting up from 30 to 50:")                                    # Loop that counts up from 30 to 50 in increments of 1
i = 30
while i <= 50:
    print(i, end=", ")
    i += 1
print("\n")


print("Counting down from 50 to 10 in decrements of 2:")               # Loop that counts down from 50 to 10 in decrements of 2
i = 50
while i >= 10:
    print(i, end=", ")
    i -= 2
print("\n")


print("Counting up from 100 to 200 in increments of 5:")                # Loop that counts up from 100 to 200 in increments of 5
i = 100
while i <= 200:
    print(i, end=", ")
    i += 5
print("\n")
