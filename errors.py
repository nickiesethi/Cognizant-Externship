# Task 1 - Understanding Python Exceptions

prompt = int(input("Enter a number: "))
while(1):
    try:
        ans = 100/prompt
        print("100 divided by " + str(prompt) + " is: " + str(ans))
        break
    except ZeroDivisionError:
        print("You cannot divide by zero!")
        prompt = int(input("Enter a number: "))
    except ValueError:
        print("Error: Please enter a valid number")
        prompt = int(input("Enter a number: "))
    
    
# Task 2 - Types of Exceptions
array = [2, 4, 5]
word = "hey"
try: 
    print(array[9])
    print(word + 9)
# if index is out of range
except IndexError:
    print("IndexError occurred! List index out of range.")
 
try: 
    dict = {"name": "Nickie", "age": 20}
    print(dict['school'])
# if key is not found in the dictionary
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# if different data types are used in an operation
try:
    print("Nickie" + 20)
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

# Task 3 - Types of Exceptions
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

try:
    result = num1 / num2
    print(f"The result of " + str(num1) + " divided by " + str(num2) + " is: " + str(result))
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
else:
    print("The result is " + str(result))
finally:
    print("This block always executes")

