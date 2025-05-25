# Assignment: Explore Loops in Python
# Using for and while Loops to solve practical problems!

# Task 1 - Counting Down with Loops

# asks user to enter a starting number
user = int(input("Please enter a starting number:"))

# counts down until 1: loops until user's starting input drops down to 1
while user >= 1:
    print(user, end = " ") # prints the info
    user = user - 1
print("Blast off! 🚀")

# Task 2 - Multiplication Table with for Loops

# prompts user to input a starting number
num = int(input("Please enter a starting number:"))

# for loop to writing the multiplication table starting at 1 and ending at 10
for i in range(1, 11):
    print(str(num) + " x " + str(i) + " =" , num*i, end = " ")

# Task 3 - Find the Factorial

# prompt user to enter a num
num2 = int(input("\nPlease enter a number:"))

# declar a fact variable and assign it with the number entered
factorial = num2

# apply the factorial algorithm
for i in range(1, num2):
    factorial *= i

# print the result
print("The factorial of " + str(num2) + " is " + str(factorial) + ".")