x=input("enter a string - ")
n=len(x)
c=input("enter the pattern - ")
ans=x.count(c)
if ans>=1:
    print("pattern found.")
else:
    print("pattern not found.")