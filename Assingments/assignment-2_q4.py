print("progran to find greatest among three numbers. ")

x=int(input("enter first number - "))
y=int(input("enter second number - "))
z=int(input("enter third number - "))

if x>y:
    c=x
else:
    c=y

if c>z:
    print("%d is the gratest number"%c)
else:
    print("%d is the gratest number"%z)

print("process finished.")