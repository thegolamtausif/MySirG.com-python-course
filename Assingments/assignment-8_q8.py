print(" cheack they are same in any order or not. ")
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
if x==y:
    print("yes they are same.")
else:
    print("no, they are not same.")