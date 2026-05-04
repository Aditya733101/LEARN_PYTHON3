# Python - Change List Items
thislist = ["mengo","cherry","orange","kiwi","banna"]
# before change the list
print(thislist)
# After change the list
thislist[1:2] = ["papai","luchi"]
print(thislist)

#  Change All Values Using Loop
num=[1,2,3]
for i in range(len(num)):
    num[i]=num[i]*2
    print(num[i])