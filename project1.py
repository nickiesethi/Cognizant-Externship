
# Hello there, input your age and I will let you know if you are an eligible elector or not!!

# Takes in input and converts it to an integer
age = int(input("How old are you? "))

# if the age is 18 or above, we print the following information
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
# Otherwise, we find how many years it will take for them to become eligible
else: 
    x = 18 - age # by using subtraction
    print("Oops! You’re not eligible yet. But hey, only " + str(x) + " more years to go!")

