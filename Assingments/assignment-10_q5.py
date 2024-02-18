d={}
n=int(input("enter the size of the dictionary - "))
sum=0
for i in range(n):
    d[i]=int(input("enter the value in key %d  - "%i))

for x in d:
   sum= sum + d[x]
print("sum is = ",sum)  