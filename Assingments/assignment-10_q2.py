d={}
n=int(input("enter the size of the dictionary - "))

for i in range(n):
    d[i+101]=input("enter student name whose roll is %d  - "%(i+101))

for x in d:
   print("roll is - ",x,",name  is - ",d[x])