n=int(input("enter the size of the list - "))

l=[]
for i in range(n):
      l.append(int(input("enter a number -")))

sum=0
for i in range(n):
       sum=sum +  l[i]

print("sum is - ",sum )