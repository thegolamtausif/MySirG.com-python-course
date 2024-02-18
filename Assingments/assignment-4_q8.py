#prime factors

x=int(input("enter a number - "))
print("prime factors of %d are -"%x,end=" ")
for i in range(1,x+1):
    if x%i==0:
        count=0
        for j in range(1,i+1):
            if i%j==0:
               count=count+1
        if count==2:
            print(i,end=",")