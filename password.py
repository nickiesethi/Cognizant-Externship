import string # import the strings lib to be able to access characteristic checkers

# prompt user to enter input
password = input("Input a password: ")

# conditions

# if password is less than 8 characters
if len(password) < 8:
    print("Your password needs at least one more character.")
# if there is no uppercase letter at all
if not any(char.isupper() for char in password):
    print("Your password needs at least one uppercase character")
# if there is no lowercase letter at all
if not any(char.islower() for char in password):
    print("Your password needs at least one lowercase character")
#  if there is no digit at all
if not any(char.isdigit() for char in password):
    print("Your password needs at least one digit")
# if there is no special chars in the password
if not any(char in string.punctuation for char in password):
    print("Your password needs at least one special character")
# if it meets all criteria for a strong password
else:
    print("Your password is strong! 💪")
