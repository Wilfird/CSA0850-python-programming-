num=int(input("enter the number "))
sum=0
for i in range(0,num):
    if(num%i==0):
        sum=sum+1
if(sum==num):
    print("yes")
else:
    print("no")
