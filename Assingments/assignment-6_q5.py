n=int(input("enter the value of N - "))
l=[]
print("List of squres of first %d natural numbers is L = "%n,end=" ")
for i in range(1,n+1):
     l.append(i**2)
print(l)