#hcf
#greatest common divisor

x=int(input("enter your first number - "))
y=int(input("enter your second number - "))
z = x if x<y else y

for i in range(1,z):
    if x%i==0 and y%i==0:
        gcd=i
print("gcd is - ",gcd)