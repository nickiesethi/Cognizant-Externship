
def multiply(num1, num2):
    try:
        return int(num1) * int(num2)
    except ValueError:
        print("Invalid input! Please enter a valid number")
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        return multiply(num1, num2)

def divide(num1, num2):
    try:
        return int(num1) / int(num2)
    except ValueError:
        print("Invalid input! Please enter a valid number")
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        return divide(num1, num2)
    except ZeroDivisionError:
        print("Oops! Division by zero is not allowed")
        num2 = input("Enter the second number: ")
        return divide(num1, num2)
    
def subtract(num1, num2):
    try:
        return int(num1) - int(num2)
    except ValueError:
        print("Invalid input! Please enter a valid number")
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        return subtract(num1, num2)

def add(num1, num2):
    try:
        return int(num1) + int(num2)
    except ValueError:
        print("Invalid input! Please enter a valid number")
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

def menu():
    while True:
        try:
            prompt = input("Welcome to the Error-Free Calculator! Choose an operation:\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Exit\n")
            if prompt not in ["1", "2", "3", "4", "5"]:
                print("Please select a number between 1 - 5.")
                return menu()
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
        except ValueError:
            print("Invalid input! Please enter a valid number")
            return menu()
        try:
            if prompt == "1":
                res = add(num1, num2)
            elif prompt == "2":
                res = subtract(num1, num2) 
            elif prompt == "3":
                res = multiply(num1, num2)
            elif prompt == "4":
                res = divide(num1, num2)
            elif prompt == "5":
                print("Exiting the program.")
                return False
        except ValueError:
            print("Invalid input! Please enter a valid number")
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
        else:
            print(f"The result is: " + str(res))
menu()