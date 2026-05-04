#  check palindrome or not
mylist = ["apple", "banana", "apple"]
temp=mylist.copy()
mylist.reverse()
if mylist==temp:
    print("palindrome")
else:
    print("not palindrome")