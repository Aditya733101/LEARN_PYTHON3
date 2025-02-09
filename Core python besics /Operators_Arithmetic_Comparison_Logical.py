# Arithmetic Operators
a = 10
b = 3
print(a % b) # 1
print(a // b) # 3 (integer division)
print(a ** b) # 1000 (exponentiation)
print(a / b) # 3.3333333333333335
print(a * b) # 30

# Assignment Operators
x = 5
x += 3  # x = x + 3
x -= 2  # x = x - 2
x *= 2  # x = x * 2
x /= 2  # x = x / 2
x %= 2  # x = x % 2

# Comparison Operators
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False

# Logical Operators
# Used to combine conditional statements:
# and (True if both conditions are true)
# or (True if at least one condition is true)
# not (Reverses the result)
# Logical Operators
a = True
b = False

print(not a)  # False, because 'a' is True and 'not' reverses it
print(not b)  # True, because 'b' is False and 'not' reverses it

# Using 'not' with comparison operators
x = 10
y = 5

print(not (x > y))  # False, because 'x > y' is True and 'not' reverses it
print(not (x < y))  # True, because 'x < y' is False and 'not' reverses it