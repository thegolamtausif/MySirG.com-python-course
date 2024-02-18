l=input("enter a string - ")
n=len(l)
items=[]
ans=[]
for item in l:
   if item not in items or item == " ":
      items.append(item)
      ans.append(item)
print("distinct charectors are - ",end=" ")
for i in ans:
   print(i,end="")