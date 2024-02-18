print(" merge two sorted tuples. ")
a=eval(input("enter the values of first tupple - "))
b=eval(input("enter the values of second tupple - "))

z=[]
z=list(a)
z.sort()
x=tuple(z)

z.clear()
z=list(b)
z.sort()
y=tuple(z)

ans=()
ans=x+y 
print(ans)

