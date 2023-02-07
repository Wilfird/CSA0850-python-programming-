a=input("enter the grade of the employee:")
b=int(input("enter the salary of the employee:"))
if a=='A':
    print("the salary along with the bonus:",(5/100*b)+b)
elif(a=='B'):
    print("the salary along with the bonus:",(10/100*b)+b)
elif b<10000 and a=='A':
    print("the salary along with the bonus:",(7/100*b)+b)
elif b<10000 and a=='B':
    print("the salary along with the bonus:",(12/100*b)+b)
