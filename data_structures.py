
# Task 1: Create a list of favorite fruits
fruits = ["apple", "strawberry", "banana", "grapes", "blueberry"]

fruits.append("pineapple")
fruits.remove("banana")

print(fruits[::-1])

# Task 2 - Exploring Dictionaries
dict = {"name" : "Nickie", "age":20, "city": "Orlando"}

dict["favorite_color"] = "Purple"

dict["city"] = "Miami"

print("Keys: ", end="")
for i in dict:
    print(str(i) + "," , end=" ")

print(' ')

print("Values: ", end="")
for j in dict:
    print(str(dict[j]), end = ", ")

# Task 3 - Using Tuples
tuples = ('Interstellar', 'Paris', 'Silence')

print("\nFavorite things: ", tuples)

try:
    tuples[1] = "Summer Time"
    
except:
    print("Oops! Tuples cannot be changed.")

print("Length of tuple: " + str(len(tuples)))
