n=int(input("enter the value of N - "))

l=[]
print("list of containing %d prime numbers is  L ="%n,end=" ")
for i in range(1,10000):
      if n>0:
          for j in range(2,i):
               if i%j==0:
                  break   
          else:
              l.append(i)
              n-=1

print(l)