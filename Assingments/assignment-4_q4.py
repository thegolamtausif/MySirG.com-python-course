print("next prime number of given number ")
x=int(input("enter first number - "))
z=int(input("enter second number - "))
print("prime numbers between %d and %d are -"%(x,z),end=" ")
count=0
for i in range(x,z):
   y=i
   for j in range(1,i+1):
      if y%j==0:
       count+=1
   if count<=2:
     print(y,end=",")
   else:
       count=0
       y+=1
