#example :1  check odd and even 
start=int(input('Enter the strating number -'))
end = int(input('Enter the the last number - '))
for i in range(start,end):
    if i%2==0:
        print('even no - ', i)
    else:
        print('odd no - ', i)


# example 2 : find the sum of no 
start=int(input('Enter the strating number -'))
end = int(input('Enter the the last number - '))
sum=0
for i in range(start,end):
    sum+=i
print(sum)