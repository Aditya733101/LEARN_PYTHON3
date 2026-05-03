#simple interest calculator
principle_Amount = float(input("enter the principle Amount - "))
rate_of_interest= float(input("enter the rate of interest - "))
time_period = float(input("enter the time period - "))
simple_interest = (principle_Amount * rate_of_interest * time_period)/100
print("the simpleinterest is -", simple_interest)