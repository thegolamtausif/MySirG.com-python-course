print("given number is prime or not")
x=int(input("enter a number - "))
count=0
for i in range(1,x+1,1):
    if x%i==0:
     count+=1
if count>2:
    print("%d is not a prime no."%x)
else:
    print("%d is a prime no."%x)
    