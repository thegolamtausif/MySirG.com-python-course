n=int(input("enter the size of the list - "))

l=[]
for i in range(n):
      l.append(int(input("enter a number -")))

l.sort()
print(l)