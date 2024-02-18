l=[10,10,15,12,12,4,5,2,10,12,11,45,32,12,15]
print("the list is - ",l)
n=len(l)
ans=[]
item=int(input('enter the number you want to find - '))
for i in range(n):
    if l[i]==item:
        ans.append(i)
print("ans is -" ,ans)