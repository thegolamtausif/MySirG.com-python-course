x=int(input("enter the value of N - "))
c=0
s=set()
for i in range(100):
  if x>0:
   for j in range(2,i):
    if i%j==0:
        break
   else:
     s.add(i)
     x-=1
print("prime numbers are - ",s)
