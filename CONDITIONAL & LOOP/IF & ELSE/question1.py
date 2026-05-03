num = int(input('enter the value  - '))
num2 = int(input('enter the value - '))
choich = input('Enter your choich /,* , + , - ')
if choich == '+':
    print(num+num2)
elif choich == '-':
    print(num-num2)
elif choich == '*':
    print(num*num2)
elif choich == '/':
    print(num/num2)
else:
    print("invalid input")