d={}
n=int(input("enter the size of the dictionary - "))
for i in range(n):
    t=eval(input("enter roll_no,name - "))
    d[t[0]]=t[1]
    t.clear()
sortk = dict(sorted(d.items()))
print(type(sortk))
print("Sorted by key -",sortk)
sortv = dict(sorted(d.items(), key=lambda x: x[1]))
print("Sorted by value - ",sortv) 