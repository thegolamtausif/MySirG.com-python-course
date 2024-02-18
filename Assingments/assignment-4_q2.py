print("next prime number of given number ")
x=int(input("enter a number - "))
count=0
y=x+1
for i in range(x+1,1000000):
   for j in range(1,i+1):
      print(y,j)
      if y%j==0:
       count+=1
   if count<=2:
     print("ans is - ",y)
     break
   else:
       count=0
       y+=1
