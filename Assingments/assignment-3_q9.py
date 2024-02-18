print("write a program to calculate factorial of given number .")
z=int(input("enter a number - "))

x=1
ans=1
while x<=z:
    ans=ans*x
    x=x+1
print("factorial of %d is %d"%(z,ans))