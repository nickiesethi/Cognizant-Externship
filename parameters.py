def add_numbers(num1, num2):
    sum = num1 + num2
    print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum))

def greet_user(name):
    print("Hello, " + name + "! Welcome abroad.", end = " ")

def describe_pet(pet_name, animal_type):
    print("I have a " + animal_type + " named " + pet_name + ".", end = " ")

def make_sandwich(*list):
    print("\nMaking a sandwich with the following ingredients: ", end = "")
    for i in list:
        print(i)

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

# Greet User
user = input("What is your name?")
num1 = int(input("Enter two numbers you want to add: "))
num2 = int(input())
greet_user(user)

# Adding Numbers
add_numbers(num1, num2)

# Describe pet
pet_type = input("What pet do you have and what is its name?")
pet_name = input()
describe_pet(pet_name, pet_type)

# Make Sandwitch
ingredients = ["lettuce", "tomato", "potato", "ham"]
make_sandwich(ingredients)

# Recursion to Calculate Factorial
answer = input("Enter a number to calculate the factorial: ")
fact = factorial(int(answer))
print("The factorial of " + str(answer) + " is " + str(fact) + ".", end = " ")

f = int(input("\nEnter a number to calculate the Fibonacci number: "))
result = fibonacci(f)
print("The " + str(f) + "th Fibonacci number is " + str(result) + ".")
