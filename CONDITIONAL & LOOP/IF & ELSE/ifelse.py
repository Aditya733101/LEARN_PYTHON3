# if else conditional statement is used to execute a block of code if a condition is true and another block of code if the condition is false.
marks=float(input("enter the marks - "))
if marks <=25:
    print("you are fail")
elif marks >25 and marks <=45:
    print("you are pass")
elif marks >45 and marks <=60:
    print("you are second class")
elif marks >60 and marks <=80:
    print("you are first class")
else:
    print("you are distinction")