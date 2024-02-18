d={}
n=int(input("enter the size of the dictionary - "))

for i in range(n):
    d[i+101]=input("enter a value - ")

for x in d:
   print("key is - ",x,": value is - ",d[x])