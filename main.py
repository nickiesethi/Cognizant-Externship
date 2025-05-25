
# Task 1 - VariablesL: Your First Python Intro
name = "Nickie"
age = 20
height = 5.3
print("Hey! I am " + name + " :) I am " + str(age) + " years old and " + str(height) + " tall")

# Task 2 - Operators: Playing with Numbers
num1 = 40
num2 = 80

# Addition
print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(num1 + num2))

# Subtraction
print("The different between " + str(num1) + " and " + str(num2) + " is " + str(num1 - num2))
 
# Multiplication
print("The multiplication of " + str(num1) + " and " + str(num2) + "i s " + str(num1 * num2))

# Division
print("The division of " + str(num1) + " and " + str(num2) + " is " + str(num1 / num2))

# Task 3 - Conditional Statements: The Number Checker

userInput = input("Enter a number! I will tell you whether it is 0, positive, or negative!")
    
if int(userInput) > 0:
    print("This number is positive. Awesome!")
elif int(userInput) < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")

