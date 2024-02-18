d={}
n=int(input("enter the size of the dictionary - "))
li=[]
for i in range(n):
    t=eval(input("enter roll_no,name - "))
    d[t[0]]=t[1]
    t.clear()
for j in d:
    li.append(j)
li.sort()
for x in li:
    print(" roll is -",x,"name is -",d[x])

