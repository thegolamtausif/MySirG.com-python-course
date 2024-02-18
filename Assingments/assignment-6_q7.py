l=[10,10,15,12,12,4,5,2,10,12,11,45,32,12,15]
print("the list is - ",l)
n=len(l)
ans=[]
items=[]
for item in l:
   if item not in items:
       items.append(item)
       for i in range(n):
         if l[i]==item:
           ans.append(i)
       print(item,ans)
       ans.clear()