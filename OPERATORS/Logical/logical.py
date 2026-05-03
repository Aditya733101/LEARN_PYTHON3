# logical operators are used to combine conditional statements. There are three logical operators in Python: and, or, and not.
#. 1) and operator 2) or operator 3) not operator 

# 1) and operator: The and operator returns True if both statements are true, otherwise it returns False.

# age = int(input("enter your age  - "))
# if age >=18 and age<=30:
#     print("you are eligible for this job")
# else:
#     print("you are not eligible for this job")

#  2) or operator: The or operator returns True if at least one of the statements is true, otherwise it returns False.
age_no = int(input("enter your age - "))
if age_no < 18 or age_no > 30:
    print("you are not eligible for this job")
else:
    print("you are eligible for this job")