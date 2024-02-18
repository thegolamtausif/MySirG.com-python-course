a=int(input("enter a number - "))
b=int(input("enter a number - "))
s=range(a,b)
count=0
for i in s:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i," is prime in range")
        break