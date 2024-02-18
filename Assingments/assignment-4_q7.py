#N odd natural numbers in reverse order 
x=int(input("enter your number - "))
print("first %d even numbers are -"%x,end=" ")
for i in range(2*x,0,-2):
   print(i,end=",")
