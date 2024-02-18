print("write a program to calculate sum of first N  numbers")
z=int(input("enter a number - "))
y=0
x=1
a=1
while x<=z   :
    if a%2==1:
       y=y+a
       x=x+1
    a=a+1
print("result is %d"%y)