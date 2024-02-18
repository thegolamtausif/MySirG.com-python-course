#co prime or not
#highest common factor of two number is 1 are called co prime 
x=int(input("enter your first number - "))
y=int(input("enter your second number - "))
z = x if x<y else y
for i in range(1,z):
    if x%i==0 and y%i==0:
        gcd=i

if gcd==1:
    print("%d and %d are co prime "%(x,y))
else:
    print("%d and %d are not co prime "%(x,y))
