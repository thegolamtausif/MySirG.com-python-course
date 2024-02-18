#lcm
x=int(input("enter your first number - "))
y=int(input("enter your second number - "))
z = x if x>y else y
for i in range(z,10000):
    if i%x==0 and i%y==0:
        lcm=i
        break
print("lcm is - ",lcm)