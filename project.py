import turtle

def factorial(num):
    fact = num
    if fact == 1:
        return fact
    
    return fact * factorial(fact - 1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

print("\nMenu of Recursive Functions:")
print("1. Calculate the factorial of a number")
print("2. Find the nth Fibonacci number")
print("3. Exit")
        
choice = input("Enter your choice (1-4): ")
        
if choice == "1":
    num = int(input("Enter a number for factorial calculation: "))
    print("Factorial of " + str(num) + " is " + str(factorial(num)))
elif choice == "2":
    num = int(input("Enter a number for Fibonacci sequence: "))
    print("The "+ str(num) + " th Fibonacci number is "+ str(fibonacci(num)))
elif choice == "3":
    print("Exiting the program. Goodbye!")     
else:
    print("Invalid choice! Select a number between 1 and 3.")