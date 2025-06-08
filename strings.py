# Assignment: Exploring String Methods

# Task 1 - String Slicing and Indexing
string = "Python is amazing!"

# Used slicing to extract the first word
print("First word: ", string[0:6])

# Used slicing to extract the Amazing part
print("Amazing part: ", string[10:17])

# Reverses the string
print("Reversed string: ", string[::-1])

# Task 2 - String Methods
sTring = " hello, python world! "

# strip
stripped = sTring.strip()
print("strip():", str(stripped))

# capitalize
capitalized = stripped.capitalize()
print("capitalize():", str(capitalized))

# replace
replace = capitalized.replace("World", "Universe") 
print("After replace():", str(replace))

# uppercase
uppercase = replace.upper()
print("After upper():", str(uppercase))

# Task 3
input = input("Input a word: ")

slice = input[::-1]

if input == slice:
    print("Yes, " + slice + " is a palindrome!")
else:
    print("The word is not a palindrome")

    