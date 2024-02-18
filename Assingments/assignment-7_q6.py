x=input("enter a string - ")
l=x.split()
l.sort()
n=len(l)
print("sorted in alphabetical order - ")
for i in range(n):
    print(l[i],end=" ")