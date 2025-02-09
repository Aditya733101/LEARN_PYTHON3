# 1.input() – Taking User Input
# The input() function is used to get input from the user via the keyboard.
# It always returns the input as a string by default.
# If you need a number, you must convert it to int or float.
name = input("enter the name ")
print("Hello", name) # output : Hello Aditya

# 2. print() – Displaying Output
# The print() function is used to display text or variables on the screen.
# It can take multiple arguments, separated by a comma (,).
# By default, it adds a space between them
print("Hello", "World") # output : Hello World

# 3. input() with Type Conversion
# Since input() always returns a string, you need to convert it to an integer or float if necessary.

#  Example: Taking numerical input
age = int(input("Enter your age: "))  # Converts input to an integer
print("You are", age, "years old.")


