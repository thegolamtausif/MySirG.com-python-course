print("first N prime number ")
x=int(input("enter a number - "))
count=0
c=0
print("first %d prime numbers are -"%x,end=" ")
for i in range(1,1000000):
   y=i
   for j in range(1,i+1):
      if y%j==0:
       count+=1
   if count<=2:
     print(y,end=",")
     c+=1
   else:
       count=0
   if c==x:
      break
for i in range(1,x+1,1):
    if x%i==0:
     count+=1
if count<=2:
   print()
    