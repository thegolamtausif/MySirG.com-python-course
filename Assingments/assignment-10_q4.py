d={}
n=int(input("enter the size of the dictionary - "))
li=[]
t=[]
for i in range(n):
    t=eval(input("enter roll_no,name - "))
    d[t[0]]=t[1]
    t.clear()
for j in d:
    li.append(d[j])
li.sort()
print(li)
for x in li:
    for o in d:
       if d[o]==x:
        print(" roll is -",o,"name is -",x)
